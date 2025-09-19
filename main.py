import pygame

def build_board_surface(W, H, grid=18):
    cell = min(W // grid, H // grid)
    board_px = cell * grid
    ox = (W - board_px) // 2
    oy = (H - board_px) // 2

    FRAME  = (34, 85, 34)
    LIGHT  = (180, 230, 120)
    DARK   = (160, 210, 100)

    board = pygame.Surface((board_px, board_px))

    for r in range(grid):
        for c in range(grid):
            x = c * cell
            y = r * cell
            color = LIGHT if (r + c) % 2 == 0 else DARK
            pygame.draw.rect(board, color, (x, y, cell, cell))

    return board, cell, ox, oy, FRAME

if __name__ == "__main__":
    pygame.init()
    W, H = 800, 800
    surface = pygame.display.set_mode((W, H))
    pygame.display.set_caption("PySnake")

    clock = pygame.time.Clock()

    board, cell, ox, oy, FRAME = build_board_surface(W, H, 18)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        surface.fill(FRAME)
        surface.blit(board, (ox, oy))
        pygame.draw.rect(surface, (25, 60, 25),
                         (ox, oy, board.get_width(), board.get_height()), 2)

        pygame.display.flip()
        clock.tick(10)

    pygame.quit()
