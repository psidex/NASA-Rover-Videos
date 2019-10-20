# NASA Rover Videos

How I created [Opportunity's Journey](https://youtu.be/yFXFMiCPqY4) and several other videos.

## How it works

This example runs through what happens if you wanted to create a video using Opportunity's front-left hazcam:

- It starts by looking at NASAs [offical image repository for Opportunity](https://mars.nasa.gov/mer/gallery/all/opportunity.html)
- It scrapes this page and gets all of the URLs that point to the sets of images taken by Opportunity's front-left hazcams
- Each of these URLs are loaded and scraped for images that match the given parameters
- All images are then downloaded into a directory
- Each image in the directory is edited so that the timestamp appears in the top left of the image
- Finally all of the images are compiled into one video
