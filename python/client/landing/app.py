from flask import Flask
from getImage import *
import configparser
import sys

app = Flask(__name__)

# Matrix config
config = configparser.ConfigParser()

if len(sys.argv) == 2:    # search using album and artist

