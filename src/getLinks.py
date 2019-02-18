"""
Scrape NASAs Opportunity image page and get all the URLs for images from each Sol from
the front HAZCAM, and saves these to links.txt
"""

from requests_html import HTMLSession

initialURL = "https://mars.nasa.gov/mer/gallery/all/opportunity.html"
pageURLs = []

session = HTMLSession()
r = session.get(initialURL)

# All of the image URLs are stored in option tags
for option in r.html.find("option"):

    # If the URL is for the front HAZCAM
    imageURL = option.attrs["value"]

    if imageURL.startswith("opportunity_f"):
        imageURL = imageURL.replace(".html", "")
        pageURLs.append(f"https://mars.nasa.gov/mer/gallery/all/{imageURL}_text.html")

with open("links.txt", "w") as fOut:
    for url in pageURLs:
        fOut.write(f"{url}\n")
