from django.db import models


class Command(models.Model):
    class Direction(models.IntegerChoices):
        UNKNOWN = 0,
        UP = 1000,
        UPLEFT = 1010,
        UPRIGHT = 1001,
        RIGHT = 1,
        DOWNRIGHT = 101,
        DOWN = 100,
        DOWNLEFT = 110,
        LEFT = 10

    direction = models.IntegerField(
        choices=Direction.choices,
        default=Direction.UNKNOWN
    )
