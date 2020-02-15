import pygame
from pygame.locals import*
from random import randint

pygame.init()
fenetre = pygame.display.set_mode((715, 610))
pygame.display.set_caption("Main Menu")
img = pygame.image.load("img/menu.jpg")
img = pygame.transform.scale(img,(300,200))
fenetre.fill((0, 0, 0))
bleu = (121, 248, 248)
blanc = (255,215,0)
rect1=(330, 300, 100, 50)
bouton1 = pygame.draw.rect(fenetre,bleu,rect1,0)
rect2=(330, 370, 100, 50)
bouton2 = pygame.draw.rect(fenetre,bleu,rect2,0)

play = pygame.font.Font(None, 30)
label_play = play.render("PLAY", 1, blanc)
fenetre.blit(label_play, (355,318))
quit = pygame.font.Font(None, 30)
label_quit= quit.render("QUIT", 1, blanc)
fenetre.blit(label_quit, (355,388))
fenetre.blit(img, (230,30))
pygame.display.flip()

go = True
while go == True:
    for event in pygame.event.get():
        if event.type == MOUSEBUTTONUP and event.button == 1 and 330<event.pos[0]<430 and 300<event.pos[1]<350:
            pygame.init()
            fenetre = pygame.display.set_mode((800, 650))
            fond = pygame.image.load("img/background.png")
            police = pygame.font.SysFont("arail", 32)
            pygame.display.set_caption("DuckHunt")
            duck = pygame.image.load("img/oiseau/third.png")
            time = pygame.time.Clock()
            duck2 = pygame.image.load("img/all.png")
            rect_duck2 = duck2.get_rect()
            rect_sprite = pygame.Rect(0, 0, 96, 96)
            pos_x = 0
            pos_y = 50
            win = 0
            fail = 3

            bye = False
            while bye == False:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        bye = True
                mouse_x, mouse_y = pygame.mouse.get_pos()
                
                if (mouse_x >= pos_x and mouse_x <= pos_x + 110 and mouse_y >= pos_y and mouse_y <= pos_y + 110 and pygame.mouse.get_pressed()[0] is 1):   
                    pos_x=0
                    pos_y=randint(50, 650-110)
                    win += 1
                pos_x += 1     
                if pos_x >= 800:         
                    pos_x = -300         
                    pos_y = randint(50, 650 - 110)
                    fail -= 1

                if fail <= 0:
                    bye = True
                
                font=pygame.font.Font(None, 24)
                wint = font.render("Canards Tués !",1,(255,255,255))
                failt = font.render("Vies !",1,(255,255,255))
                text_win = police.render(str(win), 3, (255, 255, 255)) 
                text_fail =  police.render(str(fail), 3, (255, 255, 255)) 
                time.tick(60)
                fenetre.blit(fond,(0,50))
                fenetre.blit(wint, (60, 14))
                fenetre.blit(failt, (550, 14))
                fenetre.blit(duck, (pos_x, pos_y))
                fenetre.blit(text_win, (10, 10))     
                fenetre.blit(text_fail, (500, 10)) 
                pygame.display.update() 
            pygame.quit()
            quit()
        if event.type == MOUSEBUTTONUP and event.button == 1 and 330<event.pos[0]<430 and 370<event.pos[1]<420:
            go = False

pygame.quit()
quit()