import pygame
from pygame.locals import *
import setting
import Button
import cat_entity 
import time
import CheckPop
import gameFont
import Mouse
import ShopPop


caption = setting.caption
screen_size = setting.screen_size
major_bg = setting.major_bg
# wall setting
wall_x_bg = setting.wall_x_bg
wall_y_bg = setting.wall_y_bg
wall_x_size = setting.wall_x_size
wall_y_size = setting.wall_y_size
# bot floor setting
botfloor_bg = setting.botfloor_bg
botfloor_size = setting.botfloor_size
# bot cat setting
botcat_bg = setting.botcat_bg
botcat_shine_bg = setting.botcat_shine_bg
botcat_size = setting.botcat_size


# scene state
START = "START"
INPROGRESS = "INPROGRESS"
CHECKPRODUCE = "CHECKPRODUCE"
SHOPPROC = "SHOPPROC"
GAMEOVER = "GAMEOVER"

class Scene:
	"""background and mouse render"""
	def __init__(self):
		# initial pygame module for further use
		pygame.init()
		# scene states
		self.state = START

		# start scene element
		self.startbg = setting.startbg
		self.playicon = Button.PlayButton((750, 200))
		self.decwall = setting.decwall
		self.decpole = pygame.transform.scale(pygame.image.load(wall_y_bg), (50, 200))
		# initial screen and some static background
		self.screen = pygame.display.set_mode(screen_size, 0, 32)
		pygame.display.set_caption(caption)
		
		self.mouse = Mouse.MouseObject()
		self.major_bg = pygame.transform.scale(pygame.image.load(major_bg), screen_size)
		self.wall_x = pygame.transform.scale(pygame.image.load(wall_x_bg), wall_x_size)
		self.wall_y = pygame.transform.scale(pygame.image.load(wall_y_bg), wall_y_size)
		self.botfloor = pygame.transform.scale(pygame.image.load(botfloor_bg), botfloor_size)
		self.userpopbg = setting.userpopbg_image
		self.frame1bg = setting.frame1_image
		self.shoptag = Button.ShopButton()
		self.frame2bg = setting.frame2_image
		self.userfood = setting.food_images
		self.storage_disp = gameFont.storage_disp()
		self.cat_info_disp = gameFont.cat_info_disp()

		# set bot cat
		self.botcat = pygame.transform.scale(pygame.image.load(botcat_bg), botcat_size)
		self.botcat_shine = pygame.transform.scale(pygame.image.load(botcat_shine_bg), botcat_size)
		self.shine_trigger = 0
		self.last_shine_trigger_time = 0

		# set score display field
		self.score = 200
		self.score_disp = gameFont.score_disp("SCORE: " + str(self.score))

		# set food display field
		self.foods_num = [0, 0, 0]
		self.foods_disp_pos = ((180, 210), (180, 310), (180, 415))
		self.foods_num_disp = gameFont.food_numbers_disp(["X " + str(i) for i in self.foods_num], self.foods_disp_pos)
		self.foods_button = [
		Button.FoodButton(self.userfood[0], (120, 230)),
		Button.FoodButton(self.userfood[1], (120, 330)),
		Button.FoodButton(self.userfood[2], (120, 432))
		]

		# set cat number display field
		self.cat_num = 0
		self.cat_num_disp = gameFont.cat_num_disp(self.cat_num)

		# set cat-produce button
		self.cpb = Button.CatProduceButton()
		self.if_produce_refuse = 0

		# set cat group
		self.CatGroup = cat_entity.CatSpriteGroup()

		# CHECKPROGRESS sub window
		self.check_pop = CheckPop.CheckWindowPop()

		# SHOPPROC sub window
		self.shop_pop = ShopPop.ShopWindowPop()

		# play cat and kill cat icon
		self.mouse_feather = Button.FeatherButton((400, 150))
		self.mouse_shovel = Button.ShovelButton((460, 150))

		print("Scene inital!")

	def DRAW_START(self):
		self.draw_start()

	def DRAW_UPDATE_INPROGRESS(self, fps, clock):
		# draw background
		self.draw_background()
		# draw button
		self.draw_button()
		# draw and update catgroup
		self.draw_and_update_catgroup(fps, clock, True, self.mouse.getState())

	def DRAW_CHECKPRODUCE(self, fps, clock):
		# draw background
		self.draw_background()
		# draw button
		self.draw_button()
		# draw and update catgroup
		self.draw_and_update_catgroup(fps, clock, False, self.mouse.getState())
		# draw check pop
		self.draw_check_pop()

	def DRAW_SHOPPROC(self, fps, clock):
		# draw background
		self.draw_background()
		# draw button
		self.draw_button()
		# draw and update catgroup
		self.draw_and_update_catgroup(fps, clock, False, self.mouse.getState())
		# draw shop pop
		self.draw_shop_pop()

	def draw_start(self):
		self.screen.blit(self.startbg, (400,0))
		self.screen.blit(self.decwall, (0, 0))
		self.screen.blit(self.decwall, (1100, 0))
		for i in range(0,5):
			# draw left, right wall
			self.screen.blit(self.decpole, (350, 200 * i))
			self.screen.blit(self.decpole, (1100, 200 * i))

		self.playicon.draw(self.screen)

	def draw_background(self):
		# draw floor
		self.screen.blit(self.major_bg, (0,0))
		# draw user pop bg
		self.screen.blit(self.userpopbg, (0, 0))
		# draw wall and botfloor
		for i in range(0,5):
			# draw left, right wall
			self.screen.blit(self.wall_y, (0.2*screen_size[0], wall_x_size[1]+i*wall_y_size[1]))
			self.screen.blit(self.wall_y, (screen_size[0]-wall_y_size[0], wall_x_size[1]+i*wall_y_size[1]))
		for i in range(0,5):
			# top wall
			self.screen.blit(self.wall_x, (0.2*screen_size[0]+i*wall_x_size[0], 0))
			# bot floor
			self.screen.blit(self.botfloor, (0.2*screen_size[0]+i*wall_x_size[0], 0))
			self.screen.blit(self.botfloor, (0.2*screen_size[0]+i*wall_x_size[0]+botfloor_size[0], 0))
			# bottom wall
			self.screen.blit(self.wall_x, (0.2*screen_size[0]+i*wall_x_size[0], screen_size[1]-wall_x_size[1]))
			# bot floor
			self.screen.blit(self.botfloor, (0.2*screen_size[0]+i*wall_x_size[0], screen_size[1]-botfloor_size[1]))
			self.screen.blit(self.botfloor, (0.2*screen_size[0]+i*wall_x_size[0]+botfloor_size[0], screen_size[1]-botfloor_size[1]))


		self.draw_and_update_botcat()

		# draw score board
		self.score_disp = gameFont.score_disp("SCORE: " + str(self.score))
		self.score_disp.draw(self.screen)

		# draw user pop
		self.screen.blit(self.frame1bg, (0, 0))
		self.shoptag.draw(self.screen)
		self.screen.blit(self.frame2bg, (0, 118))
		self.storage_disp.draw(self.screen)
		self.screen.blit(self.frame2bg, (0, 540))
		self.cat_info_disp.draw(self.screen)

		# draw user food and food number
		for i in range(0, 3):
			self.foods_button[i].draw(self.screen)
		self.foods_num_disp = gameFont.food_numbers_disp(["X " + str(i) for i in self.foods_num], self.foods_disp_pos)
		for mem in self.foods_num_disp:
			mem.draw(self.screen)

		# draw cat num display
		self.cat_num = self.CatGroup.count_cat_num()
		self.cat_num_disp = gameFont.cat_num_disp(self.cat_num)
		self.cat_num_disp.draw(self.screen)

		# draw feather and stovel button
		self.mouse_feather.draw(self.screen)
		self.mouse_shovel.draw(self.screen)

	def trigger_botcat(self, time):
		self.shine_trigger = 1
		self.last_shine_trigger_time = time

	def draw_and_update_botcat(self):
		if(self.shine_trigger == 1):
			self.draw_botcat(self.botcat_shine)
		else:
			self.draw_botcat(self.botcat)

		curr_t = time.time()
		if(curr_t - self.last_shine_trigger_time >= 1):
			self.shine_trigger = 0

	def draw_botcat(self, surface):
		# draw bot cat
		self.screen.blit(surface, (0.2*screen_size[0], 0))
		self.screen.blit(surface, (screen_size[0]-botcat_size[0], 0))
		self.screen.blit(surface, (0.2*screen_size[0], screen_size[1]-botcat_size[1]))
		self.screen.blit(surface, (screen_size[0]-botcat_size[0], screen_size[1]-botcat_size[1]))
			


	def draw_and_update_catgroup(self, fps, clock, if_purchase, mouse_state):
		self.CatGroup.draw(self.screen)
		time_passed_seconds = clock.tick(fps) / 1000.0
		self.CatGroup.update(time_passed_seconds, int(time.time()), if_purchase, mouse_state)
		# add scores produces by cats
		self.score += self.CatGroup.count_value()

	def draw_button(self):
		#cat produce button
		self.cpb.draw(self.screen)

	def draw_check_pop(self):
		self.check_pop.draw(self.screen, self.score)
	
	def draw_shop_pop(self):
		self.shop_pop.draw(self.screen, self.score)

	def playground_info(self):
		# return the boundary of the playground for limiting the space of cats
		# return a tuple (topleft coordinate, bottomright coordinate)
		topleft = (int(0.2*screen_size[0]) + wall_y_size[0], botfloor_size[1] + 10)
		bottomright = (screen_size[0] - botfloor_size[0], screen_size[1] - botfloor_size[1])
		return (topleft, bottomright)