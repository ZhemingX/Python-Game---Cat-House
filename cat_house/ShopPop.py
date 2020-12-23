"""window pops of shopping"""
import pygame
import setting
import Button
import gameFont

class ShopWindowPop(object):

	def __init__(self):
		self.windowimage = setting.shop_image
		self.windowpos = setting.shop_pos
		self.cancelbutton = Button.CheckWindowCancel(setting.cancel_s_pos)
		# amount change button
		self.increase0 = Button.IncreaseButton((550, 465))
		self.decrease0 = Button.DecreaseButton((640, 465))		
		self.increase1 = Button.IncreaseButton((700, 465))
		self.decrease1 = Button.DecreaseButton((790, 465))		
		self.increase2 = Button.IncreaseButton((850, 465))
		self.decrease2 = Button.DecreaseButton((940, 465))
		#
		self.showbg = setting.showbg_image
		self.shopconfirm = Button.ShopConfirmButton()
		self.shopcaption = setting.shopcaption_image
		self.remind_info = gameFont.shop_remind_info_disp()
		self.food_images = setting.food_images
		# amount & price
		self.num0 = 0
		self.price0 = 80
		self.num1 = 0
		self.price1 = 90
		self.num2 = 0
		self.price2 = 100
		self.price0_disp = gameFont.price_disp(self.price0, (580, 400))
		self.price1_disp = gameFont.price_disp(self.price1, (730, 400))
		self.price2_disp = gameFont.price_disp(self.price2, (880, 400))
		self.num0_disp = gameFont.amount_order_disp(self.num0, (580, 465))
		self.num1_disp = gameFont.amount_order_disp(self.num1, (730, 465))
		self.num2_disp = gameFont.amount_order_disp(self.num2, (880, 465))
		self.total = self.num0 * self.price0 + self.num1 * self.price1 + self.num2 * self.price2
		self.total_disp = gameFont.total_disp('Total Amount: $' + str(self.total), (550, 483))

	def draw(self, screen, score):
		wx, wy = self.windowimage.get_size()
		screen.blit(self.windowimage, (self.windowpos[0] - wx/2, self.windowpos[1] - wy/2))
		self.cancelbutton.draw(screen)
		screen.blit(self.shopcaption, (680, 220))
		self.remind_info.draw(screen)
		# draw food icon
		screen.blit(self.food_images[0], (570, 330))
		screen.blit(self.food_images[1], (720, 330))
		screen.blit(self.food_images[2], (870, 333))
		# draw amount choice tag
		screen.blit(self.showbg, (550, 450))
		self.increase0.draw(screen)
		self.decrease0.draw(screen)
		screen.blit(self.showbg, (700, 450))
		self.increase1.draw(screen)
		self.decrease1.draw(screen)
		screen.blit(self.showbg, (850, 450))
		self.increase2.draw(screen)
		self.decrease2.draw(screen)
		# display price
		self.price0_disp.draw(screen)
		self.price1_disp.draw(screen)
		self.price2_disp.draw(screen)
		# display amount
		self.num0_disp = gameFont.amount_order_disp(self.num0, (580, 450))
		self.num1_disp = gameFont.amount_order_disp(self.num1, (730, 450))
		self.num2_disp = gameFont.amount_order_disp(self.num2, (880, 450))
		self.num0_disp.draw(screen)
		self.num1_disp.draw(screen)
		self.num2_disp.draw(screen)
		# display total
		self.total = self.num0 * self.price0 + self.num1 * self.price1 + self.num2 * self.price2
		self.total_disp = gameFont.total_disp('Total Amount: $' + str(self.total), (550, 483))
		self.total_disp.draw(screen)
		# display confirm button
		if score >= self.total:
			self.shopconfirm.enable = 1
		else:
			self.shopconfirm.enable = 0
		self.shopconfirm.draw(screen)
