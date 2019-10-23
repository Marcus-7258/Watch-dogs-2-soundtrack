import pygame
import random
green = (0,255,0)
red = (255, 0, 0)
blue = (0,0,255)
white = (255,255,255)
turquoise = (66,243,203)
pygame.init()
pygame.mixer.init()
screen=pygame.display.set_mode((800,600))
background=pygame.Surface(screen.get_size())
mainloop=True
pause=False
  
while mainloop:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      mainloop=False
  background.fill((0,0,0))
  background=background.convert()
  screen.blit(background,(0,0))
  pygame.draw.rect(screen, green,(150,450,100,50))
  font = pygame.font.SysFont("comicsansms", 19)

  text = font.render("Shanghaied", True, (0, 0, 0))
  screen.blit(text,(150, 460))
  mouse = pygame.mouse.get_pos()

  pressed = pygame.mouse.get_pressed()[0]
  if 150+100 > mouse[0] > 150 and 450+50 > mouse[1] > 450 and pressed:
      #pygame.mixer.music.load('WATCH DOGS 2 SONG IM A WATCH DOG #NerdOut.mp3')
      #pygame.mixer.music.load('Hudson Mohawke - Watch Dogs Theme.mp3')
      pygame.mixer.music.load('Shanghaied.mp3')
      pygame.mixer.music.play(0)
      
  pygame.draw.rect(screen, red,(550,450,100,50))
  font = pygame.font.SysFont("comicsansms", 18)
  
  text = font.render("Watch dogs", True, (0, 0, 0))
  text1 = font.render("song", True, (0, 0, 0))
  screen.blit(text,(550,450))
  screen.blit(text1,(580,470))
  mouse = pygame.mouse.get_pos()
  pressed = pygame.mouse.get_pressed()[0]
  if 550+100 > mouse[0] > 550 and 450+50 > mouse[1] > 450 and pressed:
      #pygame.mixer.music.load('Shanghaied.mp3')
      #pygame.mixer.music.load('Hudson Mohawke - Watch Dogs Theme.mp3')
      pygame.mixer.music.load('WATCH DOGS 2 SONG IM A WATCH DOG #NerdOut.mp3')
      pygame.mixer.music.play(0)
      

  pygame.draw.rect(screen, blue, (350,450,100,50))
  
  font = pygame.font.SysFont("comicsansms", 18)

  text = font.render("Watch dogs", True, (0, 0, 0))
  text1 = font.render ("2 theme", True, (0,0,0))
  screen.blit(text1,(365,470))
  screen.blit(text,(350, 450))
  mouse = pygame.mouse.get_pos()
  pressed = pygame.mouse.get_pressed()[0] 
  if 350+100 > mouse[0] > 350 and 450+50 > mouse[1] > 450 and pressed:
      #pygame.mixer.music.load('Shanghaied.mp3')
      #pygame.mixer.music.load('WATCH DOGS 2 SONG IM A WATCH DOG #NerdOut.mp3')
      pygame.mixer.music.load('Hudson Mohawke - Watch Dogs Theme.mp3')
      pygame.mixer.music.play(0)
      

  pygame.draw.rect(screen, white, (150,250,100,50))
  font = pygame.font.SysFont("comicsansms", 38)

  text = font.render("Stop", True, (255, 0, 0))


  screen.blit(text,(150, 245))
  mouse = pygame.mouse.get_pos()
  pressed = pygame.mouse.get_pressed()[0]
  if 150+100 > mouse[0] > 150 and 250+50 > mouse[1] > 250 and pressed:
     pygame.mixer.music.stop()
     pause = False


  pygame.draw.rect(screen, white, (350,250,100,50))
  font = pygame.font.SysFont("comicsansms",19)

  text = font.render("Pause/", True, (255, 0, 0))
  text1 = font.render("Unpause", True, (255, 0, 0))
  screen.blit(text,(370, 250))
  screen.blit(text1,(360, 270))
  mouse = pygame.mouse.get_pos()
  pressed = pygame.mouse.get_pressed()[0]
  if 350+100 > mouse[0] > 350 and 250+50 > mouse[1] > 250 and pressed:
    pause = not pause
    if pause:
      pygame.mixer.music.pause()
    else:
      pygame.mixer.music.unpause()
      
  pygame.draw.rect(screen, turquoise, (550,250,100,50))
  font = pygame.font.SysFont("comicsansms", 28)

  text = font.render("Shuffle", True, (0, 0, 0))


  screen.blit(text,(549, 255))
  mouse = pygame.mouse.get_pos()
  pressed = pygame.mouse.get_pressed()[0]
  if 550+100 > mouse[0] > 550 and 250+50 > mouse[1] > 250 and pressed:
    songs = ['Hudson Mohawke - Watch Dogs Theme.mp3','Shanghaied.mp3','WATCH DOGS 2 SONG IM A WATCH DOG #NerdOut.mp3']
    pygame.mixer.music.load(random.choice(songs))
    pygame.mixer.music.play(0)

  font = pygame.font.SysFont("comicsansms", 48)

  text = font.render("Watch dogs 2 soundtracks", True, (0, 100, 0))


  screen.blit(text,(100, 0))
    
  pygame.display.update()
pygame.quit()
