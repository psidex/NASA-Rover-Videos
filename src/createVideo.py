"""
Take all images from the "oppyImages" directory and compile them into a video
"""

from natsort import natsorted
import cv2
import os

frameRate = 15
imageDir = "oppyImages"
videoName = "output.avi"

images = natsorted([img for img in os.listdir(imageDir) if img.endswith(".jpg")])
frame = cv2.imread(os.path.join(imageDir, images[0]))
height, width, layers = frame.shape

video = cv2.VideoWriter(videoName, 0, frameRate, (width, height))

for image in images:
    print(f"Processing {image}")
    video.write(cv2.imread(os.path.join(imageDir, image)))

cv2.destroyAllWindows()
video.release()
