import pygame

def print_grid(surface, W, H, grid):
	cell = min(W // grid, H // grid)
	board_px = cell * grid
	ox = (W - board_px) // 2
	oy = (H - board_px) // 2

	surface.fill((180, 230, 120))

if __name__ == "__main__":
	pygame.init()
	W, H = 800, 800
	surface = pygame.display.set_mode((W, H))
	pygame.display.set_caption("PySnake")

	clock = pygame.time.Clock()

	running = True
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
		print_grid(surface, W, H, 18)
		pygame.display.flip()
		clock.tick(10)
