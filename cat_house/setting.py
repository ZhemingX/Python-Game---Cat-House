"""settings for all basic components"""
import pygame

# home path
path = "/home/aaa/bbb/location"

"""---------scene----------"""

# start scene
startbg = pygame.transform.scale(pygame.image.load(path + "/cat_house/images/scene/startbg.png"), (700, 1000))
playicon = pygame.transform.scale(pygame.image.load(path + "/cat_house/images/scene/play.png"), (300, 160))
decwall = pygame.transform.scale(pygame.image.load(path + "/cat_house/images/scene/scene_wall_y.png"), (400, 1000))
# screen setting
caption = "cat house"
screen_size = (1500,1000)
major_bg = path + "/cat_house/images/scene/major_bg.png"

# wall setting
wall_x_bg = path + "/cat_house/images/scene/wall2_x.png"
wall_y_bg = path + "/cat_house/images/scene/wall2_y.png"
wall_x_size = (int(0.8*screen_size[0]/5), 50)
wall_y_size = (50, int((screen_size[1]-100)/5))

# bot cat setting
botcat_bg = path + "/cat_house/images/scene/scene_botcat.png"
botcat_shine_bg = path + "/cat_house/images/scene/scene_botcat_shine.png"
botcat_size = (100, 120)

# bot cat floor setting
botfloor_bg = path + "/cat_house/images/scene/bot_floor.png"
botfloor_size = (120, 120)

# mouse setting
mouse_icon_basic_path = path + "/cat_house/images/scene/pretty_mouse.png"
mouse_size = (50, 50)
mouse_icon_basic = pygame.transform.scale(pygame.image.load(mouse_icon_basic_path), mouse_size)
mouse_feather = pygame.transform.scale(pygame.image.load(path + "/cat_house/images/scene/feather.png"), mouse_size)
mouse_shovel = pygame.transform.scale(pygame.image.load(path + "/cat_house/images/scene/shovel.png"), mouse_size)

# check window pops
cwp_image_path = path + "/cat_house/images/scene/check_window_pop.png"
cancel_image_path = path + "/cat_house/images/scene/cancel3.png"
ccb_image_path = path + "/cat_house/images/scene/confirm_cat_button.png"

cwp_image = pygame.transform.scale(pygame.image.load(cwp_image_path), (480, 288))
cwp_pos = (750, 400) # center pos
cancel_image = pygame.transform.scale(pygame.image.load(cancel_image_path), (35, 35))
cancel_pos = (562, 280)
ccb_image = pygame.transform.scale(pygame.image.load(ccb_image_path), (90, 90))
ccb_pos = (750, 480)

# shop window pops
shop_image = pygame.transform.scale(pygame.image.load(cwp_image_path), (530, 390))
shop_pos = (750, 400)
cancel_s_pos = (540, 240)
increase_image = pygame.transform.scale(pygame.image.load(path + "/cat_house/images/scene/increase.png"), (30, 30))
decrease_image = pygame.transform.scale(pygame.image.load(path + "/cat_house/images/scene/decrease.png"), (30, 30))
enable_shop_image = pygame.transform.scale(pygame.image.load(path + "/cat_house/images/scene/enable_shop.png"), (120, 60))
disable_shop_image = pygame.transform.scale(pygame.image.load(path + "/cat_house/images/scene/disable_shop.png"), (120, 60))
shopcaption_image = pygame.transform.scale(pygame.image.load(path + "/cat_house/images/scene/shop_caption.png"), (140, 55))
showbg_image = pygame.transform.scale(pygame.image.load(path + "/cat_house/images/scene/frame2.png"), (100, 30))

# cat info window
catinfo_bg = pygame.transform.scale(pygame.image.load(path + "/cat_house/images/scene/catinfo_bg.png"), (300, 415))

# fps setting
fps = 80

# user pop:
#background
userpopbg_image_path = path + "/cat_house/images/scene/userpop.png"
userpopbg_image = pygame.transform.scale(pygame.image.load(userpopbg_image_path), (310, 1000))
# frame1
frame1_image_path = path + "/cat_house/images/scene/frame1.png"
frame1_image = pygame.transform.scale(pygame.image.load(frame1_image_path), (300, 120))
# shoptag
shoptag_image_path = path + "/cat_house/images/button/shoptag.png"
shoptag_image = pygame.transform.scale(pygame.image.load(shoptag_image_path), (180, 80))
shoptagon_image_path = path + "/cat_house/images/button/shoptag_on.png"
shoptagon_image = pygame.transform.scale(pygame.image.load(shoptagon_image_path), (180, 80))
# frame2
frame2_image_path = path + "/cat_house/images/scene/frame2.png"
frame2_image = pygame.transform.scale(pygame.image.load(frame2_image_path), (300, 60))
# food icon
food_paths = [path + "/cat_house/images/button/food0.png", path + "/cat_house/images/button/food1.png", path + "/cat_house/images/button/food2.png"]
food_images = [pygame.transform.scale(pygame.image.load(food_path), (60, 60)) for food_path in food_paths]
food_images[2] = pygame.transform.scale(pygame.image.load(food_paths[2]), (55, 55))
food_mouse_images = [pygame.transform.scale(pygame.image.load(food_path), mouse_size) for food_path in food_paths]

