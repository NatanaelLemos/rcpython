from .bot.Motor import *


class ManualControl:

    PWM = Motor()

    def move(self, direction):
        if (direction == 1010):
            #for some reason this one is not working
            print("forward")
            print("left")
            self.moveRobot(-300, -300, -2500, -2500)
        elif(direction & 1000) == 1000:
            print("forward")

            if(direction & 10) == 10:
                print("left")
                self.moveRobot(-300, -300, -2500, -2500)
            elif(direction & 1) == 1:
                print("right")
                self.moveRobot(-2500, -2500, -300, -300)
            else:
                self.moveRobot(-2000, -2000, -2000, -2000)
        elif(direction & 100) == 100:
            print("backward")

            if(direction & 10) == 10:
                print("left")
                self.moveRobot(300, 300, 2500, 2500)
            elif(direction & 1) == 1:
                print("right")
                self.moveRobot(2500, 2500, 300, 300)
            else:
                self.moveRobot(2000, 2000, 2000, 2000)
        elif(direction & 10) == 10:
            print("left")
            self.moveRobot(2000, 2000, -2000, -2000)
        elif(direction & 1) == 1:
            print("right")
            self.moveRobot(-2000, -2000, 2000, 2000)
        else:
            print("stop")
            self.moveRobot(0, 0, 0, 0)

    def moveRobot(self, frontLeft, rearLeft, frontRight, rearRight):
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
