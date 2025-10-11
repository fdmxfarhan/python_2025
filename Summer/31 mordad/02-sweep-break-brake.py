import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))

x = 400
y = 300
a = 0
b = 0
xr = 350
yr = 550
breaks = []
row = [True] * 7

print(breaks)
print(row)
while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      exit()
  screen.fill((255, 255, 0))
  ###############
  
  pygame.draw.rect(screen, (0, 0, 255), (xr, yr, 100, 20))
  pygame.draw.circle(screen, (0, 0, 255), (x, y), 10)
  for j in range(10, 200, 50):
    for i in range(10, 700, 110):
      pygame.draw.rect(screen, (200, 0, 100), (i, j, 100, 40))
  x = x + a
  y = y + b
  if y < 0: b = -b
  if x > 800 or x < 0: a = -a
  if y > 600: 
    print('game over')
    x = 400
    y = 300
    a = 0
    b = 0

  keys = pygame.key.get_pressed()
  if keys[pygame.K_SPACE]:
    a = 0.5
    b = 0.5
  if keys[pygame.K_LEFT] and xr > 0:
    xr = xr - 0.5
  if keys[pygame.K_RIGHT] and xr < 700:
    xr = xr + 0.5

  if x > xr and x < xr+100 and y > yr - 10:
    b = -b
  
  ###############
  pygame.display.update()