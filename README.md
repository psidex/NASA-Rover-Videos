# Opportunitys-Journey

How I created "Opportunity's Journey" and various other videos

## Steps

1. I started by looking at NASAs [offical image repository for Opportunity](https://mars.nasa.gov/mer/gallery/all/opportunity.html)

2. I then wrote a script which scrapes this page, and gets all of the URLs that point to the sets of images taken by Opportunity's front-facing Hazcam

3. Now I have this list, I can load each of these URLs and scrape those pages for images specifically from the left Hazcam, and specifically in the "Full Frame" format. I did not use the left over the right for any reason, I just had to pick one. I chose "Full Frame" because that seems to be the highest quality, and also the one that occurs the most (the different image types taken differ on each sol)

4. I wrote another script which does what I described above, and downloads all of the matching images to a directory

5. Now that I have all the images, I can just use cv2 to compile these all into one video

[The final result](https://youtu.be/Bd8qvLp73Ls)

## Update

I have improved most of the code, and moved it all into 3 files:
- [downloadImages.py](src/downloadImages.py) - This will do steps 1-3, and can do it for Opportunity or Spirit, with either of the left/right front/rear Hazcams
- [addText.py](src/addText.py) - This is a new script which will take each image and write in the top left the sol and [timestamp](https://mars.nasa.gov/mer/gallery/edr_filename_key.html) from the rover
- [createVideo.py](src/createVideo.py) - This does what the name suggests, it takes all of the images and compiles them into one video

Each script has variables that you can edit to change certain aspects of the final video

[You can watch the updated Opportunity's Journey video here](https://youtu.be/Eexd4eWUEfo)
