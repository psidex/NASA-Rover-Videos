# Opportunitys-Journey

How I created my "Opportunity's Journey" video

## Steps

I started by looking at NASAs [offical image repository for Opportunity](https://mars.nasa.gov/mer/gallery/all/opportunity.html)

I then wrote [getLinks.py](src/getLinks.py) which scrapes this page, and gets all of the URLs that point to the sets of images taken by Opportunity's front-facing HAZCAM. It then saves this list of URLs to a file called `links.txt`

Now I have this list, I can load each of these URLs and scrape those pages for images specifically from the left HAZCAM, and specifically in the "Full Frame" format. I did not use the left over the right for any reason, I just had to pick one. I chose "Full Frame" because that seems to be the highest quality, and also the one that occurs the most (the different image types taken differ on each sol)

I wrote [downloadImages.py](src/downloadImages.py) which does what I described above, and downloads all of the matching images to the `oppyImages` directory

Now that I have all the images, I can just use cv2 to compile these all into one video, using [createVideo.py](src/createVideo.py)

[The final result](https://youtu.be/rtP6iYhFuqQ)
