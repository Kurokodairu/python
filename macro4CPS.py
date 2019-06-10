import pyautogui as a
import time
import keyboard

a.PAUSE = 0.25

print("--- MOUSE CURSON POSITION ---")

try:
    while True:
        x, y = a.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)
        
        try:
            if(keyboard.is_pressed('q')):
                a.click()
                pass
            else:
                pass
        except:
            pass


except KeyboardInterrupt:
    print('\n Closing...')

print("ok")