"""
Using links.txt, scrape and download all of Opportunity's images that are:
- From the left facing HAZCAM
- Full frame

Helper functions used info from https://mars.nasa.gov/mer/gallery/edr_filename_key.html
"""

from requests_html import HTMLSession
import os

imageDir = "oppyImages"


def fromOppLeftHZCM(imageName):
    """
    Detect if image is from Opportunity's left Forward HAZCAM
    """
    if imageName[0] == "1" and imageName[1] == "F" and imageName[23] == "L":
        return True
    return False


def isFullFrame(imageName):
    """
    Detect if image is "Full Frame"
    """
    if imageName[11:14] == "EFF":
        return True
    return False


def getRawImageURL(relativePath):
    return "https://mars.nasa.gov/mer/gallery/all/" + relativePath


def getImageURL(tagObject):
    """
    Return either the URL to the image or False
    """
    try:
        imageURL = tagObject.attrs["href"]
        if imageURL.endswith(".JPG"):
            return imageURL
    except KeyError:
        pass
    return False


if not os.path.exists(imageDir):
    os.mkdir(imageDir)

with open("links.txt", "r") as f:
    imgLinks = f.read().strip().split("\n")

    # For testing the corrupted version overwriting (see comments below)
    # imgLinks = ["https://mars.nasa.gov/mer/gallery/all/opportunity_f3644_text.html"]

session = HTMLSession()
for imgLink in imgLinks:
    r = session.get(imgLink)

    for anchorTag in r.html.find("a"):

        currentURL = getImageURL(anchorTag)
        if not currentURL:
            continue  # Skip this non-image URL

        filename = currentURL.split("/")[-1]
        sol = currentURL.split("/")[2]
        timestamp = filename[2:11]
        newFilename = f"{sol}-{timestamp}"

        # Sometimes there are multiple photos with the same {newFilename}, as there are
        # multiple versions of some images, the latest version of which is better
        # quality / less corrupted. Because the <a> tags are read in the correct order,
        # the "best" version will be read last and will overwrite the previous
        # version(s). This does however mean that bandwidth will be wasted downloading
        # images to be immediatley be overwritten

        # TODO: Instead of overwriting, look at all the filenames and check for
        # duplicates with different / higher versions

        if fromOppLeftHZCM(filename) and isFullFrame(filename):
            print(f"Found image from sol {newFilename}")

            rawImgURL = getRawImageURL(currentURL)
            rawImg = session.get(rawImgURL).content

            with open(f"{imageDir}/{newFilename}.jpg", "wb") as imageOut:
                imageOut.write(rawImg)

            print(currentURL, "downloaded")
