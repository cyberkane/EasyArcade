import pygame
import spritesheet as sps

pygame.init()

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Spritesheets')

sprite_sheet_image = pygame.image.load('char_blue.png').convert_alpha()
sprite_sheet = sps.SpriteSheet(sprite_sheet_image)

BG = (50, 50, 50)
BLACK = (0, 0, 0)


frame_0 = sprite_sheet.get_image(0, 56, 44, 3, BLACK)
#frame_1 = sprite_sheet.get_image(1, 140, 60, 3, BLACK)
#frame_2 = sprite_sheet.get_image(2, 180, 60, 3, BLACK)
#frame_3 = sprite_sheet.get_image(3, 240, 60, 3, BLACK)

run = True
while run:

	#update background
	screen.fill(BG)

	#show frame image
	screen.blit(frame_0, (0, 0))
#	screen.blit(frame_1, (60, 0))
#	screen.blit(frame_2, (120, 0))
#	screen.blit(frame_3, (180, 0))

	#event handler
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	pygame.display.update()

pygame.quit()