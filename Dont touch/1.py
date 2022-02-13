import pygame
pygame.init()

#definir éléments (couleur, taille ecrans, nom du jeu et le temps)
gray=(119,118,110) #couleurs préconfigurées pour etre réutiliser
black=(0,0,0)
red=(255,0,0)
green=(170, 219, 170)
blue=(170, 170, 230)
bright_red=(255,0,0)
bright_green=(237, 245, 237)
bright_blue=(117, 117, 184)
display_width=800
display_height=600
import time
import random


gamedisplays=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Dont touch")
clock=pygame.time.Clock()
carimg=pygame.image.load('rollerman.png') #charger img joueur
backgroundpic=pygame.image.load("download12.jpg") #mettre en place images de fond
yellow_strip=pygame.image.load("yellow strip.jpg") #trait blanc route img
strip=pygame.image.load("strip.jpg") #ligne bordure route img
intro_background=pygame.image.load("background.jpg") #img menu
instruction_background=pygame.image.load("background2.jpg") #img instructions
car_width=56 #largeur voiture
pause=False #le jeu ne commence pas en pause

#Boucle intro
def intro_loop():
    intro=True
    while intro:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()

        #Aficher menu principal
        gamedisplays.blit(intro_background,(0,0))
        largetext=pygame.font.Font('freesansbold.ttf',115)
        TextSurf,TextRect=text_objects("DONT TOUCH",largetext)
        TextRect.center=(400,80)
        gamedisplays.blit(TextSurf,TextRect)
        button("COMMENCER",120,520,150,50,green,bright_green,"play")
        button("QUITTER",550,520,100,50,green,bright_green,"quit")
        button("INSTRUCTIONS",315,520,180,50,green,bright_green,"intro")
        pygame.display.update()
        clock.tick(50)

#definir bouton
def button(msg,x,y,w,h,ic,ac,action=None):
    mouse=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    if x+w>mouse[0]>x and y+h>mouse[1]>y:
        pygame.draw.rect(gamedisplays,ac,(x,y,w,h))
        if click[0]==1 and action!=None:
            if action=="play":
                countdown()
            elif action=="quit":
                pygame.quit()
                quit()

            elif action=="intro":
                introduction()
            elif action=="menu":
                intro_loop()
            elif action=="pause":
                paused()
            elif action=="unpause":
                unpaused()


    else:
        pygame.draw.rect(gamedisplays,ic,(x,y,w,h))
    smalltext=pygame.font.Font("freesansbold.ttf",20)
    textsurf,textrect=text_objects(msg,smalltext)
    textrect.center=((x+(w/2)),(y+(h/2)))
    gamedisplays.blit(textsurf,textrect)

#Instruction
def introduction():
    introduction=True
    while introduction:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()

        #Contenus d'instruction
        gamedisplays.blit(instruction_background,(0,0))
        largetext=pygame.font.Font('freesansbold.ttf',80)
        smalltext=pygame.font.Font('freesansbold.ttf',20)
        mediumtext=pygame.font.Font('freesansbold.ttf',40)
        textSurf,textRect=text_objects("Eviter les gens!",smalltext)
        textRect.center=((260),(180))
        TextSurf,TextRect=text_objects("INSTRUCTIONS",mediumtext)
        TextRect.center=((260),(130))
        gamedisplays.blit(TextSurf,TextRect)
        gamedisplays.blit(textSurf,textRect)
        stextSurf,stextRect=text_objects("Flèche de droite : tourner à droite",smalltext)
        stextRect.center=((240),(300))
        hTextSurf,hTextRect=text_objects("Flèche de gauche : tourner à gauche" ,smalltext)
        hTextRect.center=((237),(350))
        atextSurf,atextRect=text_objects("A : ACCELERATION",smalltext)
        atextRect.center=((250),(400))
        rtextSurf,rtextRect=text_objects("B : FREINER ",smalltext)
        rtextRect.center=((250),(450))
        ptextSurf,ptextRect=text_objects("P : PAUSE  ",smalltext)
        ptextRect.center=((250),(500))
        sTextSurf,sTextRect=text_objects("CONTROLES",mediumtext)
        sTextRect.center=((250),(250))
        gamedisplays.blit(sTextSurf,sTextRect)
        gamedisplays.blit(stextSurf,stextRect)
        gamedisplays.blit(hTextSurf,hTextRect)
        gamedisplays.blit(atextSurf,atextRect)
        gamedisplays.blit(rtextSurf,rtextRect)
        gamedisplays.blit(ptextSurf,ptextRect)
        button("RETOUR",600,450,100,50,blue,bright_blue,"menu")
        pygame.display.update()
        clock.tick(30)

