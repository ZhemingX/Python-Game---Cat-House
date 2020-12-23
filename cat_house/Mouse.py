import pygame
import setting

mouse_icon_basic = setting.mouse_icon_basic
mouse_f0 = setting.food_mouse_images[0]
mouse_f1 = setting.food_mouse_images[1]
mouse_f2 = setting.food_mouse_images[2]
mouse_feather = setting.mouse_feather
mouse_shovel = setting.mouse_shovel

class MouseObject(object):

	def __init__(self):
		self.image = mouse_icon_basic
		self.state = 0 # 0 for normal state, 1 for feed state, 2 for play cat, 3 for kill cat

	def getState(self):
		return self.state

	def feed_f0(self):
		self.state = 1
		self.image = mouse_f0

	def feed_f1(self):
		self.state = 1
		self.image = mouse_f1

	def feed_f2(self):
		self.state = 1
		self.image = mouse_f2

	def play_cat(self):
		self.state = 2
		self.image = mouse_feather

	def kill_cat(self):
		self.state = 3
		self.image = mouse_shovel

	def back_normal(self):
		self.state = 0
		self.image = mouse_icon_basic

	def getFoodDetail(self):
		if self.image == mouse_f0:
			return 0
		if self.image == mouse_f1:
			return 1
		if self.image == mouse_f2:
			return 2

		return -1

	def draw(self, screen):
		x, y = pygame.mouse.get_pos()
		x-= self.image.get_width() / 2
		y-= self.image.get_height() / 2
		pygame.mouse.set_visible(False)
		screen.blit(self.image, (x, y))