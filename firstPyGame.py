import pygame
pygame.init()

screenWidth = 800
screenHeight = 480

win = pygame.display.set_mode((screenWidth, screenHeight))

pygame.display.set_caption("First Game")

walk_left = [pygame.image.load('images/left_run_1.png'),pygame.image.load('images/left_run_2.png'),pygame.image.load('images/left_run_3.png')]
walk_right = [pygame.image.load('images/right_run_1.png'),pygame.image.load('images/right_run_2.png'),pygame.image.load('images/right_run_3.png')]
bg = pygame.image.load('images/bg.png')
charLeft = pygame.image.load('images/left_stand.png')
charRight = pygame.image.load('images/right_stand.png')

x = 50
y = 440
width = 32
height = 32
vel = 10
isJump = False
jumpCount = 7
left = False
right = False
walkCount = 0

def redrawGameWindow():
    global walkCount

    win.blit(bg, (0,0))
    pygame.draw.circle(win, (255,0,0), (x,y),width)
    pygame.display.update()

#mainloop

run = True
while run:
    pygame.time.delay(20)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        if x > 0:
            x -= vel
            left = True
            right = False
    elif keys[pygame.K_RIGHT]:
        if x < screenWidth - width:
            x += vel
            left = False
            right = True
    else:
            left = False
            right = False
            walkCount = 0


    if not(isJump):
        if keys[pygame.K_UP]:
            isJump = True
    else:
        if jumpCount >= -7:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y-= (jumpCount ** 2) * neg
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 7
            
    redrawGameWindow()

pygame.quit()
