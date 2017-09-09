Title: Making Census Data Exciting (Part 1)
Date: 2016-2-27 13:31
Author: Jeff Wen
Category: Python
Slug: making_census_data_exciting_part_1
Summary: Setting up the AWS EC2 used to store census data and also discussing some project design choices
Index_image_url:/images/census_1_index.png

_February 27, 2016_

Let's talk about remote servers, census data, classification models, and data visualization...lots to cover...

_Warning:_ This post will be a bit lengthy and cover some details that might not be that interesting but I am also using this post as a way to capture the process so I don't forget things.
![Census Logo](/images/census-logo.png)
### Summary
In this post, I will discuss some of the design decisions that I made while working on this project and also go through some of the set up required to get things up and running. To start off with the goal of this project was to take census data and use it and visualize it in an interesting way.

While I did not really have a clear idea when I started the project, I worked with a couple of my teammates to come up with an overall plan. We had to use [census data](https://archive.ics.uci.edu/ml/datasets/Census+Income) and also had to think about how to tell a story with that data using classification models and D3.js. With this said, we really racked our brains to try to figure out how to use the data in an interesting way. I think we eventually did and will share more in the upcoming 2 posts!

### Setup
One of the tools that I wanted to start playing around with was Amazon's EC2 servers because the trial version is free for the first year and I also wanted to learn the technology! However, the set up for the EC2 server was actually not as straight forward as I would have imagined. Particularly because I wanted to use PostgreSQL and directly connect to the server to pull data into my local machine to analyze with Python (Psycopg2 to the rescue).

#### Amazon Instance
Anyways, the first step was to create the EC2 instance:

1. Make sure that you have an AWS account and select a region that makes sense (in my case US West)
2. Choose one of the configurations that you want (my teammates and I chose Ubuntu)
3. Select a "free tier" instance ("t2.micro" for me!)
4. Walk through the setup process by following the prompts
5. Setup security groups
	* This part was a bit confusing because PostgreSQL required another port to allow connections from my local machine's Python (will talk more about this later)
6. Choose to "Create a new key pair" and give it a name
7. Download your .pem file.
8. Move the file somewhere sensible like ~/.ssh/.
9. Make the file read only with chmod 400 filename

At this point, the server is set up and can be accessed using:

```bash
ssh -i ~/.ssh/my_cool_machine.pem ubuntu@123.234.123.234
```

#### Loading the tools and getting things ready
At this point we needed to get a couple packages onto the server so that we could get working. `apt-get` is awesome for this when using Ubuntu.

1. First of all we needed to be able to install Python related things:
	* Use `pip` to install Python things: `sudo apt-get install python-pip`
	* Other scipy things: `sudo apt-get install python-numpy python-scipy python-matplotlib ipython ipython-notebook python-pandas python-sympy python-nose`
	* I like git and emacs :) : `sudo apt-get install git emacs`
2. Instead of signing in as 'Ubuntu' I added myself as a user:
	* `sudo adduser [username]`
	* Grant total access: `sudo visudo` which will open a nano text file
		* Add `[username] ALL=(ALL:ALL) ALL`
