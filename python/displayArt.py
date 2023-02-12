from getImage import *
import sys
import os
from PIL import Image
import configparser
from rgbmatrix import RGBMatrix, RGBMatrixOptions

if len(sys.argv) == 3:    # search using album and artist
    album = sys.argv[1]
    artist = sys.argv[2]
    imgUrl = getImageTxt(album, artist)

elif len(sys.argv) == 2:    # search using barcode
    barcode = sys.argv[1]
    imgUrl = getImageBar(barcode)

dir = os.path.dirname(__file__)
filename = os.path.join(dir, "../config/rgb_options.ini")
config = configparser.ConfigParser()
config.read(filename)

options = RGBMatrixOptions()
options.rows = int(config['DEFAULT']['rows'])
options.cols = int(config['DEFAULT']['columns'])
options.chain_length = int(config['DEFAULT']['chain_length'])
options.parallel = int(config['DEFAULT']['parallel'])
options.hardware_mapping = config['DEFAULT']['hardware_mapping']
options.gpio_slowdown = int(config['DEFAULT']['gpio_slowdown'])
options.brightness = int(config['DEFAULT']['brightness'])
options.limit_refresh_rate_hz = int(config['DEFAULT']['refresh_rate'])

matrix = RGBMatrix(options = options)