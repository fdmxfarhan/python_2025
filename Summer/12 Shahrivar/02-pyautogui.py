import pyautogui as pg

# حرکت ماوس به مختصات 900 و 500
pg.moveTo(900, 500, duration=1)
# کلیک کردن و حرکت کردن
pg.dragTo(900, 100, duration=1)
# کلیک کردن
pg.click(400, 1060)
# تایپ کردن
pg.write('salam')

