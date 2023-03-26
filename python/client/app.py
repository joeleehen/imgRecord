from flask import Flask, render_template, request
from werkzeug.exceptions import HTTPException
from displayArt import displayArt
from getImage import *
import os
import configparser

app = Flask(__name__)

dir = os.path.dirname(__file__)
filename = os.path.join(dir, "../../config/rgb_options.ini")

config = configparser.ConfigParser()
config.read(filename)

@app.route("/")
def home():
    brightness = int(config['DEFAULT']['brightness'])
    width = int(config['DEFAULT']['width']
    height = int(config['DEFAULT']['height'])
    hardware_mapping = config[DEFAULT']['hardware_mapping']
    gpio_slowdown = int(config['DEFAULT']['gpio_slowdown'])

    return render_template("index.html")

@app.route("/textSearch", methods = ["POST", "GET"])
def textSearch():
    album = request.form["album"]
    artist = request.form["artist"]
    urlImg = getImageTxt(album, artist)
    displayArt(urlImg)

    return render_template("index.html", urlImg = urlImg)


@app.route("/barSearch", methods = ["POST", "GET"])
def barSearch():
    barcodeStr = request.form["barcodeStr"]
    urlImg = getImageBar(barcodeStr)
    displayArt(urlImg)

    return render_template("index.html", urlImg = urlImg)


if __name__ == "__main__":
    app.run()
