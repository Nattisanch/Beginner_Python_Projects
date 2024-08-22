import pygame

x = 50
y = 425
width = 40
height = 60 
vel = 5

pygame.init()
root = pygame.display.set_mode((500, 500))
pygame.display.set_caption('my first game')
clock = pygame.time.Clock()
running = True

isJump = False
jumpCount = 10

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
    if keys[pygame.K_RIGHT] and x < 500 - width - vel:
        x += vel
    if not(isJump): 
        if keys[pygame.K_UP] and y > vel:
            y -= vel
        if keys[pygame.K_DOWN] and y < 500 - height - vel:  
            y += vel
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y-= (jumpCount ** 2) * 0.5 * neg
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10

    root.fill((0, 0, 0))  
    pygame.draw.rect(root, (255, 0, 0), (x, y, width, height)) 
    pygame.display.update()

    clock.tick(60)

pygame.quit()
