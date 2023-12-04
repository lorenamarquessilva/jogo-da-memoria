import sys
import random
import pygame
from pygame.locals import QUIT

pygame.init()

DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Genius')

clock = pygame.time.Clock()
FPS = 10

cores = ['r', 'b', 'y', 'g']
ordemcerta = [random.choice(cores)]
ordem = []

red = pygame.image.load('R.png')
green = pygame.image.load('G.png')
blue = pygame.image.load('B.png')
yellow = pygame.image.load('Y.png')
preto = pygame.image.load('Preto.png')
preto.set_alpha(120)
errou = pygame.image.load('errou.jpg')

posicoes = {'r' : (66, 33),
           'g' : (66, 167),
           'b' : (234, 167),
           'y' : (234, 33)}

tecla_pressionada = False
fonte = pygame.font.Font("Pixels.ttf", 15)
pontucao = 0
texto = f"pontos: {pontucao}"
surface = fonte.render(texto, True, (255, 255, 255))

def selecao():
  DISPLAYSURF.blit(preto, posicoes[ordem[i]])
  pygame.display.flip()
  pygame.time.delay(200)

  DISPLAYSURF.fill((0, 0, 0))
  DISPLAYSURF.blit(red, posicoes['r'])
  DISPLAYSURF.blit(green, posicoes['g']) 
  DISPLAYSURF.blit(blue, posicoes['b']) 
  DISPLAYSURF.blit(yellow, posicoes['y'])
  DISPLAYSURF.blit(surface, (5, 10))
  pygame.display.flip()

while True:
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()

  DISPLAYSURF.fill((0, 0, 0))
  DISPLAYSURF.blit(red, posicoes['r'])
  DISPLAYSURF.blit(green, posicoes['g']) 
  DISPLAYSURF.blit(blue, posicoes['b']) 
  DISPLAYSURF.blit(yellow, posicoes['y']) 
  DISPLAYSURF.blit(surface, (5, 10))
  pygame.display.update()
  
  tamanho = len(ordemcerta)

  for i in range(tamanho):
    pygame.time.delay(500)
    DISPLAYSURF.blit(preto, posicoes[ordemcerta[i]])
    pygame.display.flip()
    pygame.time.delay(500)

    DISPLAYSURF.fill((0, 0, 0))
    DISPLAYSURF.blit(red, posicoes['r'])
    DISPLAYSURF.blit(green, posicoes['g']) 
    DISPLAYSURF.blit(blue, posicoes['b']) 
    DISPLAYSURF.blit(yellow, posicoes['y']) 
    DISPLAYSURF.blit(surface, (5, 10))
    pygame.display.flip()
  
  i = 0
  
  while tamanho > i :
    pygame.event.pump()
    if pygame.key.get_pressed()[pygame.K_r] and not tecla_pressionada:
      ordem.append('r')
      selecao()
      tecla_pressionada = True
      i += 1
      
    elif pygame.key.get_pressed()[pygame.K_g] and not tecla_pressionada:
      ordem.append('g')
      selecao()
      tecla_pressionada = True
      i += 1
    
    elif pygame.key.get_pressed()[pygame.K_b] and not tecla_pressionada:
      ordem.append('b')
      selecao()
      tecla_pressionada = True
      i += 1
    
    elif pygame.key.get_pressed()[pygame.K_y] and not tecla_pressionada:
      ordem.append('y')
      selecao()
      tecla_pressionada = True
      i += 1
    
    if not pygame.key.get_pressed()[pygame.K_r] and not pygame.key.get_pressed()[pygame.K_g] and not pygame.key.get_pressed()[pygame.K_b] and not pygame.key.get_pressed()[pygame.K_y]:
      tecla_pressionada = False

  for i in range(tamanho):
    if ordem[i] != ordemcerta[i]:
      DISPLAYSURF.blit(errou, (0,0))
      pygame.display.flip()
      pygame.time.delay(1000)
      pygame.quit()
      sys.exit()

  pontucao = tamanho
  texto = f"pontos: {pontucao}"
  surface = fonte.render(texto, True, (255, 255, 255))

  ordemcerta.append(random.choice(cores))
  ordem.clear()
      
  clock.tick(FPS)
