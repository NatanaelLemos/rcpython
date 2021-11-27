from flask import Flask, render_template, request, jsonify
from Motor import *
from Buzzer import *
from Led import *

app = Flask(__name__)
PWM = Motor()
buzzer = Buzzer()
led = Led()


@app.route("/", methods=["GET"])
def hello_world():
    return render_template("index.html")


@app.route("/", methods=["POST"])
def post():
    if isHornCommand():
        horn()
    else:
        direction = getDirection()

        if (direction & 1000) == 1000:
            print("forward")
            moveRobot(-2000, -2000, -2000, -2000)
        elif (direction & 100) == 100:
            print("backward")
            moveRobot(2000, 2000, 2000, 2000)
        elif (direction & 10) == 10:
            print("left")
            moveRobot(2000, 2000, -2000, -2000)
        elif (direction & 1) == 1:
            print("right")
            moveRobot(-2000, -2000, 2000, 2000)
        else:
            print("stop")
            moveRobot(0, 0, 0, 0)

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


def moveRobot(frontLeft, rearLeft, frontRight, rearRight):
    PWM.setMotorModel(frontLeft, rearLeft, frontRight, rearRight)

    # 3  bus    1
    #
    #
    # 2  camera 0

    # forward       PWM.setMotorModel(-1000,-1000,-1000,-1000)

    # backward      PWM.setMotorModel(1000,1000,1000,1000)

    # left          PWM.setMotorModel(1500,1500,-1500,-1500)

    # right         PWM.setMotorModel(-1500,-1500,1500,1500)

    # stop          PWM.setMotorModel(0,0,0,0)

    # 1000 = forward
    # 100 = backward
    # 10 = left
    # 1 = right