#definir pause
def paused():
    global pause

    while pause:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    quit()

            gamedisplays.blit(instruction_background,(0,0))
            largetext=pygame.font.Font('freesansbold.ttf',115)
            TextSurf,TextRect=text_objects("PAUSE",largetext)
            TextRect.center=((display_width/2),(display_height/2))
            gamedisplays.blit(TextSurf,TextRect)
            button("CONTINUER",150,450,150,50,green,bright_green,"unpause")
            button("RECOMMENCER",350,450,150,50,blue,bright_blue,"play")
            button("MENU PRINCIPAL",550,450,200,50,red,bright_red,"menu")
            pygame.display.update()
            clock.tick(30)

#definir sortie de pause
def unpaused():
    global pause
    pause=False

#definir éléments de fond du jeu
def countdown_background():
    font=pygame.font.SysFont(None,25)
    x=(display_width*0.45)
    y=(display_height*0.8)
    gamedisplays.blit(backgroundpic,(0,0))
    gamedisplays.blit(backgroundpic,(0,200))
    gamedisplays.blit(backgroundpic,(0,400))
    gamedisplays.blit(backgroundpic,(700,0))
    gamedisplays.blit(backgroundpic,(700,200))
    gamedisplays.blit(backgroundpic,(700,400))
    gamedisplays.blit(yellow_strip,(400,100))
    gamedisplays.blit(yellow_strip,(400,200))
    gamedisplays.blit(yellow_strip,(400,300))
    gamedisplays.blit(yellow_strip,(400,400))
    gamedisplays.blit(yellow_strip,(400,100))
    gamedisplays.blit(yellow_strip,(400,500))
    gamedisplays.blit(yellow_strip,(400,0))
    gamedisplays.blit(yellow_strip,(400,600))
    gamedisplays.blit(strip,(120,200))
    gamedisplays.blit(strip,(120,0))
    gamedisplays.blit(strip,(120,100))
    gamedisplays.blit(strip,(680,100))
    gamedisplays.blit(strip,(680,0))
    gamedisplays.blit(strip,(680,200))
    gamedisplays.blit(carimg,(x,y))
    text=font.render("ESQUIVES: 0",True, black)
    score=font.render("SCORE: 0",True,red)
    gamedisplays.blit(text,(0,50))
    gamedisplays.blit(score,(0,30))
    button("PAUSE",650,0,150,50,blue,bright_blue,"pause")

