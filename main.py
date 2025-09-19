import pygame

def main():
	pygame.init()
	surface = pygame.display.set_mode((800, 800))
	pygame.display.set_caption("PySnake")
	color = (255, 0, 0)

	clock = pygame.time.Clock()

	running = True
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
		surface.fill(color)
		pygame.display.flip()
		clock.tick(10)

if __name__ == "__main__":
	main()
