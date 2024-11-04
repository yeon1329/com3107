import pygame
import time

pygame.init()

# functions
def message(fonts, msg, color, posx, posy):
    mesg = fonts.render(msg, True, color)
    mesg_Rect = mesg.get_rect()
    mesg_Rect.centerx = posx
    mesg_Rect.centery = posy
    screen.blit(mesg, mesg_Rect)
clock = pygame.time.Clock()

#Fonts
font_gameOver = pygame.font.SysFont(None, 50)
font_madeBy = pygame.font.SysFont(None, 20)

#color
BLUE = (0,0,255); RED = (255,0,0); WHITE = (255,255,255)
BLACK = (0,0,0); GRAY = (127,127,127)

#screen
SCR_WIDTH, SCR_HEIGHT = 800,600
screen = pygame.display.set_mode((SCR_WIDTH, SCR_HEIGHT))
pygame.display.set_caption("Snake Game ver 1.0")

#snake
snake_size = 20
snake_pos_x = int(SCR_WIDTH/2 - snake_size/2)
snake_pos_y = int(SCR_HEIGHT/2 - snake_size/2)
snake_posx_change = 0
snake_posy_change = 0

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
                
    snake_pos_x += snake_posx_change
    snake_pos_y += snake_posy_change
    if snake_pos_x >= (SCR_WIDTH - snake_size) or snake_pos_x - (snake_size/2) < 0 \
       or snake_pos_y >= (SCR_HEIGHT - snake_size) or snake_pos_y - (snake_size/2) < 0:
       running = False
       
    screen.fill(WHITE)
    pygame.draw.rect(screen, GRAY, [0,0,SCR_WIDTH, SCR_HEIGHT],10)
    pygame.draw.rect(screen, BLUE, [snake_pos_x,snake_pos_y,snake_size,snake_size])
    pygame.display.flip()
    clock.tick(30)
                            
    pygame.draw.rect(screen, BLUE, [int(SCR_WIDTH/2 - snake_size/2), \
                                    int(SCR_HEIGHT/2 - snake_size/2), \
                                    snake_size, snake_size])
    pygame.display.update()

    message(font_gameOver, 'Game Over', RED, int(SCR_WIDTH/2), int(SCR_HEIGHT/2))
    message(font_madeBy, 'made by yeon1329', GRAY, int(SCR_WIDTH/2), int(SCR_HEIGHT/2) + 30)
    pygame.display.update()
    time.sleep(2)
pygame.quit()
