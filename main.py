from __future__ import print_function
import os
from PIL import Image


#construct the path that points to the picture you're working with, then opens it.
file = "mtns.jpg"
image = Image.open(file)


#Debug area
print(image.format, image.size, image.mode)
print(file)
