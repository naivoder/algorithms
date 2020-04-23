"""
this file uses the PIL module to convert an image to black and white

"""
from PIL import Image

imgFile = input("Please enter the file path to the image: ")
img = Image.open(imgFile)
img = img.convert('1')
img.save('../Pictures/result.png')