#Lancer le compteur
def countdown():
    countdown=True

    while countdown:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    quit()

            #Contenus de la partie
            gamedisplays.fill(gray)
            countdown_background()
            largetext=pygame.font.Font('freesansbold.ttf',115)
            TextSurf,TextRect=text_objects("3",largetext)
            TextRect.center=((display_width/2),(display_height/2))
            gamedisplays.blit(TextSurf,TextRect)
            pygame.display.update()
            clock.tick(1)
            gamedisplays.fill(gray)
            countdown_background()
            largetext=pygame.font.Font('freesansbold.ttf',115)
            TextSurf,TextRect=text_objects("2",largetext)
            TextRect.center=((display_width/2),(display_height/2))
            gamedisplays.blit(TextSurf,TextRect)
            pygame.display.update()
            clock.tick(1)
            gamedisplays.fill(gray)
            countdown_background()
            largetext=pygame.font.Font('freesansbold.ttf',115)
            TextSurf,TextRect=text_objects("1",largetext)
            TextRect.center=((display_width/2),(display_height/2))
            gamedisplays.blit(TextSurf,TextRect)
            pygame.display.update()
            clock.tick(1)
            gamedisplays.fill(gray)
            countdown_background()
            largetext=pygame.font.Font('freesansbold.ttf',115)
            TextSurf,TextRect=text_objects("C'EST PARTI!",largetext)
            TextRect.center=((display_width/2),(display_height/2))
            gamedisplays.blit(TextSurf,TextRect)
            pygame.display.update()
            clock.tick(1)
            game_loop()

#definir obstacles
def obstacle(obs_startx,obs_starty,obs):
    if obs==0:
        obs_pic=pygame.image.load("car.png")
    elif obs==1:
        obs_pic=pygame.image.load("car1.png")
    elif obs==2:
        obs_pic=pygame.image.load("car2.png")
    elif obs==3:
        obs_pic=pygame.image.load("car4.png")
    elif obs==4:
        obs_pic=pygame.image.load("car5.png")
    elif obs==5:
        obs_pic=pygame.image.load("car6.png")
    elif obs==6:
        obs_pic=pygame.image.load("car7.png")
    gamedisplays.blit(obs_pic,(obs_startx,obs_starty))

#definir le systeme de score
def score_system(passed,score):
    font=pygame.font.SysFont(None,25)
    text=font.render("Equives:"+str(passed),True,black)
    score=font.render("Score:"+str(score),True,red)
    gamedisplays.blit(text,(0,50))
    gamedisplays.blit(score,(0,30))

#mettre le texte sur la surface et definir couleur texte
def text_objects(text,font):
    textsurface=font.render(text,True,black)
    return textsurface,textsurface.get_rect()

#ligne bordure route img
def message_display(text):
    largetext=pygame.font.Font("freesansbold.ttf",80)
    textsurf,textrect=text_objects(text,largetext)
    textrect.center=((display_width/2),(display_height/2))
    gamedisplays.blit(textsurf,textrect)
    pygame.display.update()
    time.sleep(3)
    game_loop()

#initier message lors de crash
def crash():
    message_display("CONTAGIEUX !")

#mise en place img de fond
def background():

    # la pelouse
    gamedisplays.blit(backgroundpic,(0,0))
    gamedisplays.blit(backgroundpic,(0,200))
    gamedisplays.blit(backgroundpic,(0,400))
    gamedisplays.blit(backgroundpic,(700,0))
    gamedisplays.blit(backgroundpic,(700,200))
    gamedisplays.blit(backgroundpic,(700,400))

    # lignes blanches
    gamedisplays.blit(yellow_strip,(400,0))
    gamedisplays.blit(yellow_strip,(400,100))
    gamedisplays.blit(yellow_strip,(400,200))
    gamedisplays.blit(yellow_strip,(400,300))
    gamedisplays.blit(yellow_strip,(400,400))
    gamedisplays.blit(yellow_strip,(400,500))

    # bordures route
    gamedisplays.blit(strip,(120,0))
    gamedisplays.blit(strip,(120,100))
    gamedisplays.blit(strip,(120,200))
    gamedisplays.blit(strip,(680,0))
    gamedisplays.blit(strip,(680,100))
    gamedisplays.blit(strip,(680,200))

#definir image joueur dans la fenetre (position et surface par axe x et y)
def car(x,y):
    gamedisplays.blit(carimg,(x,y))

