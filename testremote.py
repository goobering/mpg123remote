#!/usr/bin/env python3

import subprocess
import time
import mpg123wrapper
import os

# Get fifo path from mpg123wrapper
fifo = mpg123wrapper.fifo

# Create an instance of mpg123 in remote/fifo mode
p = subprocess.Popen(["mpg123", "-R", "--fifo", fifo])

# Load and play a single file
mpg123wrapper.load('/home/pi/Music/1.mp3')

# Let it run for 5 seconds
time.sleep(5)

# Jump to 120 seconds
mpg123wrapper.jump('120s')

# Let it play for 3 seconds
time.sleep(3)

# Pause playback
mpg123wrapper.pause()

# Wait 3 seconds
time.sleep(3)

# Unpause/continue playing
mpg123wrapper.pause()

# Let it play for 3 seconds
time.sleep(3)

# Stop playback
mpg123wrapper.stop()

# Quit mpg123
mpg123wrapper.quit()
