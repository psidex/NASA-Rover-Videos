"""
Iterates all images in {imageDir} and adds the filename (which should be sol-timestamp)
to the top left of the image and saves them to {newImageDir}
"""

from PIL import Image, ImageFont, ImageDraw
import datetime
import os

# Variables to change
imageDir = "roverImages"
newImageDir = "roverImagesWithText"
# - - - - - - - - - -

# January 1, 2000 at 11:58:55.816 UTC.
initialTimestamp = datetime.datetime(
    year=2000, month=1, day=1, hour=11, minute=58, second=55, microsecond=816_000
)

imageNames = [img for img in os.listdir(imageDir) if img.endswith(".jpg")]
# IMPORTANT: Must have FiraCode-Regular.ttf either installed or downloaded in this dir
font = ImageFont.truetype("FiraCode-Regular.ttf", 30)

if not os.path.exists(newImageDir):
    os.mkdir(newImageDir)

for imageName in imageNames:
    print(f"Processing {imageName}")

    try:
        img = Image.open(os.path.join(imageDir, imageName))
    except OSError:
        continue  # File corrupted / unusable

    sol, timestamp = imageName.replace(".jpg", "").split("_")

    earthTime = initialTimestamp + datetime.timedelta(seconds=int(timestamp))
    earthTimeFormatted = earthTime.strftime("%b %d %Y - %H:%M:%S")

    # Prepend "sol ", remove file extension, and add spaces to make it look better
    imageText = f"{earthTimeFormatted}\nsol {sol} - {timestamp}"

    draw = ImageDraw.Draw(img)
    draw.text((0, 0), imageText, (255, 255, 255), font=font)

    img.save(os.path.join(newImageDir, imageName))