#definir la boucle du jeu
def game_loop():
    global pause
    x=(display_width*0.45) #position x
    y=(display_height*0.8) #position y
    x_change=0#pour definir que le mouvement de la voiture se fait que sur l'axe x et 0 = position initiale
    obstacle_speed=9
    obs=0
    y_change=0
    obs_startx=random.randrange(200,(display_width-200))
    obs_starty=-750
    obs_width=56
    obs_height=125
    passed=0
    level=0
    score=0
    y2=7
    fps=120

    bumped=False #bumped = crash (heurté) = desactivé
    while not bumped:
        for event in pygame.event.get():
            if event.type==pygame.QUIT: #Pour que le script s'arrete lors du départ du joueur
                pygame.quit()
                quit()

            # Controle joueur via un event et via la methode KEYDOWN de pygame
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    x_change=-5
                if event.key==pygame.K_RIGHT:
                    x_change=5
                if event.key==pygame.K_a:
                    obstacle_speed+=2
                if event.key==pygame.K_b:
                    obstacle_speed-=2
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                    x_change=0

        x+=x_change #Ajoute une valeur et la variable et affecte le résultat à cette variable.
        pause=True
        gamedisplays.fill(gray) #Remplir ecran en gray

        #Chargement des images pour donner l'impression d'avancer sur la route
        rel_y=y2%backgroundpic.get_rect().width
        gamedisplays.blit(backgroundpic,(0,rel_y-backgroundpic.get_rect().width))
        gamedisplays.blit(backgroundpic,(700,rel_y-backgroundpic.get_rect().width))
        if rel_y<800:
            gamedisplays.blit(backgroundpic,(0,rel_y))
            gamedisplays.blit(backgroundpic,(700,rel_y))
            gamedisplays.blit(yellow_strip,(400,rel_y))
            gamedisplays.blit(yellow_strip,(400,rel_y+100))
            gamedisplays.blit(yellow_strip,(400,rel_y+200))
            gamedisplays.blit(yellow_strip,(400,rel_y+300))
            gamedisplays.blit(yellow_strip,(400,rel_y+400))
            gamedisplays.blit(yellow_strip,(400,rel_y+500))
            gamedisplays.blit(yellow_strip,(400,rel_y-100))
            gamedisplays.blit(strip,(120,rel_y-200))
            gamedisplays.blit(strip,(120,rel_y+20))
            gamedisplays.blit(strip,(120,rel_y+30))
            gamedisplays.blit(strip,(680,rel_y-100))
            gamedisplays.blit(strip,(680,rel_y+20))
            gamedisplays.blit(strip,(680,rel_y+30))

        y2+=obstacle_speed



        #obstacle et systeme/conditions de point lié à ce dernier
        obs_starty-=(obstacle_speed/4) #vitesse voiture obstacle
        obstacle(obs_startx,obs_starty,obs)
        obs_starty+=obstacle_speed
        car(x,y)
        score_system(passed,score)
        if x>690-car_width or x<110:  #definir limite de la voiture sur la route largeur
            crash()  #lancer fonction crash si on ne l'a respecte pas
        if x>display_width-(car_width+110) or x<110:
            crash()
        if obs_starty>display_height:
            obs_starty=0-obs_height
            obs_startx=random.randrange(170,(display_width-170))
            obs=random.randrange(0,7)
            passed=passed+1
            score=passed*10
            if int(passed)%10==0:
                level=level+1
                obstacle_speed+2
                largetext=pygame.font.Font("freesansbold.ttf",80)
                textsurf,textrect=text_objects("NIVEAU"+str(level),largetext)
                textrect.center=((display_width/2),(display_height/2))
                gamedisplays.blit(textsurf,textrect)
                pygame.display.update()
                time.sleep(3)

        #En cas de crash (echec)
        if y<obs_starty+obs_height:
            if x > obs_startx and x < obs_startx + obs_width or x+car_width > obs_startx and x+car_width < obs_startx+obs_width:
                crash()
        button("Pause",650,0,150,50,blue,bright_blue,"pause")
        pygame.display.update()
        clock.tick(60)
intro_loop()

#Lancer la boucle
game_loop()

#quitter jeu
pygame.quit()
quit()
