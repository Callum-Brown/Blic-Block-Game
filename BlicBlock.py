import pygame
import time
from threading import Timer

pygame.font.init()

WIDTH, HEIGHT = 600, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First Game!")

HEALTH_FONT = pygame.font.SysFont("comicsans", 40)
WIN_FONT = pygame.font.SysFont("cambria", 50)
COUNTDOWN_FONT = pygame.font.SysFont('cambria', 40)

PLAYER1 = pygame.Rect(40, 300, 10, 50)
PLAYER2 = pygame.Rect(560, 300, 10, 50)
BALL = pygame.Rect(400, 100, 10, 10)
FPS = 60
GREY = (100, 100, 100)
BLACK = (0,0,0)
WHITE = (255,255,255)
BALL_VEL_X = 5
BALL_VEL_Y = 5
PLAYER1_health = 2
PLAYER2_health = 2
PLAYER1_POINT = pygame.USEREVENT + 1
PLAYER2_POINT = pygame.USEREVENT + 2

def draw_winner(text):
    WIN_TEXT = WIN_FONT.render(text, 1, BLACK) ## fix draw winner function
    WIN.blit(WIN_TEXT, (125, 300))
    pygame.display.update()



def Ball_repositioner():
    global BALL_VEL_X
    BALL_VEL_X *= -1
    BALL.x = 300
    BALL.y = 50

def PLAYER1_movement(keys_pressed, PLAYER1):
    if keys_pressed[pygame.K_w] and PLAYER1.y - 5 > 0:  # up
        PLAYER1.y -= 5
    if keys_pressed[pygame.K_s] and PLAYER1.y < HEIGHT -10:  # down
        PLAYER1.y += 5

def PLAYER2_movement(keys_pressed, PLAYER2):
    if keys_pressed[pygame.K_UP] and PLAYER2.y - 5 > 0:  # up
        PLAYER2.y -= 5
    if keys_pressed[pygame.K_DOWN] and PLAYER2.y < HEIGHT -10:  # down
        PLAYER2.y += 5

def draw_window():
    WIN.fill(WHITE)
    PLAYER1_health_text = HEALTH_FONT.render("Health: " + str(PLAYER1_health), 1, BLACK)
    PLAYER2_health_text = HEALTH_FONT.render("Health: " + str(PLAYER2_health), 1, BLACK)
    WIN.blit(PLAYER1_health_text, (WIDTH - PLAYER1_health_text.get_width() - 10, 1))
    WIN.blit(PLAYER2_health_text, (10, 10))
    pygame.draw.rect(WIN, BLACK, PLAYER1)
    pygame.draw.rect(WIN, BLACK, PLAYER2)
    pygame.draw.rect(WIN, BLACK, BALL)
    pygame.display.update()

def main():
        global countdown
        global last_count
        global PLAYER1_health, PLAYER2_health
        global BALL_VEL_X, BALL_VEL_Y
        clock = pygame.time.Clock()
        run = True
        while run:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                if event.type == PLAYER1_POINT:
                    PLAYER1_health -= 1
                if event.type == PLAYER2_POINT:
                    PLAYER2_health -= 1

            BALL.x += BALL_VEL_X
            BALL.y += BALL_VEL_Y
            if BALL.y == 600:
                BALL_VEL_Y *= -1
            if BALL.y == 0:
                BALL_VEL_Y *= -1
            if BALL.x == 600:
                pygame.event.post(pygame.event.Event(PLAYER1_POINT))
                t = Timer(3, Ball_repositioner)
                t.start()
            if BALL.x == 0:
                pygame.event.post(pygame.event.Event(PLAYER2_POINT))
                t = Timer(3, Ball_repositioner)
                t.start()

                ## collisions BALL and PlAYER's
            collision_tolerance = 10
            if PLAYER1.colliderect(BALL):
                if abs(PLAYER1.top - BALL.bottom) < collision_tolerance and BALL_VEL_Y > 0:
                    BALL_VEL_Y *= -1
                if abs(PLAYER1.bottom - BALL.top) < collision_tolerance and BALL_VEL_Y < 0:
                    BALL_VEL_Y *= -1
                if abs(PLAYER1.right - BALL.left) < collision_tolerance and BALL_VEL_X < 0:
                    BALL_VEL_X *= -1
                if abs(PLAYER1.left - BALL.right) < collision_tolerance and BALL_VEL_X > 0:
                    BALL_VEL_X *= -1

            if PLAYER2.colliderect(BALL):
                if abs(PLAYER2.top - BALL.bottom) < collision_tolerance and BALL_VEL_Y > 0:
                    BALL_VEL_Y *= -1
                if abs(PLAYER2.bottom - BALL.top) < collision_tolerance and BALL_VEL_Y < 0:
                    BALL_VEL_Y *= -1
                if abs(PLAYER2.right - BALL.left) < collision_tolerance and BALL_VEL_X < 0:
                    BALL_VEL_X *= -1
                if abs(PLAYER2.left - BALL.right) < collision_tolerance and BALL_VEL_X > 0:
                    BALL_VEL_X *= -1


            winner_text = ""
            if PLAYER1_health <= 0:
                winner_text = "PLAYER1 WINS"

            if PLAYER2_health <= 0:
                winner_text = "PLAYER2 WINS"

            if winner_text != "":
                draw_winner(winner_text)
                break

            keys_pressed = pygame.key.get_pressed()
            PLAYER1_movement(keys_pressed, PLAYER1)
            PLAYER2_movement(keys_pressed, PLAYER2)
            draw_window()



        pygame.quit()
if __name__ == "__main__":
    main()
