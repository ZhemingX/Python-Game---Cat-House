import pygame
from pygame.locals import *
import setting
from util.Vector2 import *
import random
import time
import gameFont
import CatInfoDisp

basecat_images = setting.basecat_images
browncat_images = setting.browncat_images
ywcat_images = setting.ywcat_images
badcat_images = setting.badcat_images
blackcat_images = setting.blackcat_images
bullcat_images = setting.bullcat_images
supercat_images = setting.supercat_images
pbcat_images = setting.pbcat_images
cat_convert_image = setting.cat_convert_image

# cat revolution category #-------cat attribute [image, value, consume, name]
cat_category = (
	[(basecat_images, 5, 5, "basecat")], #level 0
	[(browncat_images, 8, 6, "browncat"), (ywcat_images, 8, 6, "ywcat")], #level 1
	[(blackcat_images, 10, 8, "blackcat"), (pbcat_images, 12, 8, "pbcat"), (bullcat_images, 15, 10, "bullcat"), (badcat_images, 2, 2, "badcat")], #level 2
	[(supercat_images, 25, 12, "supercat")] #level 3
)

deadcat_image = setting.deadcat_image
ground_info = setting.ground_info

# cat state
PRODUCE = "PRODUCE"
NORMAL  = "NORMAL"
DEAD    = "DEAD"

