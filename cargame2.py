import pygame
import time
import random

#initiating pygame
pygame.init()

#Display window with frame 600 to 600
display_width = 600
display_height = 600

#car width and height from the image
car_width=65
car_height=113

#color
black = (0,0,0)
white = (255,255,255)

gameDisplay = pygame.display.set_mode((display_width,display_height))

#window name
pygame.display.set_caption('Race Mania')

clock = pygame.time.Clock()

# Background image of the road
background_image = pygame.image.load('road.png')

#image of the car
carImg = pygame.image.load('racecarr.png')

#image of the enemy car
enemycarImg = pygame.image.load('car.png')

#image of the road
roadImg = pygame.image.load('road.png')

def dodged_blocks(count):
    font = pygame.font.SysFont(None,50)
    text = font.render("Dodged:"+str(count),True,white)
    gameDisplay.blit(text,(0,0))

def road(x,y):
    gameDisplay.blit(roadImg,(x,y))

def enemycar(x,y):
    gameDisplay.blit(enemycarImg,(x,y))
    
def car(x,y):
    gameDisplay.blit(carImg,(x,y))

def text_objects(text, font):
    textSurface = font.render(text,True,black)
    return textSurface,textSurface.get_rect()

def message_display(text):
    largeText=pygame.font.Font('freesansbold.ttf',100)
    TextSurf,TextRect = text_objects(text,largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf,TextRect)
    pygame.display.update()
    time.sleep(2)
    game_loop()

def crash():
    message_display('You Crashed')

#Game Loop function
    
def game_loop():
    x = (display_width * 0.45)
    y = (display_height * .8)

    gameexit = False

    x_change=0
    
    block_x=random.randrange(0,display_width-100)
    block_y=-600
    block_speed=8
    block_h=90
    block_w=40
    dodged=0

    road_x=0
    road_y=0
    road_y_2=-600
    road_speed=7

    
    while not gameexit:
        #list of event that happened in the game , like mouse click or arrow clicked
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               pygame.quit()
               quit()

            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    x_change=-5
                elif event.key==pygame.K_RIGHT:
                    x_change=5

            if event.type == pygame.KEYUP:
                if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                    x_change=0


        #road function
        road(road_x,road_y)

        road_y=(road_y+road_speed)%600

        road(road_x,road_y_2)

        road_y_2=(road_y_2+road_speed)%(-600)




        x+=x_change       
        #gameDisplay.blit(background_image,[0,0])

        #enemy car function
        enemycar(block_x,block_y)

        #speeding up the car
        block_y=block_y+block_speed

        # Number of cars dodged
        dodged_blocks(dodged)

        #car function
        car(x,y)

        
        if x>display_width-car_width or x<0:
            crash()

        if block_y>display_height:
            block_y = -block_h
            block_x = random.randrange(0,display_width-100)
            dodged+=1
            block_speed+=1

        if y <block_y + block_h:

            if x>block_x and x < block_x + block_w or x+car_width>block_x and x+car_width<block_x +block_w:
                crash()

        pygame.display.update()
        
        #frames per second
        clock.tick(60)

game_loop()
pygame.quit()
quit()
