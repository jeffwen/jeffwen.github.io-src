Title: Visaurant: Reimagining the food search experience
Date: 2016-5-2 14:26
Author: Jeff Wen
Category: Python
Slug: visaurant
Summary: Using computer vision techniques to visually filter and search through images
Index_image_url:/images/visaurant_index.png


_May 02, 2016_

![Visaurant Logo](/images/visaurant_logo.png)
This blog post is a work in progress and will detail the process that I took to create the Visaurant project.

Visaurant (as you can see in the video below) is a reimagination of the way users search through images that they are interested in. One prime use case for Visaurant is in sorting and filtering through food images (hence _VIS_ -ual rest- _AURANT_).

### Background
So why do we want a visual search application?

Images represent a wealth of information. As cliche as it sounds, _'a picture is worth a thousand words'_ especially when it comes to looking for food items that seem appetizing. Speaking from personal experience, I often use apps like Yelp by:

1. Going to the images of a particular restaurant
2. Looking for the pictures that look good
3. Reading the caption
4. Going back to the reviews to find the reviews regarding the item that I saw

While this process works, it is by no means streamlined. Having to go back and forth between the images, captions, and reviews is a hassle and quite often overwhelming because there are so many images to sift through. So although images are powerful and contain a lot of information, if the images are not ordered or organized then it becomes difficult to find what I care about (like the example below...).

![Yelp Restaurant Photos](/images/yelp_photo.png)

Visaurant aims to change that by:

1. Clustering visually similar images to allow users to quickly narrow down to images of interest
2. Parsing through captions to extract reviews that are relevant to the image that was selected

<iframe src="https://player.vimeo.com/video/165064797" width="640" height="344" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe>

#### What is happening in the video?

1. User gets to select a group of images from a restaurant that looks interesting (4 selections)
![Visaurant Selection](/images/visaurant_selection.png)
2. Recommendations will be made based on the user's selections
3. User can once again select the restaurant that looks most appealing
![Visaurant Recommendation](/images/visaurant_recommendation.png)
4. Restaurant specific page will show up allowing the user to hover over images that look interesting and images within the same visual cluster will be highlighted
![Visaurant Highlight](/images/visaurant_highlight.png)
5. User can select an image and all images will be filtered for images in the same cluster
![Visaurant Filtered](/images/visaurant_filtered.png)
6. After filtering down to a single cluster, user can select a specific image to bring up reviews that have matching words with the image's caption
![Visaurant Caption](/images/visaurant_caption.png)




