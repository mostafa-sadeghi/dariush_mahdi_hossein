import pygame
pygame.init()


SCREEN_WIDTH = 1100
SCREEN_HEIGHT = 700
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))


font64 = pygame.font.Font("Facon.ttf", 64)
# font64 = pygame.font.SysFont("Arial", 64)
welcome_text = font64.render('Welcome To First Game', True, (240, 10, 190))
welcome_rect = welcome_text.get_rect(center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))

monster_img = pygame.image.load("monster.png")
monster_rect = monster_img.get_rect(center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2+100))


start_time = pygame.time.get_ticks()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0,0,0))
    if pygame.time.get_ticks() - start_time < 3000:
        screen.blit(welcome_text, welcome_rect)
        screen.blit(monster_img, monster_rect)
    pygame.display.update()