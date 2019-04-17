from __future__ import print_function
import os, sys
from PIL import Image


#construct the path that points to the picture you're working with, then opens it.
file = "mtns.jpg"
#converting an image to mode "L" will make it grayscale
image = Image.open(file)
#trying out how to save a new file.  Always call this on the last product (end)
newfile = "mountains.jpg"
box = (100,100,400,400)
region = image.crop(box)
region = region.convert("L")
region.show()
image.paste(region, box)
image.show()
#r,g,b = region.split()
#region = Image.merge("RGB", (b,r,g))

#Debug area
print(image.format, image.size, image.mode)
print(file)
try:
	image.save(newfile)
except AttributeError:
	print("Could not save photo")