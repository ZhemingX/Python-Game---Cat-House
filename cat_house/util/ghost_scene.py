import pygame
from pygame.locals import *
from sys import exit
import time

pygame.init()

bg = pygame.transform.scale(pygame.image.load("/home/xdd/文档/pyfile/cat_house/images/scene/computer.jpg"), (1400, 800))
screen = pygame.display.set_mode((1500, 1000), 0, 32)
screen_ghost = pygame.transform.scale(pygame.image.load("/home/xdd/文档/pyfile/cat_house/images/scene/screen_ghost.png"), (448, 325))
screen_game = pygame.transform.scale(pygame.image.load("/home/xdd/文档/pyfile/cat_house/images/scene/game_shot.png"), (448, 325))
ghost = pygame.transform.scale(pygame.image.load("/home/xdd/文档/pyfile/cat_house/images/scene/ghost.JPG"), (900, 1080))
curTime = int(time.time())

while True:
	for event in pygame.event.get():
			if event.type == QUIT:
				exit()

	if 10 <= int(time.time()) - curTime <= 12:
		screen.blit(bg, (50,100))
		screen.blit(screen_ghost, (529,190))

	elif int(time.time()) - curTime >= 13:
		screen.fill([0, 0, 0])
		screen.blit(ghost, (300, 0))

	else:
		screen.blit(bg, (50,100))
		screen.blit(screen_game, (529,190))
	
	pygame.display.update()

