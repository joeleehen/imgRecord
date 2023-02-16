from getImage import *
import sys
from io import BytesIO
from PIL import Image
import requests
from rgbmatrix import RGBMatrix, RGBMatrixOptions

def displayArt(url):
    # matrix configuration
    options = RGBMatrixOptions()    # amazing brother
    options.rows = 32
    options.cols = 32
    options.chain_length = 1
    options.parallel = 1
    options.hardware_mapping = 'adafruit-hat'
    options.gpio_slowdown = 4

    matrix = RGBMatrix(options = options)    # pop off (only on occasion) brother
    headers = {
        "User-Agent": "imgRecord/5.0",
    }
    response = requests.get(url, headers=headers)    # get binary for image 

    # write image to file
    temp = open("temp.jpg", "wb")
    temp.write(response.content)
    temp.close()
    img = Image.open("temp.jpg")

    # image to matrix
    img.thumbnail((matrix.width, matrix.height), Image.ANTIALIAS)
    matrix.SetImage(img.convert("RGB"))

    return
