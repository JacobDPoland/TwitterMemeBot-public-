# This file follows along with the following video by freeCodeCamp
# https://www.youtube.com/watch?v=8u-zJVVVhT4

# This is the web scraper

import requests  # allows python to get info about a website
from bs4 import BeautifulSoup as bs  # allows download of html for parsing
import os  # used to store images

# website with images
url = "https://cleanmemes.com/"

# download page for parsing
page = requests.get(url)  # requesting a response from the server on that page
soup = bs(page.text, 'html.parser')  # html that makes up the website

# locate all elements with image tag
image_tags = soup.findAll('img')  # raw html tags

# create directory if it doesnt already exist
if not os.path.exists('memes'):
    os.makedirs('memes')

# move to memes directory
os.chdir('memes')

# image file name variable
x = 0  # used to increment name of picture so they're not overwritten

i = 0
# writing images
for image in image_tags:
    try:
        url = image["src"]  # try to get the source link for the image (image is prob a dict)
        source = requests.get(url)
        if source.status_code == 200:  # if we get a response
            with open('meme-' + str(x) + '.jpg', 'wb') as f:  # create image name and write to it (wb)
                f.write(requests.get(url).content)  # write to f the contents of requsts (the image)
                f.close()  # close the file
                x += 1  # increment x for naming
        if i > 20:
            break
        else:
            i + 1
    except:  # if there is any problem in the loop (can't get image) the image is passed
        pass