# cat produce initial space
cat_born_space = ((400, 1200), (400, 600))

""" ----Cat Entity ---- """
cat_size = (120, 120)

#-----common rule--------#
# speed (speed for each cat is among 30, 40, 50)

# space for cat move
# a tuple (topleft coordinate, bottomright coordinate)
topleft = (int(0.2*screen_size[0]) + wall_y_size[0], botfloor_size[1] + 10)
bottomright = (screen_size[0] - botfloor_size[0], screen_size[1] - botfloor_size[1])
ground_info = (topleft, bottomright)

# dead state image
deadcat_image_path = path + "/cat_house/images/cat/deadcat.png"
deadcat_image = pygame.transform.scale(pygame.image.load(deadcat_image_path), cat_size)


#-----individual config--#

# basecat image
basecat_image_paths = [path + "/cat_house/images/cat/basecat/basecat" + str(i) + ".png" for i in range(0,8)]
basecat_images = [pygame.transform.scale(pygame.image.load(img_path), cat_size) for img_path in basecat_image_paths] 

# yellowwhitecat image
ywcat_image_paths = [path + "/cat_house/images/cat/yellowwhitecat/yellowwhitecat" + str(i) + ".png" for i in range(0,8)]
ywcat_images = [pygame.transform.scale(pygame.image.load(img_path), cat_size) for img_path in ywcat_image_paths] 
# browncat image
browncat_image_paths = [path + "/cat_house/images/cat/browncat/browncat" + str(i) + ".png" for i in range(0,8)]
browncat_images = [pygame.transform.scale(pygame.image.load(img_path), cat_size) for img_path in browncat_image_paths] 

# blackcat image
blackcat_image_paths = [path + "/cat_house/images/cat/blackcat/blackcat" + str(i) + ".png" for i in range(0,8)]
blackcat_images = [pygame.transform.scale(pygame.image.load(img_path), cat_size) for img_path in blackcat_image_paths] 

# bullcat image
bullcat_image_paths = [path + "/cat_house/images/cat/bullcat/bullcat" + str(i) + ".png" for i in range(0,8)]
bullcat_images = [pygame.transform.scale(pygame.image.load(img_path), cat_size) for img_path in bullcat_image_paths] 

# supercat image
supercat_image_paths = [path + "/cat_house/images/cat/supercat/supercat" + str(i) + ".png" for i in range(0,8)]
supercat_images = [pygame.transform.scale(pygame.image.load(img_path), cat_size) for img_path in supercat_image_paths] 

# pbcat image
pbcat_image_paths = [path + "/cat_house/images/cat/pbcat/pbcat" + str(i) + ".png" for i in range(0,8)]
pbcat_images = [pygame.transform.scale(pygame.image.load(img_path), cat_size) for img_path in pbcat_image_paths] 

# badcat image
badcat_image_paths = [path + "/cat_house/images/cat/badcat/badcat" + str(i) + ".png" for i in range(0,8)]
badcat_images = [pygame.transform.scale(pygame.image.load(img_path), cat_size) for img_path in badcat_image_paths] 


"""----Button Entity-----"""

# CatProduceButton
cpb_size = (100, 60)
cpb_position = (540, 60) # center position
cpb_on_path = path + "/cat_house/images/button/catproducebutton_on.png"
cpb_off_path = path + "/cat_house/images/button/catproducebutton_off.png"
cpb_on = pygame.transform.scale(pygame.image.load(cpb_on_path), cpb_size)
cpb_off = pygame.transform.scale(pygame.image.load(cpb_off_path), cpb_size)




"""---Other flexible Components"""
msg_cloud = path + "/cat_house/images/scene/msg_cloud.png"
msg_cloud_image = pygame.transform.scale(pygame.image.load(msg_cloud), (100, 100))

cat_convert = path + "/cat_house/images/cat/cat_convert.png"
cat_convert_image = pygame.transform.scale(pygame.image.load(cat_convert), (120, 120))

normal_msg_cloud = path + "/cat_house/images/scene/normal_msg_cloud.png"
normal_msg_cloud_image = pygame.transform.scale(pygame.image.load(normal_msg_cloud), (220, 60))
