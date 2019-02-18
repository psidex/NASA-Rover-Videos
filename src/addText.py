"""
Iterates all images in {imageDir} and adds the filename (which should be sol-timestamp)
to the top left of the image and saves them to {newImageDir}
"""

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import os

imageDir = "oppyImages"
newImageDir = "oppyImagesText"
imageNames = [img for img in os.listdir(imageDir) if img.endswith(".jpg")]

# Need to have FiraCode-Regular.ttf downloaded and in this dir
font = ImageFont.truetype("FiraCode-Regular.ttf", 30)

if not os.path.exists(newImageDir):
    os.mkdir(newImageDir)

for imageName in imageNames:
    print(f"Processing {imageName}")
    imagePath = os.path.join(imageDir, imageName)

    try:
        img = Image.open(imagePath)
    except OSError:
        continue  # File corrupted

    draw = ImageDraw.Draw(img)

    # WE = Without Extension
    imageNameWE = imageName.replace(".jpg", "")

    sol, timestamp = [int(i) for i in imageNameWE.split("-")]

    # :04d = always 4 digits (e.g. sol 0006 - timestamp)
    imageText = f"sol {sol:04d} - {timestamp}"

    draw.text((0, 0), imageText, (255, 255, 255), font=font)

    img.save(os.path.join(newImageDir, imageName))
