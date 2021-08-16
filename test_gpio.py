
from gpiozero import LED       
import time
import os

close = Button(22)
open = Button(27)

close.wait_for_press()
print("close is pressed")