3. Setup public key by following this [link](http://docs.oracle.com/cd/E19253-01/816-4557/sshuser-33/index.html)
	* Once the public key is generated copy it/ paste it onto remote server (copy/ paste probably isn't the best way... but it works!)
		* Copy this `~/.ssh/id_rsa.pub`
		* Create proper files on remote machine `sudo mkdir /home/my_cool_username/.ssh/`
		* Paste the copied public key into the authorized keys file `sudo nano /home/my_cool_username/.ssh/authorized_keys`
	* This should work now! `ssh my_cool_username@123.234.123.234`
4. Make it easier to login
	* Edit ssh config file by adding
		* `Host my_cool_machine`
		* `User my_cool_username`
	* Edit `/etc/hosts` file
		* `Host_ip my_cool_machine`
5. Finally we can now login using `ssh my_cool_machine`
	* And easily move things over to the remote machine using `scp cool_file.png my_cool_machine:~`


#### PostgreSQL
In order to start using PostgreSQL I had to install PostgreSQL onto the remote machine and set up the access so that I could reach it from my local machine through Python.

1. Install PostgreSQL `sudo apt-get install postgresql postgresql-contrib`
	* Start and stop the PostgreSQL server using the following
		* `sudo service postgresql status`
		* `sudo service postgresql stop`
		* `sudo service postgresql start`

2. Installing PostgreSQL created a `postgres` user, but to add myself as a user I had to

```bash
sudo -u postgres createuser --superuser my_user_name
sudo -u postgres psql
# now in psql...
\password my_user_name
# exit out of psql with Ctrl+D
# Create a database for your user
sudo -u postgres createdb my_user_name
```

### Load the data
At this point the Postgres environment was set up but there was no data yet! So in order to add some data, I found it easiest to just directly import a `.csv` file. However, I had to create the database first.

```sql
CREATE DATABASE census;
```

Then switch to the newly created database `\c endor`

```sql
CREATE TABLE census (
	id SERIAL PRIMARY KEY,
	age INT; 
	workclass TEXT,
    fnlwgt INT,
    education TEXT,
    education_num INT,
    marital_status TEXT,
    occupation TEXT,
    relationship TEXT,
    race TEXT,
    sex TEXT,
    capital_gain INT,
    capital_loss INT,
    hours_per_week INT,
    native_country TEXT
);
```

Now with the data table set up, I scp'ed the census data from my local machine to the remote machine and copied the data into database.

```sql
COPY census FROM '/path/to/ewoks.csv' DELIMITER ',' CSV HEADER;
```

###Permissions
Now the Postgres database is set up and work can begin if I wanted to do all the work on my remote machine. However, it is much easier to work from my local machine so I had to change a few things in the Postgres configuration files and my Amazon AWS security group.

Lets start with the AWS security group. Whenever I want to log into my remote machine from a different IP address I need to add a 'rule' that allows that new IP address (or I can set it to allow any IP but thats probably not the best). So under security group on my AWS I add a new SSH with my current IP address. But I also need to allow communication with the Postgres database. Luckily, AWS has a pretty smooth process for this. Once again I add a 'rule' but this time from the drop down I select 'PostgreSQL' and I can allow any IP address to access the databse or some specified ones.

![Postgres AWS](/images/postgre_aws.png)

In order to edit the Postgres configuration files, I need to go back into my remote machine. There are 2 files that I need to edit.

* `sudo nano /etc/postgresql/9.3/main/postgresql.conf`
	* Under 'CONNECTIONS & AUTHENTIFICATION' change the 'listening_addresses' from 'localhost' to '*' this will allow all to access
		* `listen_addresses = '*'`
* `sudo nano /etc/postgresql/9.3/main/pg_hba.conf`
	* Under 'IPv4 LOCAL CONNECTIONS' I change the allowed IPs
		* `host all all 0.0.0.0/0 trust`

FINALLY. At this point, I can actually access my remote database from my local machine. However, when using Python and psycopg2 to access the database there were a few more hurdles that I had to jump over :(.


###Psycopg2 and Python
To directly connect with the database I had to install [psycopg2](http://initd.org/psycopg/), which is a Postgres adapter for Python. I did the following in order to get the set up working... (lots of steps and troubleshooting; took  me a long time to figure out the last step)

```python
brew install postgresql
pip install psycopg2
# this next step I had to preform only because it kept throwing back an error saying that my
# AWS was not set up correctly but when I looked on stackoverflow it seemed like it was a psychopg2 bug
brew unlink openssl && brew link openssl --force
```

### Finishing up
Whew! That was exciting. I know...

The process to get the server and database all set up may seem quite tedious, but many of the steps above are actually quite quick! Plus, it is good to have things all set up so that the analysis and visualization steps can happen smoothly! In the next post, I will discuss more of the details behind the analysis and also hopefully show a working version of the D3 dashboard!
