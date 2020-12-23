"""Button Class"""
import pygame
import setting

class PlayButton(object):

	def __init__(self, pos):
		self.image = setting.playicon
		self.position = pos

	def isOver(self):
		# check whether the mouse is on the button
		mx, my = pygame.mouse.get_pos()
		cx, cy = self.position
		bw, bh = self.image.get_size()

		in_x = cx - bw/2 < mx < cx + bw/2
		in_y = cy - bh/2 < my < cy + bh/2

		return in_x and in_y

	def draw(self, screen):
		cx, cy = self.position
		bw, bh = self.image.get_size()
		screen.blit(self.image, (cx - bw/2, cy - bh/2))

class CatProduceButton(object):

	def __init__(self):
		self.imageUp = setting.cpb_off
		self.imageDown = setting.cpb_on
		self.position = setting.cpb_position

	def isOver(self):
		# check whether the mouse is on the button
		mx, my = pygame.mouse.get_pos()
		cx, cy = self.position
		bw, bh = self.imageUp.get_size()

		in_x = cx - bw/2 < mx < cx + bw/2
		in_y = cy - bh/2 < my < cy + bh/2

		return in_x and in_y

	def draw(self, screen):
		cx, cy = self.position
		bw, bh = self.imageUp.get_size()

		if self.isOver():
			screen.blit(self.imageDown, (cx - bw/2, cy - bh/2))
		else:
			screen.blit(self.imageUp, (cx - bw/2, cy - bh/2))


class CheckWindowCancel(object):

	def __init__(self, pos):
		self.image = setting.cancel_image
		self.position = pos

	def isOver(self):
		# check whether the mouse is on the button
		mx, my = pygame.mouse.get_pos()
		cx, cy = self.position
		bw, bh = self.image.get_size()

		in_x = cx - bw/2 < mx < cx + bw/2
		in_y = cy - bh/2 < my < cy + bh/2

		return in_x and in_y

	def draw(self, screen):
		cx, cy = self.position
		bw, bh = self.image.get_size()
		screen.blit(self.image, (cx - bw/2, cy - bh/2))


class CheckWindowConfirm(object):

	def __init__(self):
		self.image = setting.ccb_image
		self.position = setting.ccb_pos

	def isOver(self):
		# check whether the mouse is on the button
		mx, my = pygame.mouse.get_pos()
		cx, cy = self.position
		bw, bh = self.image.get_size()

		in_x = cx - bw/2 < mx < cx + bw/2
		in_y = cy - bh/2 < my < cy + bh/2

		return in_x and in_y

	def draw(self, screen):
		cx, cy = self.position
		bw, bh = self.image.get_size()
		screen.blit(self.image, (cx - bw/2, cy - bh/2))

class ShopButton(object):

	def __init__(self):
		self.imageUp = setting.shoptag_image
		self.imageDown = setting.shoptagon_image
		self.position = (150, 60)

	def isOver(self):
		# check whether the mouse is on the button
		mx, my = pygame.mouse.get_pos()
		cx, cy = self.position
		bw, bh = self.imageUp.get_size()

		in_x = cx - bw/2 < mx < cx + bw/2
		in_y = cy - bh/2 < my < cy + bh/2

		return in_x and in_y

	def draw(self, screen):
		cx, cy = self.position
		bw, bh = self.imageUp.get_size()

		if self.isOver():
			screen.blit(self.imageDown, (cx - bw/2, cy - bh/2))
		else:
			screen.blit(self.imageUp, (cx - bw/2, cy - bh/2))

class FoodButton(object):

	def __init__(self, image, pos):
		self.image = image
		self.position = pos

	def isOver(self):
		# check whether the mouse is on the button
		mx, my = pygame.mouse.get_pos()
		cx, cy = self.position
		bw, bh = self.image.get_size()

		in_x = cx - bw/2 < mx < cx + bw/2
		in_y = cy - bh/2 < my < cy + bh/2

		return in_x and in_y

	def draw(self, screen):
		cx, cy = self.position
		bw, bh = self.image.get_size()
		screen.blit(self.image, (cx - bw/2, cy - bh/2))

class IncreaseButton(object):

	def __init__(self, pos):
		self.image = setting.increase_image
		self.position = pos

	def isOver(self):
		# check whether the mouse is on the button
		mx, my = pygame.mouse.get_pos()
		cx, cy = self.position
		bw, bh = self.image.get_size()

		in_x = cx - bw/2 < mx < cx + bw/2
		in_y = cy - bh/2 < my < cy + bh/2

		return in_x and in_y

	def draw(self, screen):
		cx, cy = self.position
		bw, bh = self.image.get_size()
		screen.blit(self.image, (cx - bw/2, cy - bh/2))

class DecreaseButton(object):

	def __init__(self, pos):
		self.image = setting.decrease_image
		self.position = pos

	def isOver(self):
		# check whether the mouse is on the button
		mx, my = pygame.mouse.get_pos()
		cx, cy = self.position
		bw, bh = self.image.get_size()

		in_x = cx - bw/2 < mx < cx + bw/2
		in_y = cy - bh/2 < my < cy + bh/2

		return in_x and in_y

	def draw(self, screen):
		cx, cy = self.position
		bw, bh = self.image.get_size()
		screen.blit(self.image, (cx - bw/2, cy - bh/2))

class ShopConfirmButton(object):

	def __init__(self):
		self.imageUp = setting.enable_shop_image
		self.imageDown = setting.disable_shop_image
		self.position = (750, 550)
		self.enable = 1

	def isOver(self):
		# check whether the mouse is on the button
		mx, my = pygame.mouse.get_pos()
		cx, cy = self.position
		bw, bh = self.imageUp.get_size()

		in_x = cx - bw/2 < mx < cx + bw/2
		in_y = cy - bh/2 < my < cy + bh/2

		return in_x and in_y

	def draw(self, screen):
		cx, cy = self.position
		bw, bh = self.imageUp.get_size()

		if self.enable == 1:
			if self.isOver():
				screen.blit(self.imageDown, (cx - bw/2, cy - bh/2))
			else:
				screen.blit(self.imageUp, (cx - bw/2, cy - bh/2))
		else:
			screen.blit(self.imageDown, (cx - bw/2, cy - bh/2))

class FeatherButton(object):

	def __init__(self, pos):
		self.image = setting.mouse_feather
		self.position = pos

	def isOver(self):
		# check whether the mouse is on the button
		mx, my = pygame.mouse.get_pos()
		cx, cy = self.position
		bw, bh = self.image.get_size()

		in_x = cx - bw/2 < mx < cx + bw/2
		in_y = cy - bh/2 < my < cy + bh/2

		return in_x and in_y

	def draw(self, screen):
		cx, cy = self.position
		bw, bh = self.image.get_size()
		screen.blit(self.image, (cx - bw/2, cy - bh/2))


class ShovelButton(object):

	def __init__(self, pos):
		self.image = setting.mouse_shovel
		self.position = pos

	def isOver(self):
		# check whether the mouse is on the button
		mx, my = pygame.mouse.get_pos()
		cx, cy = self.position
		bw, bh = self.image.get_size()

		in_x = cx - bw/2 < mx < cx + bw/2
		in_y = cy - bh/2 < my < cy + bh/2

		return in_x and in_y

	def draw(self, screen):
		cx, cy = self.position
		bw, bh = self.image.get_size()
		screen.blit(self.image, (cx - bw/2, cy - bh/2))


