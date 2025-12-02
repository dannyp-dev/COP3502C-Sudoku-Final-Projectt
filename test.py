import pygame

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Rectangle Example")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))  # White background

    # Draw a rectangle: (surface, color, (x, y, width, height), border thickness)
    pygame.draw.rect(screen, (0, 0, 0), (100, 100, 200, 200), 2)

    pygame.display.update()

pygame.quit()
