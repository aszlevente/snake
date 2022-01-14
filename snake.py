import pygame
import random
import time

pygame.init()

screen = pygame.display.set_mode((800, 600))

def gameOver() :
    screen.fill((0,0,0))
    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render('GAME OVER', True, (255,255,255), (0,0,0))
    textRect = text.get_rect()
    textRect.center = (800 // 2, 600 // 2)
    screen.blit(text,textRect)
    pygame.display.flip()
    time.sleep(3)
    pygame.quit()

d = 20
snake = [(10,10),(9,10),(8,10),(7,10),(6, 10)]
speed = 8
direction = 1 #0, 1, 2, 3 => up, right, down, left

foodPos = (random.randint(0,800/d-1),random.randint(0,600/d-1))
while True:
    screen.fill((0,0,0))
    
    for e in pygame.event.get():
        if e.type == pygame.QUIT :
            pygame.quit()

        if e.type == pygame.KEYDOWN :
            
            if e.key == pygame.K_LEFT and direction != 1:
                direction = 3
            elif e.key == pygame.K_RIGHT and direction != 3 :
                direction = 1
            elif e.key == pygame.K_UP and direction != 2 :
                direction = 0
            elif e.key == pygame.K_DOWN and direction != 0 :
                direction = 2

    #számolás, rajzolás
    for pos in snake :
        
        # snake body
        pygame.draw.rect(screen, (255,255,255) , pygame.Rect(pos[0]*d, pos[1]*d, d, d))

        # food
        pygame.draw.rect(screen, (255,0,0) , pygame.Rect(foodPos[0]*d, foodPos[1]*d, d, d))

        # mozgás
        if snake.index(pos) == 0 :
            if direction == 0 :
                newPos = (pos[0],pos[1]-1)
                snake[snake.index(pos)] = (pos[0],pos[1]-speed)
            elif direction == 2 :
                snake[snake.index(pos)] = (pos[0],pos[1]+speed)
                newPos = (pos[0],pos[1]+1)
            elif direction == 1 :
                snake[snake.index(pos)] = (pos[0]+speed,pos[1])
                newPos = (pos[0]+1,pos[1])
            elif direction == 3 :
                snake[snake.index(pos)] = (pos[0]-speed,pos[1])
                newPos = (pos[0]-1,pos[1])

            snake.pop(0)
            if pos in snake :
                gameOver()
            snake.insert(0,newPos)

            if pos[0]<0 or pos[0]>(800//d) or pos[1]<0 or pos[1]>(600/d) :
                gameOver()

            if pos == foodPos :
                foodPos = (random.randint(0,800/d-1),random.randint(0,600/d-1))
                if snake[-1][0]<snake[-2][0] :
                    snake.append((snake[-1][0]-1,snake[-1][1]))
                elif snake[-1][0]>snake[-2][0] :
                    snake.append((snake[-1][0]+1,snake[-1][1]))
                elif snake[-1][1]<snake[-2][1] :
                    snake.append((snake[-1][0]-1,snake[-1][1]))
                elif snake[-1][1]>snake[-2][1] :
                    snake.append((snake[-1][0]+1,snake[-1][1]))
        else :
            snake[snake.index(pos)] = (prevPos[0],prevPos[1])
        
        prevPos = pos
    #megjelenítés
                
    pygame.display.flip()
    time.sleep(1/speed)
    

