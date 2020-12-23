"""GAME Font Function"""

import pygame
import setting

font1 = 'arista-2.0/Arista2.0.ttf'

class GameFont(object):

	def __init__(self, text, font_size, font_color, font_position):
		self.text = text
		self.font_size = font_size
		self.font_color = font_color
		self.font_position = font_position

	def draw(self, screen):
		TextFormat = pygame.font.Font(font1, self.font_size)
		TextSurface = TextFormat.render(self.text, True, self.font_color)
		screen.blit(TextSurface, self.font_position)

# score display
def score_disp(text):
	return GameFont(text, 32, (128, 0, 0), (1150, 130))

# cloud value display
def cloud_value_disp(text, pos):
	return GameFont(text, 26, (128, 0, 0), pos)

# normal cloud value display
def normal_cloud_value_disp(text, pos):
	return GameFont(text, 20, (128, 0, 0), pos)

# food_number_display
def food_numbers_disp(number_list, pos_list):
	num0_disp = GameFont(number_list[0], 28, (139, 69, 19), pos_list[0])
	num1_disp = GameFont(number_list[1], 28, (139, 69, 19), pos_list[1])
	num2_disp = GameFont(number_list[2], 28, (139, 69, 19), pos_list[2])

	return [num0_disp, num1_disp, num2_disp]

# storage text display
def storage_disp():
	return GameFont("Storage", 32, (128, 0, 0), (90, 130))

# storage text display
def cat_info_disp():
	return GameFont("Cat Info", 32, (128, 0, 0), (90, 550))

# cat number display
def cat_num_disp(num):
	return GameFont("Cat Number: " + str(num), 24, (128, 0, 0), (30, 500))

# shop window remind info display
def shop_remind_info_disp():
	remind_info = "Maximum 0 items for each kind every purchase~"
	return GameFont(remind_info, 24, (139, 69, 19), (505, 275))

# amount of purchase display
def amount_order_disp(num, pos):
	return GameFont('X ' + str(num), 24, (139, 69, 19), pos)

# shop price display
def price_disp(num, pos):
	return GameFont('$' + str(num), 30, (139, 69, 19), pos)

# total price display
def total_disp(text, pos):	
	return GameFont(text, 26, (139, 69, 19), pos)

# cat descrip display (24 letters at most)
def cat_descrip_disp(text, pos):
	return GameFont(text, 24, (128, 0, 0), pos)

def cat_level_disp(text, pos):
	return GameFont(text, 24, (220, 20, 60), pos)