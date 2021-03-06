import pygame, sys, random
import pygame.locals as GAME_GLOBALS
import pygame.event as GAME_EVENTS

# Pygame Variables
pygame.init()
clock = pygame.time.Clock()

blob = pygame.image.load('images/Cat03.png')

windowWidth = 800
windowHeight = 800
rectX =  10.0
rectY = 10.0
rectendX = 30
rectendY = 20

surface = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption('Pygame Keyboard!')

# Square Variables
playerSize = 20
playerX = (windowWidth / 2) - (playerSize / 2)
playerY = windowHeight - playerSize
playerVX = 1.0
playerVY = 0.0
jumpHeight = 80.0
moveSpeed = 1.0
maxSpeed = 10.0
gravity = 1.0


# Keyboard Variables
leftDown = False
rightDown = False
haveJumped = False

def quitgame():
	pygame.quit()
	sys.exit()
	
def move():

	global playerX, playerY, playerVX, playerVY, haveJumped, gravity

	# Move left 
	if leftDown:
		#If we're already moving to the right, reset the moving speed and invert the direction
		if playerVX > 0.0:
			playerVX = moveSpeed
			playerVX = -playerVX	
		# Make sure our square doesn't leave our window to the left
		if playerX > 0:
			playerX += playerVX	

	# Move right
	if rightDown:
		# If we're already moving to the left reset the moving speed again
		if playerVX < 0.0:
			playerVX = moveSpeed
		# Make sure our square doesn't leave our window to the right
		if playerX + playerSize < windowWidth:
			playerX += playerVX

	if playerVY > 1.0:
		playerVY = playerVY * 0.9
	else :
		playerVY = 0.0
		haveJumped = False

	# Is our square in the air? Better add some gravity to bring it back down!
	if playerY < windowHeight - playerSize:
		playerY += gravity
		gravity = gravity * 1.1
	else :
		playerY = windowHeight - playerSize
		gravity = 1.0

	playerY -= playerVY

	if playerVX > 0.0 and playerVX < maxSpeed or playerVX < 0.0 and playerVX > -maxSpeed:
		if haveJumped == False:
			playerVX = playerVX * 1.1


direction =1
	
while True:
	surface.fill((0, 0, 0))
	pygame.draw.rect(surface, (255, 255, 255), (rectX, rectY, rectendX, rectendY))
	if rectX > windowWidth:
		direction = -1
	if rectX < 0:
		direction = 1
	rectX += direction * random.randint(0, 10)
	if rectY > windowWidth:
		direction = -1
	if rectY < 0:
		direction = 1
	rectY += direction * random.randint(0, 10)
	# rectendX += direction
	# rectendY += direction
	pygame.draw.lines(surface, (53, 198, 27), False, [(100, 100), (100, 250), (200, 250)], 4)
	# pygame.draw.lines(window, (53, 198, 27), True, [(400, 200), (100, 100)], 4)
	pygame.draw.line(surface, (53, 198, 27), [250, 100], [250, 250], 4)
	pygame.draw.lines(surface, (53, 198, 27), False, [(300, 100), (400, 100), (300, 250), (400, 250)], 4)
	
	pygame.draw.rect(surface, (255,0,0), (playerX, playerY, playerSize, playerSize))
	surface.blit(blob, (playerX, playerY, playerSize, playerSize))

	# Get a list of all events that happened since the last redr..........000000000000aw
	for event in GAME_EVENTS.get():

		if event.type == pygame.KEYDOWN:

			if event.key == pygame.K_LEFT:
				leftDown = True
			if event.key == pygame.K_RIGHT:
				rightDown = True
			if event.key == pygame.K_UP:
				if not haveJumped:
					haveJumped = True
					playerVY += jumpHeight
			if event.key == pygame.K_ESCAPE:
				quitGame()

		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT:
				leftDown = False
				playerVX = moveSpeed
			if event.key == pygame.K_RIGHT:
				rightDown = False
				playerVX = moveSpeed

		if event.type == GAME_GLOBALS.QUIT:
			quitGame()

	move()

	
	
	
	clock.tick(60)
	pygame.display.update()
