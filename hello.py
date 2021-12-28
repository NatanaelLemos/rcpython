from flask import Flask, render_template, request
from .bot.Buzzer import *
from .bot.Led import *
from .manualControl import *

app = Flask(__name__)
buzzer = Buzzer()
led = Led()
manualControl = ManualControl()


@app.route("/", methods=["GET"])
def hello_world():
    return render_template("index.html")


@app.route("/", methods=["POST"])
def post():
    if isHornCommand():
        horn()
    else:
        direction = getDirection()
        manualControl.move(direction)

    return "ok"


def isHornCommand():
    content = request.json
    return ("horn" in content) and (content["horn"] == 1)


def horn():
    led.colorWipe(led.strip, Color(255, 255, 255))
    time.sleep(2)
    led.colorWipe(led.strip, Color(0, 0, 0))


def getDirection():
    content = request.json
    return int(content["direction"])
