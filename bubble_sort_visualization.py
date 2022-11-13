import pygame
import random
import copy
import time
pygame.init()
pygame.font.init()

WIDTH, HEIGHT = 1300, 700
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
FPS = 60
BAR_SPACE = 50
screen = pygame.display.set_mode((WIDTH, HEIGHT))

n_of_objects = 50
x_pos = WIDTH/n_of_objects
size  = x_pos -5

def bubble_sort(numbers):
    j = 1
    prohozeni = True
    while prohozeni:
        prohozeni = False
        for i in range(len(numbers) - j):
            if numbers[i] > numbers[i+1]:
                temp = numbers[i]
                numbers[i] = numbers[i + 1]
                numbers[i + 1] = temp
                prohozeni = True
                draw_rects()
        j +=1
    return numbers


def draw():
    #Upper and lower bar
    pygame.draw.line(screen, WHITE, (0, BAR_SPACE), (WIDTH, BAR_SPACE))
    pygame.draw.line(screen, WHITE, (0, HEIGHT - BAR_SPACE), (WIDTH, HEIGHT - BAR_SPACE))
    #description of controlling
    font = pygame.font.SysFont("comicsans", 25)
    space_text = font.render("SPACE to start", 1, WHITE)
    e_text = font.render("R to restart", 1, WHITE)
    r_text = font.render("E to spawn new num", 1, WHITE)
    t_text = font.render("T to change speed" + "(" + str(speed_choice) + ")", 1, WHITE)

    y_pos = 25/2
    SPACE = 25
    screen.blit(space_text, (0,y_pos))
    screen.blit(e_text, (0 + 120 + SPACE,y_pos))
    screen.blit(r_text, (0 + 120 + 92 + SPACE *2 ,y_pos))
    screen.blit(t_text, (0 + 120 + 92 + 167 + SPACE *3 ,y_pos))




def draw_rects():
    screen.fill(BLACK)

    for i in range(n_of_objects):
        pygame.draw.rect(screen, WHITE, (i*x_pos, BAR_SPACE, size, numbers[i] ))
    
    draw()
    time.sleep(speed)
    pygame.display.update()



#def main():
run = True
numbers = []
original_numbers = []
speed_choice = 1
speed = 0
allow = True
clock = pygame.time.Clock()

while run:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_SPACE:
                original_numbers = copy.copy(numbers)
                numbers = bubble_sort(numbers)
                


            if event.key == pygame.K_e:
                numbers = []
                if len(numbers) == 0:
                    for i in range(260):
                        r_number = random.randrange(5,600)           
                        numbers.append(r_number)

            if event.key == pygame.K_r:
                numbers = original_numbers

            if event.key == pygame.K_t:
                speed_choice +=1

                if speed_choice ==1:
                    speed = 0.01
                if speed_choice ==2:
                    speed = 0.02
                if speed_choice ==3:
                    speed = 0.03
                if speed_choice ==4:
                    speed_choice = 1
                    speed = 0            

    if len(numbers) == 0:
        for i in range(n_of_objects):
            r_number = random.randrange(5,600)           
            numbers.append(r_number) 
    
    draw_rects()