import pyautogui as pg
import time

pg.moveTo(954, 1054, duration=1)
pg.click()
pg.moveTo(206, 789, duration=3)
pg.click()
pg.write('my awsome commit')
pg.moveTo(252, 996, duration=1)
pg.click()
time.sleep(2)
pg.hotkey('ctrl', 'p')

while True:
    print(pg.position())
