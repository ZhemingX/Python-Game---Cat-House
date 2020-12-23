# text of cat info
# each cat has three sentences for description

import pygame
import gameFont

# base cat
basecat_descrip = [
	"level 0",
	"weak small mild",
	"remember to feed him"
]

browncat_descrip = [
	"level 1",
	"smart mild",
	"need to be stronger"
]

ywcat_descrip = [
	"level 1",
	"smart small mild",
	"cousin of browncat"
]

blackcat_descrip = [
	"level 2",
	"loyalty guy",
	"feed me, dont like black"
]

pbcat_descrip = [
	"level 2",
	"strange type, smart",
	"am I looking cool?"
]

bullcat_descrip = [
	"level 2",
	"strong fierce angry",
	"you f*** ugly face"
]

badcat_descrip = [
	"level 2",
	"mischeivous phantom",
	"you got me..good luck~"
]

supercat_descrip = [
	"level 3",
	"strong rare powerful",
	"congratulations!"
]

cat_descrip = {
	"basecat" : basecat_descrip,
	"browncat" : browncat_descrip,
	"ywcat" : ywcat_descrip,
	"blackcat" : blackcat_descrip,
	"pbcat" : pbcat_descrip,
	"bullcat" : bullcat_descrip,
	"badcat" : badcat_descrip,
	"supercat" : supercat_descrip,
}

def show_descrip(cname, surface):
	catdescrip = cat_descrip[cname]
	gameFont.cat_level_disp(catdescrip[0], (20, 720)).draw(surface)
	gameFont.cat_descrip_disp(catdescrip[1], (20, 760)).draw(surface)
	gameFont.cat_descrip_disp(catdescrip[2], (20, 800)).draw(surface)


# cat anonymous text display (maximum 15 characters)
anonymous_texts = [
	"Day Day Up!",
	"Keep on Work!",
	"No 3 Bad Cats!",
	"Hello my owner",
	"Good Weather",
	"PEACE GAME",
	"Really peace?",
	"Idiot...",
	"Feed Me!"
]