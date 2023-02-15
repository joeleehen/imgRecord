from flask import Flask, render_template, request
import displayArt
from getImage import *

app = Flask(__name__)

@app.route("/")
def home():
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
