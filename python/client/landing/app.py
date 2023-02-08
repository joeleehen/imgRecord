from flask import Flask, render_template, request
import configparser
import os
import dbus

app = Flask(__name__)

dir = os.path.dirname(__file__)
filename = os.path.join(dir, "../../config/rgb_options.ini")
# Matrix config
config = configparser.ConfigParser()

sysbus = dbus.SystemBus()
systemd1 = sysbus.get_object('org.freedesktop.systemd1', '/org/freedesktop/systemd1')
manager = dbus.Interface(systemd1, 'org.freedesktop.systemd1.Manager')

@app.route("/")
def savedConfig():
    brightness = int(config['DEFAULT']['brightness'])
    width = int(config['DEFAULT']['rows'])
    height = int(config['DEFAULT']['columns'])
    power = config['DEFAULT']['power']
    refresh_rate = config['DEFAULT']['refresh_rate']
    return render_template('index.html', brightness = brightness, width = width, height = height, power = power, refresh_rate = refresh_rate)

@app.route("/brightness")
def setBrightness():
    config.set('DEFAULT', 'brightness', request.form['brightness'])
    width = int(config['DEFAULT']['rows'])
    height = int(config['DEFAULT']['columns'])
    power = config['DEFAULT']['power']
    with open(filename, 'w') as configfile:
        config.write(configfile)
    job = manager.RestartUnit('spotipi.service', 'fail')
    return render_template('index.html', brightness = request.form['brightness'], width = width, height = height, power = power)
