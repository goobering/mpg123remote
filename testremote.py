#!/usr/bin/env python3

import subprocess
import time
import mpg123wrapper
import os

fifo = mpg123wrapper.fifo
print(fifo)

#from subprocess import call
p = subprocess.Popen(["mpg123", "-R", "--fifo", fifo, "--buffer", "1024"])

print("sleep 5")
time.sleep(5)
print("load")
mpg123wrapper.load('/home/pi/Music/1.mp3')
print("sleep 5")
time.sleep(5)
print("jump 30")
mpg123wrapper.jump('120s')
print("sleep 3")
time.sleep(3)
print("pause")
mpg123wrapper.pause()
print("sleep 3")
time.sleep(3)
print("pause")
mpg123wrapper.pause()
print("sleep 3")
time.sleep(3)
print("volume 50")
mpg123wrapper.volume(50)
print("sleep 3")
time.sleep(3)
print("volume 100")
mpg123wrapper.volume(100)
print("sleep 3")
time.sleep(3)
print("stop")
mpg123wrapper.stop()
print("sleep 3")
time.sleep(3)

print(mpg123wrapper.fifo)
print(os.path.isfile(mpg123wrapper.fifo))

mpg123wrapper.quit()



#mpg123wrapper.closefile()
#p.kill()





