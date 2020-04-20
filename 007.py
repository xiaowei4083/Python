import pygame
pygame.init()
screen=pygame.display.set_mode([800,600])
pygame.display.set_caption("阻挡球")
keepGoing=True
pic=pygame.image.load("timg.bmp")
colorkey=pic.get_at((0,0))
pic.set_colorkey(colorkey)
picx=0
picy=0
BLACK=(0,0,0)
WHITE=(255,255,255)
time=pygame.time.Clock()
speedx=5
speedy=5
paddLew=200
paddLeh=25
paddLex=300
paddLey=550
picw=100
pich=100
points=0
lives=5
font=pygame.font.SysFont("Time",24)

while keepGoing:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            keepGoing=False
    picx +=speedx
    picy +=speedy

    if picx <=0 or picx + pic.get_width() >=800:
        speedx= -speedx
    if picy <=0:
        speedy= -speedy

    if picy >=500:
        lives -=1
        speedy= -speedy

    screen.fill(BLACK)
    screen.blit(pic,(picx,picy))

    paddLex=pygame.mouse.get_pos()[0]
    paddLex -=paddLew/2
    pygame.draw.rect(screen,WHITE,(paddLex,paddLey,paddLew,paddLeh))

    if picy + pich >=paddLey and picy + pich <= paddLey + paddLeh \
        and speedy > 0:
        if picx + picw / 2 >=paddLex and picx + picw /2 <= paddLex + \
            paddLew:
            points +=1
            speedy= -speedy

    draw_string="Live:" + str(lives) + " Points:" + str(points)
    if lives <=0:
        keepGoing=False


    text=font.render(draw_string,True,WHITE)
    text_rect=text.get_rect()
    text_rect.centerx=screen.get_rect().centerx
    text_rect.y=10
    screen.blit(text,text_rect)
    pygame.display.update()
    time.tick(60)

pygame.quit()