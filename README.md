# Opportunitys-Journey

How I created my "Opportunity's Journey" video - just some quick notes for anyone interested

## Steps

I started by looking at NASAs [offical image repository for Opportunity](https://mars.nasa.gov/mer/gallery/all/opportunity.html)

I then wrote [getLinks.py](src/getLinks.py) which scrapes this page, and gets all of the URLs that point to the sets of images taken by Opportunity's front-facing HAZCAM. It then saves this list of URLs to a file called `links.txt`

Now I have this list, I can load each of these URLs and scrape those pages for images specifically from the left HAZCAM, and specifically in the "Full Frame" format. I did not use the left over the right for any reason, I just had to pick one. I chose "Full Frame" because that seems to be the highest quality, and also the one that occurs the most (the different image types taken differ on each sol)

I wrote [downloadImages.py](src/downloadImages.py) which does what I described above, and downloads all of the matching images to the `oppyImages` directory

Now that I have all the images, I can just use cv2 to compile these all into one video, using [createVideo.py](src/createVideo.py)

[The final result](https://youtu.be/Bd8qvLp73Ls)

A similar video can be made from images taken by the rear left HAZCAM (with small changes to the getLinks and downloadImages scripts)

[You can see that video here](https://youtu.be/lcdB9VeV08Q)

Another similar video can be made for Spirits journey

[You can see that video here](https://youtu.be/2BNyX0kwEcE)

Read the description of each video for more info

## Update

After getting some reccomendations, I have added the sol & timestamp to the top left each frame

To do this I wrote [addText.py](src/addText.py)

I have also fixed a lot of the corrupted / lower quality images, which should make for a slightly smoother video

You can see an example of one of the [corrupted images](https://mars.nasa.gov/mer/gallery/all/1/f/3644/1F451694215EFFCC3OP1225L0M1.JPG) compared to the [better version of the same image](https://mars.nasa.gov/mer/gallery/all/1/f/3644/1F451694215EFFCC3OP1225L0M2.JPG)

The last change is that this new video is 10fps instead of 15fps, which essentially slows down the video and makes it easier to see what is happening

[You can watch the updated video here](https://youtu.be/Eexd4eWUEfo)
