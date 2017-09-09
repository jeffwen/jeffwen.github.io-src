Title: Setting up the blog
Date: 2015-11-28 13:03
Author: Jeff Wen
Slug: pelican-setup
Category: Misc
Summary: Setting up the blog and things to remember
Index_image_url:/images/setup_blog_index.png

_November 28, 2015_

Over the past couple of days, I have been working towards getting a blog up and running. There were a couple of different options that I was considering and ultimately I ended up choosing to use [Pelican](http://blog.getpelican.com) as my site generator. I also use GitHub Pages to host my blog for free!

### Decisions 
Initially, I was considering just sticking with Jekyll, which is the site generator that pairs really nicely with [GitHub Pages](https://help.github.com/articles/using-jekyll-with-pages/). However, I read a couple different posts by other users, thought about the decision, and noticed the following:

1. _Ruby vs. Python_: Jekyll is Ruby based whereas Pelican is Python based.
    * Although I am also picking up Ruby, I am definitely more comfortable with Python at this point.

2. _Speed_: While I am still new to blogging and don't necessarily feel the struggle of slow page loading (given that I don't have much experience with slow loading blogs), [this user's](http://arunrocks.com/moving-blogs-to-pelican/) blog post was definitely persuasive enough for me to take speed into consideration.

3. _Personal Growth_: Jekyll might have been easier to use given that it is integrated with GitHub so well, but I wanted to (at least in my mind at the time) learn a little bit more by using something that required just a little more work. 

### Getting Started
With these things in mind, I decided to jump right in and start setting up my blog. It was quite simple for the most part but it definitely took some time figuring everything out because I was trying to use a couple different resources to make sure that my blog would run smoothly. Looking back on it, I guess it probably would have been better to stick with one solid resource vs. trying to merge different ways of doing the same thing. However, as stated before, I wanted to learn as much as possible and see the different ways people were setting up their blogs.

- Resources:
    - [Pelican Documentation](http://docs.getpelican.com/en/3.6.3/)
    - [Amy Halon's blog post on GitHub Pages Migration](http://mathamy.com/migrating-to-github-pages-using-pelican.html)
    - [Fedora Magazine's blog post on GitHub Pages and Pelican](https://fedoramagazine.org/make-github-pages-blog-with-pelican/)

As I was following some of the resources mentioned earlier, I realized that it was a great opportunity for me to also learn more about other technologies as well. For example, I read up on GitHub submodules because Fedora's post mentioned initiaizing the output directory as a submodule. I am getting my hands dirty with Markdown because I am using Markdown to write these blog posts and pages. Additionally, HTML and CSS are relevant as well because I am learning to customize my blog. Therefore, all in all, things seem to be going pretty smoothly and I am excited to see what else I can do with this site!

### Customization
#### New Posts
In order to get more familiar with the workings of the platform/ try to customize what I was doing, I decided to write my own function to help speed up the process of writing a new blog. Pelican makes this quite simple with the fabfile.py, which allows you to create new functions for anything that you may want to customize.

In my case, I wanted to be able to create new posts from the command line. So by typing the following I can now create a new Markdown file in my content folder with the title, slug, date, etc. preformatted.
```bash
fab newpost:"title of my post"
```
The code that makes this happen is just a simple function that fills in a prespecified template.

```python
TEMPLATE = """
Title: {title}
Date: {year}-{month}-{day} {hour}:{minute}
Category:
Slug: {slug}
Summary:
Status: draft
"""
```
```python
def newpost(title):
    today = datetime.today()
    slug = title.lower().strip().replace(' ', '_')
    f_create = "content/{}{:0>2}{:0>2}_{}.md".format(
        today.year, today.month, today.day, slug)
    t = TEMPLATE.strip().format(title=title,
                                year=today.year,
                                month=today.month,
                                day=today.day,
                                hour=today.hour,
                                minute=today.minute,
                                slug=slug)
    with open(f_create, 'w') as w:
         w.write(t)
    return t
    print("File created -> " + f_create)
```
#### Themes
I also wanted to experiment with HTML/ CSS and modify the themes that I was using on my blog. I started with the [SVBHACK](https://github.com/gfidente/pelican-svbhack) theme but did not really like that the index and archives links were at the top of the page, which seemed to clutter the simplicity of the page. This was a pretty simple customization that I fixed by changing some of the HTML template code to move the links around but now the top of the page is clean!

Original:

![original index and archives](/images/index_archives_orig.png)

Modified:

![new archives](/images/archives_new.png)

I was also interested in customizing the color of the side column and so that took some time digging through the style sheet to make it look the way I wanted. Anyways, now things seem to be the way I want them and I hope that they don't break.

### Writing and Viewing
Pelican actually makes it surprisingly simple to write and view what has been written.

With the function that I wrote above, I can now create first drafts pretty quickly, then when I want to see the post on my blog, Pelican allows for a local server to be created to view the changes. What is most awesome is that if I use

```bash
make devserver
```
I can actually have the page regenerate each time with new content and all I have to do is refresh the page. So now I can make sure that everything is formatted correctly before I publish my posts.

### Final Thoughts
As I learn more about Pelican and blogging in general, I may update this post to include new information about customizations or features that I learn about!
