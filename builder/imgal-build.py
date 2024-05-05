import os, sys
from PIL import Image
import shutil

title = input("Enter the gallery title > ")
description = input("\nEnter a description for the gallery > ")
author = input("\nEnter the author's name > ")
authorContact = input("\nEnter the author's email. You can leave this blank to hide the contact link. > ")
showWatermark = input("\nDo you want to show a small 'made with Imgal' note at the bottom of the website? (Y/N/y/n) > ")
directory = input("\nWhat folder/directory are the images located in (example : ./pics/pngFiles) > ")

def resize_image(directory, image_path, max_size):
    # Open the image file
    image = Image.open(f"./{directory}/{image_path}")

    # Calculate aspect ratio
    width, height = image.size
    aspect_ratio = width / height

    # Determine the maximum size while maintaining aspect ratio
    if width > height:
        new_width = min(width, max_size[0])
        new_height = int(new_width / aspect_ratio)
    else:
        new_height = min(height, max_size[1])
        new_width = int(new_height * aspect_ratio)

    # Resize the image
    image.thumbnail((new_width, new_height))

    # Return the resized image
    return image

def createPage(picsList):

    i = 1
    picsCode = ""
    for x in picsList:
        picsCode += f"<div class='images'>\n\t<a href='./view.html?img=./viewer/{x}_viewer.png&target=./fullSize/{x}'><img src='./thumbnails/{x}_thumbnail.png' onerror='this.onerror=null; this.remove()'></a>\n</div>\n"

    multiples_3 = [n for n in range(0, 9999) if n % 3 == 0]

    closest = min(num for num in multiples_3 if num >= len(picsList))
    emptyDivs = closest - len(picsList)
    for x in range(emptyDivs):
        picsCode += f"<div class='emptyDiv'></div>\n"

    if authorContact == "":
        contactAuthorA = ""
        footerHr = ""
    else:
        contactAuthorA = f"<a href='mailto:{authorContact}'>Contact Author</a>"
        footerHr = "<div class='hr'></div>"

    data = {
        "title":title,
        "description":description,
        "author":author,
        "images":picsCode,
        "contactAuthor":contactAuthorA,
        "footerHr":footerHr
    }

    dataV = {
        "title":title,
        "description":description,
        "author":author,
        "contactAuthor":contactAuthorA,
        "footerHr": footerHr
    }

    if showWatermark.lower() == "y":
        data['watermark'] = "<div id='footer'><p>Created with Imgal - KIOYDIOLABS © 2024</p></div>"
        dataV['watermark'] = "<div id='footer'><p>Created with Imgal - KIOYDIOLABS © 2024</p></div>"
    else:
        data['watermark'] = ""
        dataV['watermark'] = ""

    template = open("./templates/index.html").read()
    templateView = open("./templates/view.html").read()
    for key, value in data.items():
        template = template.replace(f"{{{{{key}}}}}", value)
    for key, value in dataV.items():
        templateView = templateView.replace(f"{{{{{key}}}}}", value)

    with open(f"{directory}/index.html", "w", encoding="utf-8") as f:
        f.write(template)
    with open(f"{directory}/view.html", "w", encoding="utf-8") as f:
        f.write(templateView)

    stylesheet = open("./templates/style.css").read()
    with open(f"{directory}/style.css","w") as f:
        f.write(stylesheet)

def createThumbnails(picsList, directory):
    os.makedirs(f"./{directory}/thumbnails")

    for x in picsList:
        thumbnail = resize_image(directory, x, (120,120))
        thumbnail.save(f"./{directory}/thumbnails/{x}_thumbnail.png")

def createViewerSize(picsList, directory):
    os.makedirs(f"./{directory}/viewer")

    for x in picsList:
        thumbnail = resize_image(directory, x, (406,300))
        thumbnail.save(f"./{directory}/viewer/{x}_viewer.png")

def moveFullSize(directory, file_names):

    os.mkdir(f"{directory}/fullSize")

    for file_name in file_names:
        shutil.move(os.path.join(directory, file_name), f"{directory}/fullSize")


picsList = os.listdir(directory)
try:
    createPage(picsList)
    createThumbnails(picsList, directory)
    createViewerSize(picsList, directory)
except Exception as e:
    print("Error occurred. Bypassing image. Details : "+e)
moveFullSize(directory, picsList)