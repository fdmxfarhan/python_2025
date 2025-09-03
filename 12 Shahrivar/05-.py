import pyautogui as pg

pg.FAILSAFE = True
pg.PAUSE = 3
pos = pg.locateOnScreen('12 Shahrivar/win.png', confidence=0.9)
pg.moveTo(pos, duration=2)
pg.click()
pg.write('github')
pg.press('enter')