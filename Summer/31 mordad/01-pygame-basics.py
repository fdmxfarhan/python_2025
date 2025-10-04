import pygame

pygame.init()
screen = pygame.display.set_mode((600, 400))

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      exit()
  screen.fill((255, 255, 0))
  ###############
  
  pygame.draw.rect(screen, (0, 0, 255), (100, 100, 100, 50))
  pygame.draw.circle(screen, (0, 255, 0), (300, 100), 50)

  ###############
  pygame.display.update()