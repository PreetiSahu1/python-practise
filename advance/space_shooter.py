import pygame
import random

# Initialize pygame
pygame.init()

# Screen settings
WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooter")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Player settings
player_x = WIDTH // 2
player_y = HEIGHT - 70
player_speed = 7

# Bullet settings
bullets = []
bullet_speed = 10

# Enemy settings
enemy_x = random.randint(0, WIDTH - 50)
enemy_y = 50
enemy_speed = 5

# Score
score = 0

# Font
font = pygame.font.SysFont(None, 36)

# Clock
clock = pygame.time.Clock()


# ---------------- FUNCTIONS ---------------- #

def draw_player(x, y):
    pygame.draw.rect(screen, WHITE, (x, y, 50, 50))


def move_player(x):
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= player_speed

    if keys[pygame.K_RIGHT]:
        x += player_speed

    # Prevent going outside screen
    x = max(0, min(WIDTH - 50, x))

    return x


def shoot_bullet():
    bullets.append([player_x + 20, player_y])


def move_bullets():
    for bullet in bullets:
        bullet[1] -= bullet_speed


def draw_bullets():
    for bullet in bullets:
        pygame.draw.rect(screen, RED, (bullet[0], bullet[1], 5, 10))


def remove_old_bullets():
    global bullets
    bullets = [b for b in bullets if b[1] > 0]


def draw_enemy(x, y):
    pygame.draw.rect(screen, RED, (x, y, 50, 50))


def move_enemy(y):
    y += enemy_speed

    if y > HEIGHT:
        y = 0

    return y


def check_collision():
    global enemy_x, enemy_y, score

    for bullet in bullets:

        if (enemy_x < bullet[0] < enemy_x + 50 and
                enemy_y < bullet[1] < enemy_y + 50):

            bullets.remove(bullet)

            score += 1

            enemy_x = random.randint(0, WIDTH - 50)
            enemy_y = 0


def draw_score():
    text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(text, (10, 10))


# ---------------- GAME LOOP ---------------- #

running = True

while running:

    clock.tick(60)

    screen.fill(BLACK)

    # Events
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_SPACE:
                shoot_bullet()

    # Update player
    player_x = move_player(player_x)

    # Update bullets
    move_bullets()

    remove_old_bullets()

    # Update enemy
    enemy_y = move_enemy(enemy_y)

    # Collision
    check_collision()

    # Draw everything
    draw_player(player_x, player_y)

    draw_bullets()

    draw_enemy(enemy_x, enemy_y)

    draw_score()

    pygame.display.update()

pygame.quit()