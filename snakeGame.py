import pygame
import time

def message(fonts, msg, color, posx, posy):
    mesg = fonts.render(msg, True, color)
    mesg_Rect = mesg.get_rect()
    mesg_Rect.centerx = posx
    mesg_Rect.centery = posy
    screen.blit(mesg, mesg_Rect)

pygame.init()
clock = pygame.time.Clock()
#Fonts
font_gameOver = pygame.font.SysFont(None, 50)
font_madeBy = pygame.font.SysFont(None, 20)

#color
RED = (255,0,0); GREEN = (0,255,0)
BLUE = (0,0,255); WHITE = (255,255,255)
BLACK = (0,0,0)
#screen
SCR_WIDTH, SCR_HEIGHT = 800,600

#snake
SNAKE_SIZE = 20
snake_pos_x  = SCR_WIDTH/2 - SNAKE_SIZE/2
snake_pos_y  = SCR_HEIGHT/2 - SNAKE_SIZE/2
snake_posx_change = 0
snake_posy_change = 0

screen = pygame.display.set_mode((SCR_WIDTH, SCR_HEIGHT))
pygame.display.set_caption("Snake Game ver 1.0")


running = True
while running:
    for event in pygame.event.get() :
        #print(event)
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake_posx_change = 0
                snake_posy_change = -10
            if event.key == pygame.K_DOWN:
                snake_posx_change = 0
                snake_posy_change = 10
            if event.key == pygame.K_LEFT:
                snake_posx_change = -10
                snake_posy_change = 0
            if event.key == pygame.K_RIGHT:
                snake_posx_change = 10
                snake_posy_change = 0
    if snake_pos_x >= (SCR_WIDTH - SNAKE_SIZE) or \
       snake_pos_x - (SNAKE_SIZE/2) < 0 or \
       snake_pos_y >= (SCR_HEIGHT - SNAKE_SIZE) or \
       snake_pos_y - (SNAKE_SIZE/2) < 0 :
        running = False       
                
    snake_pos_x += snake_posx_change
    snake_pos_y += snake_posy_change
    screen.fill(WHITE)

    pygame.draw.rect(screen, BLACK, [0,0, SCR_WIDTH, SCR_HEIGHT],10)
    pygame.draw.rect(screen, RED, [snake_pos_x,
                            snake_pos_y,
                            SNAKE_SIZE,
                            SNAKE_SIZE])

    
    pygame.display.update()
    clock.tick(60)
message(font_gameOver, 'Game Over', RED, int(SCR_WIDTH/2), int(SCR_HEIGHT/2))
message(font_madeBy, 'made by kig2929kig', BLACK, int(SCR_WIDTH/2), int(SCR_HEIGHT/2)+30)
pygame.display.update()
time.sleep(2)
pygame.quit()
