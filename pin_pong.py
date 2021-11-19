import time
import os
import pynput

ballX = 7
ballY = 7
ballDirX = 0.2
ballDirY = 0.4
width = 30
height = 10
racket1Y = 2
racket2Y = 1
lengthRacket = 3
def draw():
    y = 0
    while y < height:
        x = 0
        result = ""
        while x < width:
            if x == round(ballX) and y == round(ballY):
                result += 'o'
            elif (y >= racket1Y  and y <= racket1Y + lengthRacket) and x == 0:
                result += "|"
            elif (y >= racket2Y  and y <= racket2Y + lengthRacket) and x == width - 1:
                result += "|"
            else:
                result += " "
            x += 1

        print(result)
        y += 1


def press_instruction(key):
    global racket1Y, racket2Y
    if key == pynput.keyboard.KeyCode.from_char('w'):
        racket1Y -= 1
    elif key == pynput.keyboard.KeyCode.from_char('s'):
        racket1Y += 1
    if racket1Y >= height - lengthRacket:
        racket1Y = height - 1 - lengthRacket
    if racket1Y < 0:
        racket1Y = 0

    if key == pynput.keyboard.Key.up:
        racket2Y -= 1
    elif key == pynput.keyboard.Key.down:
        racket2Y += 1
    if racket2Y >= height - lengthRacket:
        racket2Y = height - 1 - lengthRacket
    if racket2Y < 0:
        racket2Y = 0


def release_instruction(key):
    print('Release', key)


pynput.keyboard.Listener(
    on_press=press_instruction,
    on_release=release_instruction
).start()

while True:
    ballX += ballDirX
    ballY += ballDirY
    if round(ballY) == height - 1:
        ballDirY *= -1
    if round(ballY) == 0:
        ballDirY *= -1
    if round(ballX) == width - 1:
        if round(ballY) >= racket2Y and round(ballY) < racket2Y + lengthRacket:
            ballDirX *= -1
        else:
            quit('Player 2 lose')
    if round(ballX) == 0:
        if round(ballY) >= racket1Y and round(ballY) < racket1Y + lengthRacket:
            ballDirX *= -1
        else:
            quit('Player 1 lose')
    os.system('clear')
    draw()
    time.sleep(0.1)
