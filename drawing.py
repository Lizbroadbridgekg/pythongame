import pygame, sys, random
import pygame.event as GAME_EVENTS
import pygame.locals as GAME_GLOBALS
import keyboard

pygame.init()

clock = pygame.time.Clock()

windowwidth = 500
windowheight = 400
rectX =  10.0
rectY = 10.0
rectendX = 30
rectendY = 20

def quitgame():
	pygame.quit()
	sys.exit()

window = pygame.display.set_mode( (windowwidth, windowheight) )
direction =1

while True:
	window.fill((0, 0, 0))
	
	pygame.draw.rect(window, (255, 255, 255), (rectX, rectY, rectendX, rectendY))
	if rectX > windowwidth:
		direction = -1
	if rectX < 0:
		direction = 1
	rectX += direction * random.randint(0, 10)
	if rectY > windowwidth:
		direction = -1
	if rectY < 0:
		direction = 1
	rectY += direction * random.randint(0, 10)
	# rectendX += direction
	# rectendY += direction
	pygame.draw.lines(window, (53, 198, 27), False, [(100, 100), (100, 250), (200, 250)], 4)
	# pygame.draw.lines(window, (53, 198, 27), True, [(400, 200), (100, 100)], 4)
	pygame.draw.line(window, (53, 198, 27), [250, 100], [250, 250], 4)
	pygame.draw.lines(window, (53, 198, 27), False, [(300, 100), (400, 100), (300, 250), (400, 250)], 4)
	
	for event in GAME_EVENTS.get():
		if event.type == GAME_GLOBALS.QUIT:
			quitgame()
			
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				quitgame()
	clock.tick(200)
	pygame.display.update()
	
	
	
	
	
	
	
	
	
	