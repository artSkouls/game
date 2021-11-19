import time
import os
import pynput

ballX = 7
ballY = 7
width = 30
height = 10

def draw():
    y = 0
    while y < height:
        x = 0
        result = ""
        while x < width:
            if x == round(ballX) and y == round(ballY):
                result += 'o'
            else:
                result += " "
            x += 1

        print(result)
        y += 1






while True:
    os.system('clear')
    draw()
    time.sleep(0.1)