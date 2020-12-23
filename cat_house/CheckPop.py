"""window pops of checking if produce a cat"""
import pygame
import setting
import Button
import gameFont

askinfo = "Do you want to buy a base cat?"
refuseinfo = "Your balance is insufficient...TnT"
priceinfo   = "$50 per cat"

class CheckWindowPop(object):

	def __init__(self):
		self.windowimage = setting.cwp_image
		self.windowpos = setting.cwp_pos
		self.cancelbutton = Button.CheckWindowCancel(setting.cancel_pos)
		self.ccbbutton = Button.CheckWindowConfirm()
		self.ask_disp = gameFont.GameFont(askinfo, 28, (139, 69, 19), (555, 350))
		self.refuse_disp = gameFont.GameFont(refuseinfo, 30, (139, 69, 19), (548, 360))
		self.price_disp = gameFont.GameFont(priceinfo, 28, (139, 69, 19), (685, 390))
		self.dead_cat = setting.deadcat_image
	def draw(self, screen, score):
		wx, wy = self.windowimage.get_size()
		screen.blit(self.windowimage, (self.windowpos[0] - wx/2, self.windowpos[1] - wy/2))
		self.cancelbutton.draw(screen)
		if score >= 50:
			self.ccbbutton.draw(screen)
			self.ask_disp.draw(screen)
			self.price_disp.draw(screen)
		else:
			self.refuse_disp.draw(screen)
			screen.blit(self.dead_cat, (685,380))
