import pygame

s1 = pygame.sprite.Sprite()
s2 = pygame.sprite.Sprite()
s3 = pygame.sprite.Sprite()
s4 = pygame.sprite.Sprite()
g1 = pygame.sprite.Group()

#empty group
print(g1.sprites())

#add sprite
g1.add(s1)
g1.add([s1,s2,s3,s4])
print(g1.sprites())

# remove sprite
g = (s1.groups())[0]
g.remove(s2)
print(g1.sprites())
for s in g:
	if s != s1:
		g.remove(s)
print(g1.sprites())
