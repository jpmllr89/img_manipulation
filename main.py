import os, sys
from PIL import Image


# file = "mtns.jpg"
# newfile = "mountains.jpg"
# #The following will crop a part of the picture and change it to grayscale and put it back.
# image = Image.open(file)
# box = (100,100,400,400)
# region = image.crop(box)
# region = region.convert("L")
# #region.show()
# image.paste(region, box)
# image.show()
# #r,g,b = region.split()
# #region = Image.merge("RGB", (b,r,g))

# #Debug area
# print(image.format, image.size, image.mode)
# print(file)
# try:
# 	image.save(newfile)
# except AttributeError:
# 	print("Could not save photo")

def crop_paste_rect_grayscale(file, newfile, box):
	img = Image.open(file)
	region = img.crop(box)
	region = region.convert("L")
	return region.show()
	# img.paste(region, size)
	# try:
	# 	img.save(newfile)
	# except AttributeError:
	# 	print("Could not save photo")
	# img.show()

crop_paste_rect_grayscale("mtns.jpg", "mountains.jpg", (100, 100, 100, 100))