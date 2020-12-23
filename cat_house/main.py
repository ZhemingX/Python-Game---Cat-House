import pygame
from pygame.locals import *
from sys import exit
import game_env
from cat_entity import *
import setting 
import time

scene = game_env.Scene()

#inital some parameters
fps = setting.fps
clock = pygame.time.Clock()
start_t = int(time.time())

# scene state
START = "START"
INPROGRESS = "INPROGRESS"
CHECKPRODUCE = "CHECKPRODUCE"
SHOPPROC = "SHOPPROC"
GAMEOVER = "GAMEOVER"

while True:
	if scene.state == START:
		for event in pygame.event.get():
			if event.type == QUIT:
				exit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				if scene.playicon.isOver():
					scene.state = INPROGRESS

		scene.DRAW_START()

	if scene.state == INPROGRESS:
		for event in pygame.event.get():
			if event.type == QUIT:
				exit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				if scene.cpb.isOver():
					scene.state = CHECKPRODUCE
					scene.mouse.back_normal()

				elif scene.shoptag.isOver():
					scene.state = SHOPPROC
					scene.mouse.back_normal()

				elif scene.foods_button[0].isOver():
					if scene.mouse.getState() == 0 and scene.foods_num[0] > 0:
						scene.mouse.feed_f0()
					else:
						scene.mouse.back_normal()

				elif scene.foods_button[1].isOver():
					if scene.mouse.getState() == 0 and scene.foods_num[1] > 0:
						scene.mouse.feed_f1()
					else:
						scene.mouse.back_normal()

				elif scene.foods_button[2].isOver():
					if scene.mouse.getState() == 0 and scene.foods_num[2] > 0:
						scene.mouse.feed_f2()
					else:
						scene.mouse.back_normal()

				elif scene.mouse_feather.isOver():
					if scene.mouse.getState() == 0:
						scene.mouse.play_cat()
					else:
						scene.mouse.back_normal()

				elif scene.mouse_shovel.isOver():
					if scene.mouse.getState() == 0:
						scene.mouse.kill_cat()
					else:
						scene.mouse.back_normal()

				else:
					# click cat to feed
					for spr in sorted(scene.CatGroup.sprites(), key=scene.CatGroup.by_y):
						if spr.isOver() and spr.state == "NORMAL":
							if scene.mouse.getState() == 0:
								# show basic info of choosing cat
								scene.CatGroup.reset_isshow_flag()
								spr.is_showinfo = 1
							elif scene.mouse.getState() == 1:
								# feed the cat (one cat gets affected each operation)
								spr.isFeed = 1
								spr.feed_st = int(time.time())
								if scene.mouse.getFoodDetail() == 0:
									spr.reward0 += 1
									scene.foods_num[0] -= 1
									spr.hp += 80
								elif scene.mouse.getFoodDetail() == 1:
									spr.reward1 += 1
									scene.foods_num[1] -= 1
									spr.hp += 90
								elif scene.mouse.getFoodDetail() == 2:
									spr.reward2 += 1
									scene.foods_num[2] -= 1
									spr.hp += 100
								scene.mouse.back_normal()
								break
							elif scene.mouse.getState() == 2:
								# only for playing cat
								pass
							elif scene.mouse.getState() == 3:
								# kill cat (one cat gets affected each operation)
								scene.CatGroup.remove(spr)
								break	

		scene.DRAW_UPDATE_INPROGRESS(fps, clock)

	elif scene.state == CHECKPRODUCE:
		for event in pygame.event.get():
			if event.type == QUIT:
				exit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				if scene.check_pop.cancelbutton.isOver():
					scene.state = INPROGRESS
				if scene.score >= 50:
					if scene.check_pop.ccbbutton.isOver():
						scene.state = INPROGRESS
						prod_t = int(time.time())
						scene.CatGroup.produce_cat(prod_t)
						scene.trigger_botcat(prod_t)
						scene.score -= 50

		scene.DRAW_CHECKPRODUCE(fps, clock)

	elif scene.state == SHOPPROC:
		for event in pygame.event.get():
			if event.type == QUIT:
				exit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				if scene.shop_pop.cancelbutton.isOver():
					scene.state = INPROGRESS
				elif scene.shop_pop.increase0.isOver():
					if scene.shop_pop.num0 < 10:
						scene.shop_pop.num0 += 1
				elif scene.shop_pop.increase1.isOver():
					if scene.shop_pop.num1 < 10:
						scene.shop_pop.num1 += 1
				elif scene.shop_pop.increase2.isOver():
					if scene.shop_pop.num2 < 10:
						scene.shop_pop.num2 += 1
				elif scene.shop_pop.decrease0.isOver():
					if scene.shop_pop.num0 > 0:
						scene.shop_pop.num0 -= 1
				elif scene.shop_pop.decrease1.isOver():
					if scene.shop_pop.num1 > 0:
						scene.shop_pop.num1 -= 1
				elif scene.shop_pop.decrease2.isOver():
					if scene.shop_pop.num2 > 0:
						scene.shop_pop.num2 -= 1
				elif scene.shop_pop.shopconfirm.isOver() and scene.shop_pop.shopconfirm.enable == 1:
					# add to storage and reset value in shop pop
					total_price = scene.shop_pop.total
					scene.foods_num[0] += scene.shop_pop.num0
					scene.shop_pop.num0 = 0
					scene.foods_num[1] += scene.shop_pop.num1
					scene.shop_pop.num1 = 0
					scene.foods_num[2] += scene.shop_pop.num2
					scene.shop_pop.num2 = 0
					# take money from score off
					scene.score -= total_price
					# change state
					scene.state = INPROGRESS

		scene.DRAW_SHOPPROC(fps, clock)

	#scene.draw_mouse()
	scene.mouse.draw(scene.screen)
	pygame.display.update()
