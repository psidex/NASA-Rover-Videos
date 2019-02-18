"""
Iterates all images in {imageDir} and adds the filename (which should be sol-timestamp)
to the top left of the image and saves them to {newImageDir}
"""

from PIL import Image, ImageFont, ImageDraw
import os

# Variables to change
imageDir = "roverImages"
newImageDir = "roverImagesWithText"
# - - - - - - - - - -

imageNames = [img for img in os.listdir(imageDir) if img.endswith(".jpg")]
# IMPORTANT: Need to have FiraCode-Regular.ttf downloaded and in this dir
font = ImageFont.truetype("FiraCode-Regular.ttf", 30)

if not os.path.exists(newImageDir):
    os.mkdir(newImageDir)

for imageName in imageNames:
    print(f"Processing {imageName}")

    try:
        img = Image.open(os.path.join(imageDir, imageName))
    except OSError:
        continue  # File corrupted / unusable

    # Prepend "sol ", remove file extension, and add spaces to make it look better
    imageText = "sol " + imageName.replace(".jpg", "").replace("-", " - ")

    draw = ImageDraw.Draw(img)
    draw.text((0, 0), imageText, (255, 255, 255), font=font)

    img.save(os.path.join(newImageDir, imageName))
