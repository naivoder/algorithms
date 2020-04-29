"""
need to keep your computer from falling asleep? need to keep status as "available" when you aren't near the computer?
this file moves the mouse around the screen to simulate activity.

to install pyautogui module:
`pip install pyautogui`

"""

from pyautogui import *
from time import sleep
from random import randint

while True:
  moveRel(randint(-500, 500), randint(-500, 500))
  sleep(1)
