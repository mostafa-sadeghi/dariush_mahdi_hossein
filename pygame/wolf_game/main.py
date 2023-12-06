import pygame

pygame.init()


SCREEN_WIDTH = 1100
SCREEN_HEIGHT = 700
FPS = 60
clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

wolf_image = pygame.image.load("assets/wolf.png")
wolf_rect = wolf_image.get_rect()
wolf_rect.bottomright = (SCREEN_WIDTH, SCREEN_HEIGHT)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        wolf_rect.y -= 5

    # TODO حرکت به سایر جهت ها

    screen.fill((0,0,0))
    screen.blit(wolf_image, wolf_rect)
    pygame.display.update()
    clock.tick(FPS)


