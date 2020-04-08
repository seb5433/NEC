from pynput.keyboard import Key ,Controller
import subprocess
import time
subprocess.Popen(["notepad","ticket1.txt"])
keyboard = Controller()
time.sleep(0.1)
with keyboard.pressed(Key.ctrl):
    keyboard.press('p')
    keyboard.release('p')
time.sleep(0.5)
with keyboard.pressed(Key.enter):
    print ("hpña")