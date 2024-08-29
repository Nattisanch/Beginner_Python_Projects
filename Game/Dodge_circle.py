import pygame
import sys
import random

pygame.init()


WIDTH, HEIGHT = 1280, 720
root = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dodge Circle")


PURPLE = (128, 0, 128)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


clock = pygame.time.Clock()
FPS = 60


player_radius = 40
player_position = pygame.Vector2(WIDTH / 2, HEIGHT / 2)
player_speed = 500


jump = False
jump_ct = 10


enemy_radius = 30
enemy_speed = 5
enemies = []


def create_enemy():
    x = random.randint(0, WIDTH)
    y = random.randint(-100, -40)
    return pygame.Vector2(x, y)


for _ in range(5):
    enemies.append(create_enemy())


def display_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    text_rect.center = (x, y)
    surface.blit(text_obj, text_rect)


def main_menu_screen():
    root.fill(WHITE)
    font = pygame.font.SysFont(None, 55)
    display_text("Main Menu", font, BLACK, root, WIDTH // 2, HEIGHT // 2 - 100)
    display_text("Start Game", font, BLACK, root, WIDTH // 2, HEIGHT // 2)
    pygame.display.update()
    pygame.time.wait(1000) 

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                if WIDTH // 2 - 100 < mouse_x < WIDTH // 2 + 100 and HEIGHT // 2 - 25 < mouse_y < HEIGHT // 2 + 25:
                    main_game()


def game_over_screen():
    root.fill(WHITE)
    font = pygame.font.SysFont(None, 55)
    display_text("Game Over", font, BLACK, root, WIDTH // 2, HEIGHT // 2 - 50)
    display_text("Try Again", font, RED, root, WIDTH // 2, HEIGHT // 2 + 50)
    display_text("Main Menu", font, BLACK, root, WIDTH // 2, HEIGHT // 2 + 150)
    pygame.display.update()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                if WIDTH // 2 - 100 < mouse_x < WIDTH // 2 + 100 and HEIGHT // 2 + 25 < mouse_y < HEIGHT // 2 + 75:
                    main_game()
                elif WIDTH // 2 - 100 < mouse_x < WIDTH // 2 + 100 and HEIGHT // 2 + 100 < mouse_y < HEIGHT // 2 + 200:
                    main_menu_screen()



def main_game():
    global jump, jump_ct  
    player_position = pygame.Vector2(WIDTH / 2, HEIGHT / 2)
    enemies = [create_enemy() for _ in range(5)]
    running = True
    dt = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        
        root.fill(PURPLE)
        pygame.draw.circle(root, BLUE, player_position, player_radius)

      
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            player_position.y -= player_speed * dt
        if keys[pygame.K_s]:
            player_position.y += player_speed * dt
        if keys[pygame.K_a]:
            player_position.x -= player_speed * dt
        if keys[pygame.K_d]:
            player_position.x += player_speed * dt
        if keys[pygame.K_SPACE] and not jump:
            jump = True
            jump_ct = 10 
        else:
            if jump:
                if jump_ct >= -10:
                    neg = 1
                    if jump_ct < 0:
                        neg = -1
                    player_position.y -= (jump_ct ** 2) * 0.5 * neg
                    jump_ct -= 1
                else:
                    jump = False
                    jump_ct = 10
              
        if player_position.x - player_radius < 0:
            player_position.x = player_radius
        if player_position.x + player_radius > WIDTH:
            player_position.x = WIDTH - player_radius
        if player_position.y - player_radius < 0:
            player_position.y = player_radius
        if player_position.y + player_radius > HEIGHT:
            player_position.y = HEIGHT - player_radius

        
        for enemy in enemies:
            enemy.y += enemy_speed
            if enemy.y > HEIGHT:
                enemy.x = random.randint(0, WIDTH)
                enemy.y = random.randint(-100, -40)
            pygame.draw.circle(root, RED, enemy, enemy_radius)

          
            distance = player_position.distance_to(enemy)
            if distance < player_radius + enemy_radius:
                game_over_screen()

        pygame.display.flip()
        dt = clock.tick(FPS) / 1000  

    pygame.quit()
    sys.exit()


main_menu_screen()
