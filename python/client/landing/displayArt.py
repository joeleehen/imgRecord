from getImage import *
import sys

if len(sys.argv) == 3:    # search using album and artist
    album = sys.argv[1]
    artist = sys.argv[2]
    imgUrl = getImageTxt(album, artist)

elif len(sys.argv) == 2:    # search using barcode
    barcode = sys.argv[1]
    imgUrl = getImageBar(barcode)