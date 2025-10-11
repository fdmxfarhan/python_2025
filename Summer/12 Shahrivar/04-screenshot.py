import pyautogui as pg
import keyboard

n = 0
while True:
    if keyboard.is_pressed('x'):
        screenshot = pg.screenshot()
        screenshot.save(f'myscreenshot{n}.png')
        n = n + 1