class CatSprite(pygame.sprite.Sprite):
	"""cat entity"""
	def __init__(self, crtTime, pos):
		# super class intial
		super().__init__()
		"""cat major settings"""
		# cat attributes
		self.hp = 300
		self.level = 0
		self.images = cat_category[0][0][0]
		self.image = self.images[0]
		self.value = cat_category[0][0][1]
		self.consume = cat_category[0][0][2]
		self.name = cat_category[0][0][3]
		# number of rewards get and feed flag
		self.reward0 = 0
		self.reward1 = 0
		self.reward2 = 0
		self.isFeed = 0
		self.feed_st = 0.0
		# speed (speed for each cat is among 30, 40, 50, 60, 70)
		self.speed = random.randint(0,4) * 10 + 20
		self.g_accelerate = 9.8

		# frame, for switching the images of the cat
		self.frame = 0
		self.move_cycle = 4

		# ground info: space for cat move ((350, 130),(1380,880))
		self.ground_info = ground_info

		# cat position and rect
		self.initpos = pos
		self.position = Vector2(self.initpos[0], self.ground_info[0][1])
		self.heading = Vector2()
		self.destination = Vector2()
		self.rect = self.image.get_rect(topleft=(self.position.x, self.position.y))

		# create time
		self.crtTime = crtTime
		
		# cat state {PRODUCE, NORMAL, DEAD}
		self.state = PRODUCE

		"""other attribute"""

		# timestamp of starting dead state 
		self.dead_start = 0
		# timestamp of last position change time
		self.last_pos_change_time = 0
		# cat value relative variables(cat contribution)
		self.last_poduce_value_time = self.crtTime
		self.if_produce_value = 0
		self.if_show_msg = 0
		# variable for monitoring revolution
		self.last_revolution_time = self.crtTime
		self.cat_index = 0
		self.is_convert = 0 # flag for showing figure of converting
		# is show info tag
		self.is_showinfo = 0
		# is show anon text flag
		self.last_shown_anon_t = self.crtTime
		self.is_showanon = 0
		self.textid = 0
		# hp decrease flag
		self.last_decrease_hp_t = self.crtTime

	def update(self, *args):
		"""main update function"""
		# args[0] refers to time_pass_seconds
		# args[1] refers to current time
		# args[2] decide whether cat should purchase the mouse
		# arg[3] refers to mouse state, choosing whether to purchase mouse
		if self.state == PRODUCE:
			self.produce_action(args[0])
		if self.state == NORMAL:
			self.normal_action(args[0], args[1], args[2], args[3])
		if self.state == DEAD:
			self.dead_action(args[1])


	def produce_action(self, time_pass):
		# simulate gravity fall when producing a new cat
		destination = Vector2(self.initpos[0], self.initpos[1])
		v2d = Vector2.from_points(self.position, destination)
		dist = v2d.get_magnitude()
		v2d.normalize()
		# self.position.y >= destination.y
		# dist <= 30, cat stop collision and switch to NORMAL state
		if dist <= 30 and float(self.speed) <= 0.2:
			self.state = NORMAL
			self.speed = self.speed = random.randint(0,4) * 10 + 30
		else:
			if dist <= 30:
				self.speed = -self.speed * 0.8
			self.speed += self.g_accelerate
			self.heading = v2d.mul(self.speed)
			self.position = self.position.add(self.heading.mul(time_pass))
			self.rect = self.image.get_rect(topleft=(self.position.x, self.position.y))


	def normal_action(self, time_pass, curTime, if_purchase, mouse_state):
		"""cat action when state is NORMAL"""
		#-----------cat hp decrease regularly----------------#
		if curTime - self.last_decrease_hp_t >= 60:
			self.hp -= self.consume
			self.last_decrease_hp_t = curTime
		if self.hp <= 0:
			self.state = DEAD
			return
		#----cat level up function-----------------#
		self.cat_revolution(curTime) 
		if self.is_convert:
			self.image = cat_convert_image
			return
		#----update isFeed value after action------#
		if curTime - self.feed_st >= 2:
			self.isFeed = 0
		#----update if-produce-value regularly-----#
		if curTime - self.last_poduce_value_time >= 30:
			self.if_produce_value = 1
			self.if_show_msg = 1
			self.last_poduce_value_time = curTime
		else:
			self.if_produce_value = 0

		if curTime - self.last_poduce_value_time > 1:
			self.if_show_msg = 0
		
		#----update is_showanon flag regularly-----#
		if curTime - self.last_shown_anon_t >= 20:
			self.last_shown_anon_t = curTime
			self.textid = random.randint(0, len(CatInfoDisp.anonymous_texts) - 1)
			chance = random.randint(0,1) # thus guarantee half of the cat will display anonmyous texts
			if not (self.isFeed and chance):
				self.is_showanon = 1

		if curTime - self.last_shown_anon_t > 1:
			self.is_showanon = 0
		
		#----update destination regularly----------#
		mouse_pos = pygame.mouse.get_pos()
		cond1 = (mouse_pos[0] >= self.ground_info[0][0] and mouse_pos[0] <= self.ground_info[1][0])
		cond2 = (mouse_pos[1] >= self.ground_info[0][1] and mouse_pos[1] <= self.ground_info[1][1])
		if not ((cond1 and cond2) and if_purchase and mouse_state == 2):
			# provide a random position regularly (every 8 seconds)
			if self.last_pos_change_time == 0 or curTime - self.last_pos_change_time >= 8:
				newpos = self.random_position()
				self.last_pos_change_time = curTime
				self.destination = Vector2(*newpos).sub((Vector2(*self.image.get_size()).div(2)))
		else:
			self.destination = Vector2(*mouse_pos).sub((Vector2(*self.image.get_size()).div(2)))

		
		vector2mouse = Vector2.from_points(self.position, self.destination)
		dist = vector2mouse.get_magnitude()
		vector2mouse.normalize()

		# dist <= 100, cat stand still
		if dist <= 100:
			# update image
			if vector2mouse.x >= 0:
				self.image = self.images[self.move_cycle]
			else:
				self.image = self.images[0]

		else:
			# update image
			if self.frame >= setting.fps / 2 - 1:
				self.frame = 0
			if vector2mouse.x >= 0:
				# cats finish two whole cycles of movements per second, since fps = 80, switch to another image every 10 frames.
				self.image = self.images[int(self.frame / 10) + self.move_cycle]
			else:
				self.image = self.images[int(self.frame / 10)]

			# update position
			self.heading = vector2mouse.mul(self.speed)
			self.position = self.position.add(self.heading.mul(time_pass))
			self.rect = self.image.get_rect(topleft=(self.position.x, self.position.y))
			self.frame += 1

	def dead_action(self, curTime):
		if not self.alive():
			pass
		else:
			self.image = deadcat_image
			if self.dead_start == 0:
				self.dead_start = curTime
			else:
				if curTime - self.dead_start >= 3:
					# remove cat from group
					self.kill()

	def random_position(self):
		"""provide a random position for cat to go"""
		x_range = (self.ground_info[0][0], self.ground_info[1][0])
		y_range = (self.ground_info[0][1], self.ground_info[1][1])
		newpos = (random.randint(x_range[0], x_range[1]), random.randint(y_range[0], y_range[1]))

		return newpos

	def cat_revolution(self, curTime):
		if self.hp >= 20:
			if self.level == 0:
				if curTime - self.last_revolution_time >= 120:
					self.last_revolution_time = curTime
					# add conditions of revolution here
					if self.reward0 != 0 or self.reward1 != 0 or self.reward2 != 0:
						self.level = 1
						self.is_convert = 1
						self.cat_index = random.randint(0,1)

			elif self.level == 1:
				if curTime - self.last_revolution_time <= 1:
					self.is_convert = 1
				elif curTime - self.last_revolution_time >= 180:
					self.last_revolution_time = curTime
					# condition
					if self.reward0 + self.reward1 + self.reward2 >= 4:
						self.level = 2
						self.cat_index = self.level1_up_condition()
				else:
					self.is_convert = 0
					newcat = cat_category[1][self.cat_index]
					self.images = newcat[0]
					self.image  = self.images[0]
					self.value  = newcat[1]
					self.consume = newcat[2]
					self.name   = newcat[3]

			elif self.level == 2:
				if curTime - self.last_revolution_time <= 1:
					self.is_convert = 1
				elif curTime - self.last_revolution_time >= 240:
					self.last_revolution_time = curTime
					if self.reward0 >=6 and self.reward1 >=6 and self.reward2 >= 6:
						self.level = 3
						self.cat_index = 0
				else:
					self.is_convert = 0
					newcat = cat_category[2][self.cat_index]
					self.images = newcat[0]
					self.image  = self.images[0]
					self.value  = newcat[1]
					self.consume = newcat[2]
					self.name   = newcat[3]

			elif self.level == 3:
				if curTime - self.last_revolution_time <= 1:
					self.is_convert = 1
				else:
					self.is_convert = 0
					newcat = cat_category[3][self.cat_index]
					self.images = newcat[0]
					self.image  = self.images[0]
					self.value  = newcat[1]
					self.consume = newcat[2]
					self.name   = newcat[3]

	def level1_up_condition(self):
		newcid = 0
		if 0 < self.reward0 <= 2 and 0 < self.reward1 <= 2 and 0 < self.reward2 <= 2:
			newcid = 0 #blackcat
		elif self.reward1 >= 4:
			newcid = 2 #bullcat
		else:
			newcid = 1 #pbcat

		nonce = random.randint(0,100)
		if nonce >= 60:
			newcid = 3 #badcat with probablity of 0.4

		return newcid

	def isOver(self):
		# check whether the mouse is on the cat entity
		mx, my = pygame.mouse.get_pos()
		ltx, lty = self.position.x, self.position.y
		bw, bh = self.image.get_size()

		in_x = ltx < mx < ltx + bw
		in_y = lty < my < lty + bh

		return in_x and in_y

