import pygame
import os
pygame.font.init()

WIDTH, HEIGHT = 600, 1000
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('BATTLESHIP!!!')
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
HEALTH_FONT = pygame.font.SysFont('comicsans', 30)
WINNER_FONT = pygame.font.SysFont('comicsans', 50)


FPS = 60
VEL = 5
BLACK = (0, 0, 0)
BORDER = pygame.Rect(0, HEIGHT//2 - 5, WIDTH, 1)
BULLETS_VAL = 10
MAX_BULLETS = 3


SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 50, 50
YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_yellow.png'))
YELLOW_SPACESHIP = pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT))

RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_red.png'))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 180)
SPACE = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'spatiu.png')), (WIDTH, HEIGHT))

YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2


def drew_window(red, yellow, yellow_bullets, red_bullets, yellow_health, red_health):
	WIN.blit(SPACE, (0, 0))
	pygame.draw.rect(WIN, BLACK, BORDER)
	
	yellow_health_text = HEALTH_FONT.render('Viata Tati: ' + str(yellow_health), 1, WHITE)
	red_health_text = HEALTH_FONT.render('Viata Tudor: ' + str(red_health), 1, WHITE)
	WIN.blit(yellow_health_text, (10, 10))
	WIN.blit(red_health_text, (350, 950))
	
	WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
	WIN.blit(RED_SPACESHIP, (red.x, red.y))
	for bullet in yellow_bullets:
		pygame.draw.rect(WIN, YELLOW, bullet)
	for bullet in red_bullets:
		pygame.draw.rect(WIN, RED, bullet)
	pygame.display.update()


def yellow_handle_movement(keys_pressed, yellow):
	if keys_pressed[pygame.K_a] and yellow.x - VEL > 0:
		yellow.x -= VEL
	if keys_pressed[pygame.K_d] and yellow.x + VEL + yellow.width < WIDTH:
		yellow.x += VEL
	if keys_pressed[pygame.K_w] and yellow.y - VEL > 0:
		yellow.y -= VEL
	if keys_pressed[pygame.K_s] and yellow.y + VEL + yellow.height < BORDER.y:
		yellow.y += VEL

		
def red_handle_movement(keys_pressed, red):
	if keys_pressed[pygame.K_LEFT] and red.x - VEL > 0:
		red.x -= VEL
	if keys_pressed[pygame.K_RIGHT] and red.x + VEL + red.width < WIDTH:
		red.x += VEL
	if keys_pressed[pygame.K_UP] and red.y - VEL > BORDER.y + BORDER.height:
		red.y -= VEL
	if keys_pressed[pygame.K_DOWN] and red.y + VEL + red.height < HEIGHT:
		red.y += VEL


def handle_bullets(yellow_bullets, red_bullets, yellow, red):
	for bullet in yellow_bullets:
		bullet.y += BULLETS_VAL
		if red.colliderect(bullet):
			pygame.event.post(pygame.event.Event(RED_HIT))
			yellow_bullets.remove(bullet)
		elif bullet.y > HEIGHT:
			yellow_bullets.remove(bullet)

	for bullet in red_bullets:
		bullet.y -= BULLETS_VAL
		if yellow.colliderect(bullet):
			pygame.event.post(pygame.event.Event(YELLOW_HIT))
			red_bullets.remove(bullet)
		elif bullet.y < 0:
			red_bullets.remove(bullet)


def draw_winner(text):
	draw_text = WINNER_FONT.render(text, 1, WHITE)
	WIN.blit(draw_text, (WIDTH/2 - draw_text.get_width()/2, HEIGHT//2 - draw_text.get_height()/2))
	pygame.display.update()
	pygame.time.delay(5000)


def BattleShip():
	yellow = pygame.Rect(275, 175, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
	red = pygame.Rect(275, 825, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
	yellow_bullets = []
	red_bullets = []
	yellow_health = 10
	red_health = 30
	clock = pygame.time.Clock()
	run = True
	while run:
		clock.tick(FPS)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
				pygame.quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame. K_LCTRL and len(yellow_bullets) < MAX_BULLETS:
					bullet = pygame.Rect(yellow.x + yellow.width//2, yellow.y + yellow.height//2, 5, 10)
					yellow_bullets.append(bullet)
				if event.key == pygame.K_RCTRL and len(red_bullets) < MAX_BULLETS:
					bullet = pygame.Rect(red.x + red.width//2, red.y + red.height//2, 5, 10)
					red_bullets.append(bullet)
			if event.type == YELLOW_HIT:
				yellow_health -= 1
			if event.type == RED_HIT:
				red_health -= 1
		winner_text = ''
		if yellow_health <= 0:
			winner_text = 'TUDOR CASTIGA!'
		if red_health <= 0:
			winner_text = 'TATI CASTIGA!'
		if winner_text != '':
			draw_winner(winner_text)
			break
		keys_pressed = pygame.key.get_pressed()
		yellow_handle_movement(keys_pressed, yellow)
		red_handle_movement(keys_pressed, red)
		
		handle_bullets(yellow_bullets, red_bullets, yellow, red)
		
		drew_window(red, yellow, yellow_bullets, red_bullets, yellow_health, red_health)
	BattleShip()
	
	
BattleShip()
