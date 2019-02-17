"""
Using links.txt, scrape and download all of Opportunity's images that are:
- From the left facing HAZCAM
- Full frame

Helper functions used info from https://mars.nasa.gov/mer/gallery/edr_filename_key.html
"""

from requests_html import HTMLSession
import os


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


if not os.path.exists("oppyImages"):
    os.mkdir("oppyImages")

with open("links.txt", "r") as f:
    imgLinks = f.read().strip().split("\n")

session = HTMLSession()
for imgLink in imgLinks:
    r = session.get(imgLink)
    for anchor in r.html.find("a"):
        try:

            currentURL = anchor.attrs["href"]
            if currentURL.endswith(".JPG"):

                filename = currentURL.split("/")[-1]
                sol = currentURL.split("/")[2]
                timestamp = filename[2:11]
                newFilename = f"{sol}-{timestamp}"

                if fromOppLeftHZCM(filename) and isFullFrame(filename):

                    print(f"Found image from sol {newFilename}")
                    if os.path.isfile(f"oppyImages/{newFilename}.jpg"):
                        continue

                    rawImgURL = getRawImageURL(currentURL)
                    rawImg = session.get(rawImgURL).content
                    print(currentURL, "downloaded")

                    with open(f"oppyImages/{newFilename}.jpg", "wb") as imageOut:
                        imageOut.write(rawImg)

        except KeyError:
            pass