class CatSpriteGroup(pygame.sprite.Group):
	"""cat group entity"""
	def __init__(self):
		super().__init__()
		self.cat_born_space = setting.cat_born_space
		self.cat_msg_cloud = setting.msg_cloud_image
		self.normal_msg_cloud = setting.normal_msg_cloud_image
		self.catinfo_bg = setting.catinfo_bg
		self.food_icon_images = [pygame.transform.scale(setting.food_mouse_images[0], (40, 40)), pygame.transform.scale(setting.food_mouse_images[1], (40, 40)), pygame.transform.scale(setting.food_mouse_images[2], (35, 35))]

	# blit according to posy
	def by_y(self, spr):
		return spr.position.y

	def count_value(self):
		"""count the total value produced by cats each unit time"""
		total = 0
		for spr in self.sprites():
			if spr.if_produce_value == 1:
				total += spr.value
				spr.if_produce_value = 0
		return total

	def count_cat_num(self):
		"""count the total number of cats currently"""
		return len(self.sprites())

	def reset_isshow_flag(self):
		for spr in self.sprites():
			spr.is_showinfo = 0

	def produce_cat(self, time):
		bornplace = (random.randint(*self.cat_born_space[0]), random.randint(*self.cat_born_space[1]))
		newcat = CatSprite(time, bornplace)
		self.add(newcat)

	def draw(self, surface):
		sprites = self.sprites()
		surface_blit = surface.blit
		for spr in sorted(sprites, key=self.by_y):
			self.spritedict[spr] = surface_blit(spr.image, spr.rect)
			if spr.if_show_msg:
				# if cat produce value, show the produce msg cloud
				self.draw_msg_cloud(spr, surface)

			self.draw_normal_msg_cloud(spr, surface)

			if spr.is_showinfo and spr.state == NORMAL:
				# when cat is clicked, show cat info
				self.draw_cat_info(spr, surface)

		self.lostsprites = []


	def draw_msg_cloud(self, spr, surface):
		# draw cloud
		surface.blit(self.cat_msg_cloud, (spr.rect.topleft[0], spr.rect.topleft[1] - 60))
		# draw msg
		value_msg = gameFont.cloud_value_disp("$" + str(spr.value) + "!", (spr.rect.topleft[0] + 25, spr.rect.topleft[1] - 30))
		value_msg.draw(surface)

	def draw_normal_msg_cloud(self, spr, surface):
		if spr.isFeed:
			#draw cloud
			surface.blit(self.normal_msg_cloud, (spr.rect.topleft[0]-200, spr.rect.topleft[1] - 30))
			value_msg = gameFont.normal_cloud_value_disp("A Li Ga Do!", (spr.rect.topleft[0] - 160, spr.rect.topleft[1] - 15))
			value_msg.draw(surface)

		if spr.is_showanon:
			surface.blit(self.normal_msg_cloud, (spr.rect.topleft[0]-200, spr.rect.topleft[1] - 30))
			value_msg = gameFont.normal_cloud_value_disp(CatInfoDisp.anonymous_texts[spr.textid], (spr.rect.topleft[0] - 160, spr.rect.topleft[1] - 15))
			value_msg.draw(surface)

	def draw_cat_info(self, spr, surface):
		show_img = pygame.transform.scale(spr.images[0], (60, 60))
		surface.blit(self.catinfo_bg, (0, 590))
		surface.blit(show_img, (20, 610))
		# disp feed situation
		surface.blit(self.food_icon_images[0], (30, 870))
		surface.blit(self.food_icon_images[1], (130, 870))
		surface.blit(self.food_icon_images[2], (230, 870))
		gameFont.cat_descrip_disp(str(spr.reward0), (45, 920)).draw(surface)
		gameFont.cat_descrip_disp(str(spr.reward1), (139, 920)).draw(surface)
		gameFont.cat_descrip_disp(str(spr.reward2), (239, 920)).draw(surface)
		# disp type and hp
		cname = gameFont.cat_descrip_disp("TYPE: " + spr.name, (120, 610))
		cname.draw(surface)
		chp = gameFont.cat_descrip_disp("HP: " + str(spr.hp), (120, 640))
		chp.draw(surface)
		descrip = gameFont.cat_descrip_disp("Introduction:",(20, 680))
		descrip.draw(surface)
		# disp details
		CatInfoDisp.show_descrip(spr.name, surface)
