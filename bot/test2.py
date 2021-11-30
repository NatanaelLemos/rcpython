from Buzzer import *
from Motor import *
from ADC import *
from servo import *
from Line_Tracking import *
from Ultrasonic import *
import time
from Led import *
led = Led()


def test_Led():
    try:
        led.ledIndex(0x01, 255, 0, 0)  # Red
        led.ledIndex(0x02, 255, 125, 0)  # orange
        led.ledIndex(0x04, 255, 255, 0)  # yellow
        led.ledIndex(0x08, 0, 255, 0)  # green
        led.ledIndex(0x10, 0, 255, 255)  # cyan-blue
        led.ledIndex(0x20, 0, 0, 255)  # blue
        led.ledIndex(0x40, 128, 0, 128)  # purple
        led.ledIndex(0x80, 255, 255, 255)  # white'''
        print("The LED has been lit, the color is red orange yellow green cyan-blue blue white")
        time.sleep(3)  # wait 3s
        led.colorWipe(led.strip, Color(0, 0, 0))  # turn off the light
        print("\nEnd of program")
    except KeyboardInterrupt:
        led.colorWipe(led.strip, Color(0, 0, 0))  # turn off the light
        print("\nEnd of program")


PWM = Motor()


def test_Motor():
    try:
        PWM.setMotorModel(1000, 1000, 1000, 1000)  # Forward
        print("The car is moving forward")
        time.sleep(1)
        PWM.setMotorModel(-1000, -1000, -1000, -1000)  # Back
        print("The car is going backwards")
        time.sleep(1)
        PWM.setMotorModel(-1500, -1500, 2000, 2000)  # Left
        print("The car is turning left")
        time.sleep(1)
        PWM.setMotorModel(2000, 2000, -1500, -1500)  # Right
        print("The car is turning right")
        time.sleep(1)
        PWM.setMotorModel(0, 0, 0, 0)  # Stop
        print("\nEnd of program")
    except KeyboardInterrupt:
        PWM.setMotorModel(0, 0, 0, 0)
        print("\nEnd of program")


ultrasonic = Ultrasonic()


def test_Ultrasonic():
    try:
        while True:
            data = ultrasonic.get_distance()  # Get the value
            print("Obstacle distance is "+str(data)+"CM")
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nEnd of program")


line = Line_Tracking()


def test_Infrared():
    try:
        while True:
            if GPIO.input(line.IR01) != True and GPIO.input(line.IR02) == True and GPIO.input(line.IR03) != True:
                print('Middle')
            elif GPIO.input(line.IR01) != True and GPIO.input(line.IR02) != True and GPIO.input(line.IR03) == True:
                print('Right')
            elif GPIO.input(line.IR01) == True and GPIO.input(line.IR02) != True and GPIO.input(line.IR03) != True:
                print('Left')
    except KeyboardInterrupt:
        print("\nEnd of program")


pwm = Servo()


def test_Servo():
    try:
        while True:
            for i in range(50, 110, 1):
                pwm.setServoPwm('0', i)
                time.sleep(0.01)
            for i in range(110, 50, -1):
                pwm.setServoPwm('0', i)
                time.sleep(0.01)
            for i in range(80, 150, 1):
                pwm.setServoPwm('1', i)
                time.sleep(0.01)
            for i in range(150, 80, -1):
                pwm.setServoPwm('1', i)
                time.sleep(0.01)
    except KeyboardInterrupt:
        pwm.setServoPwm('0', 90)
        pwm.setServoPwm('1', 90)
        print("\nEnd of program")


adc = Adc()


def test_Adc():
    try:
        while True:
            Left_IDR = adc.recvADC(0)
            print("The photoresistor voltage on the left is "+str(Left_IDR)+"V")
            Right_IDR = adc.recvADC(1)
            print("The photoresistor voltage on the right is "+str(Right_IDR)+"V")
            Power = adc.recvADC(2)
            print("The battery voltage is "+str(Power*3)+"V")
            time.sleep(1)
            print('\n')
    except KeyboardInterrupt:
        print("\nEnd of program")


buzzer = Buzzer()


def test_Buzzer():
    try:
        buzzer.run('1')
        time.sleep(1)
        print("1S")
        time.sleep(1)
        print("2S")
        time.sleep(1)
        print("3S")
        buzzer.run('0')
        print("\nEnd of program")
    except KeyboardInterrupt:
        buzzer.run('0')
        print("\nEnd of program")


def test_all():
    PWM.setMotorModel(-1000, -1000, -1000, -1000)
    time.sleep(3)
    PWM.setMotorModel(-1500, -1500, 1500, 1500)
    time.sleep(3)
    PWM.setMotorModel(-1000, -1000, -1000, -1000)
    time.sleep(3)
    PWM.setMotorModel(0, 0, 0, 0)


# Main program logic follows:
if __name__ == '__main__':

    print('Program is starting ... ')
    test_all()


# 3  bus    1
#
#
# 2  camera 0

# forward       PWM.setMotorModel(-1000,-1000,-1000,-1000)

# backward      PWM.setMotorModel(1000,1000,1000,1000)

# left          PWM.setMotorModel(1500,1500,-1500,-1500)

# right         PWM.setMotorModel(-1500,-1500,1500,1500)

# stop          PWM.setMotorModel(0,0,0,0)