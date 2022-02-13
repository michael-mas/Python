#importer lib
import pygame
import math
import random


#initier pygame
pygame.init()

#taille canva
sw = 1200
sh = 800

#importer img
bg = pygame.image.load('Pics/starbg.png')
alienImg = pygame.image.load('Pics/alienShip.png')
playerRocket = pygame.image.load('Pics/bigcat.png')
star = pygame.image.load('Pics/fish.png')
asteroid50 = pygame.image.load('Pics/minidog.png')
asteroid100 = pygame.image.load('Pics/mediumdog.png')
asteroid150 = pygame.image.load('Pics/bigdog.png')

#affecter son et parametrer volume
shoot = pygame.mixer.Sound('sounds/shoot.wav')
bangLargeSound = pygame.mixer.Sound('sounds/bigwouf.wav')
bangSmallSound = pygame.mixer.Sound('sounds/smallwouf.wav')
shoot.set_volume(.25)
bangLargeSound.set_volume(.25)
bangSmallSound.set_volume(.25)

#activer le jeu et la fentre
pygame.display.set_caption('Asteroids') #activer asteroides
win = pygame.display.set_mode((sw, sh)) #activer la fenetre (sw = surface width, sh = surface height)
clock = pygame.time.Clock() #créer un objet pour aider à suivre le temps

#parametre joueur de base
gameover = False
lives = 4
score = 0
rapidFire = False
rfStart = -1
isSoundOn = True
highScore = 0

#parametre taille/image avatar du joueur
class Player(object):
    def __init__(self): #instruction sur self via l'bjet joueur
        self.img = playerRocket #img
        self.w = self.img.get_width() #taille à celle de l'image
        self.h = self.img.get_height() #taille à celle de l'image
        self.x = sw//2 # floor division pour placer le vaisseau
        self.y = sh//2 # floor division pour placer le vaisseau
        self.angle = 0 #angle position de départ
        self.rotatedSurf = pygame.transform.rotate(self.img, self.angle) #mouvement
        self.rotatedRect = self.rotatedSurf.get_rect()
        self.rotatedRect.center = (self.x, self.y)
        self.cosine = math.cos(math.radians(self.angle + 90))
        self.sine = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cosine * self.w//2, self.y - self.sine * self.h//2)
        self.debut_timer = 90000

    #dessine l'image du vaisseau
    def draw(self, win):
        #win.blit(self.img, [self.x, self.y, self.w, self.h])
        win.blit(self.rotatedSurf, self.rotatedRect)

    #rotation droite
    def turnLeft(self):
        self.angle += 5
        self.rotatedSurf = pygame.transform.rotate(self.img, self.angle)
        self.rotatedRect = self.rotatedSurf.get_rect()
        self.rotatedRect.center = (self.x, self.y)
        self.cosine = math.cos(math.radians(self.angle + 90))
        self.sine = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cosine * self.w//2, self.y - self.sine * self.h//2)

    #rotation gauche
    def turnRight(self):
        self.angle -= 5
        self.rotatedSurf = pygame.transform.rotate(self.img, self.angle)
        self.rotatedRect = self.rotatedSurf.get_rect()
        self.rotatedRect.center = (self.x, self.y)
        self.cosine = math.cos(math.radians(self.angle + 90))
        self.sine = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cosine * self.w//2, self.y - self.sine * self.h//2)

    #avancer
    def moveForward(self):
        self.x += self.cosine * 6 #cosinus
        self.y -= self.sine * 6 #sinus
        self.rotatedSurf = pygame.transform.rotate(self.img, self.angle)
        self.rotatedRect = self.rotatedSurf.get_rect()
        self.rotatedRect.center = (self.x, self.y)
        self.cosine = math.cos(math.radians(self.angle + 90))
        self.sine = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cosine * self.w // 2, self.y - self.sine * self.h // 2)

    #mise à jour mouvement perso
    def updateLocation(self):
        if self.x > sw + 50:
            self.x = 0
        elif self.x < 0 - self.w:
            self.x = sw
        elif self.y < -50:
            self.y = sh
        elif self.y > sh + 50:
            self.y = 0

#définir tir
class Bullet(object):
    def __init__(self):
        self.point = player.head
        self.x, self.y = self.point
        self.w = 4
        self.h = 4
        self.c = player.cosine
        self.s = player.sine
        self.xv = self.c * 10
        self.yv = self.s * 10

    #mouvement balles
    def move(self):
        self.x += self.xv
        self.y -= self.yv

    #dessiner balles avec méthode rect
    def draw(self, win):
        pygame.draw.rect(win, (255, 255, 255), [self.x, self.y, self.w, self.h])

    #en cas de sortie de l'écran
    def checkOffScreen(self):
        if self.x < -50 or self.x > sw or self.y > sh or self.y < -50:
            return True

#définir astéroides
class Asteroid(object):
    def __init__(self, rank):
        self.rank = rank
        if self.rank == 1:
            self.image = asteroid50
        elif self.rank == 2:
            self.image = asteroid100
        else:
            self.image = asteroid150
        self.w = 50 * rank
        self.h = 50 * rank
        self.ranPoint = random.choice([(random.randrange(0, sw-self.w), random.choice([-1*self.h - 5, sh + 5])), (random.choice([-1*self.w - 5, sw + 5]), random.randrange(0, sh - self.h))])
        self.x, self.y = self.ranPoint
        if self.x < sw//2:
            self.xdir = 1
        else:
            self.xdir = -1
        if self.y < sh//2:
            self.ydir = 1
        else:
            self.ydir = -1
        self.xv = self.xdir * random.randrange(1,3)
        self.yv = self.ydir * random.randrange(1,3)

    # dessiner asteroides
    def draw(self, win):
        win.blit(self.image, (self.x, self.y))

#definir étoiles
class Star(object):
    def __init__(self):
        self.img = star
        self.w = self.img.get_width()
        self.h = self.img.get_height()
        self.ranPoint = random.choice([(random.randrange(0, sw - self.w), random.choice([-1 * self.h - 5, sh + 5])),
                                       (random.choice([-1 * self.w - 5, sw + 5]), random.randrange(0, sh - self.h))])
        self.x, self.y = self.ranPoint
        if self.x < sw//2:
            self.xdir = 1
        else:
            self.xdir = -1
        if self.y < sh//2:
            self.ydir = 1
        else:
            self.ydir = -1
        self.xv = self.xdir * 2
        self.yv = self.ydir * 2

    def draw(self, win):
        win.blit(self.img, (self.x, self.y))

#définir vaisseau alien
class Alien(object):
    def __init__(self):
        self.img = alienImg
        self.w = self.img.get_width()
        self.h = self.img.get_height()
        self.ranPoint = random.choice([(random.randrange(0, sw - self.w), random.choice([-1 * self.h - 5, sh + 5])),
                                       (random.choice([-1 * self.w - 5, sw + 5]), random.randrange(0, sh - self.h))])
        self.x, self.y = self.ranPoint
        if self.x < sw//2:
            self.xdir = 1
        else:
            self.xdir = -1
        if self.y < sh//2:
            self.ydir = 1
        else:
            self.ydir = -1
        self.xv = self.xdir * 2
        self.yv = self.ydir * 2

    def draw(self, win):
        win.blit(self.img, (self.x, self.y))

#definir les balles aliens
class AlienBullet(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.w = 4
        self.h = 4
        self.dx, self.dy = player.x - self.x, player.y - self.y
        self.dist = math.hypot(self.dx, self.dy)
        self.dx, self.dy = self.dx / self.dist, self.dy / self.dist
        self.xv = self.dx * 5
        self.yv = self.dy * 5

    def draw(self, win):
        pygame.draw.rect(win, (255, 255, 255), [self.x, self.y, self.w, self.h])



#la fenetre et son contenu
def redrawGameWindow():
    win.blit(bg, (0,0)) #overlap (chevauchement)  pour définir le haut à gauche de la surface soit
    font = pygame.font.SysFont('arial',30)
    livesText = font.render('Lives: ' + str(lives), 1, (255, 255, 255))
    playAgainText = font.render('Press Tab to Play Again', 1, (255,255,255))
    scoreText = font.render('Score: ' + str(score), 1, (255,255,255))
    highScoreText = font.render('High Score: ' + str(highScore), 1, (255, 255, 255))

    player.draw(win)
    for a in asteroids:
        a.draw(win)
    for b in playerBullets:
        b.draw(win)
    for s in stars:
        s.draw(win)
    for a in aliens:
        a.draw(win)
    for b in alienBullets:
        b.draw(win)

    #mode rapidfire
    if rapidFire:
        pygame.draw.rect(win, (0, 0, 0), [sw//2 - 51, 19, 102, 22])
        pygame.draw.rect(win, (255, 255, 255), [sw//2 - 50, 20, 100 - 100*(count - rfStart)/500, 20])

    #en cas de game over
    if gameover:
        win.blit(playAgainText, (sw//2-playAgainText.get_width()//2, sh//2 - playAgainText.get_height()//2))
    win.blit(scoreText, (sw- scoreText.get_width() - 25, 25))
    win.blit(livesText, (25, 25))
    win.blit(highScoreText, (sw - highScoreText.get_width() -25, 35 + scoreText.get_height()))
    pygame.display.update() #afficher script


#definir taux apparition selon timer
player = Player()
playerBullets = []
asteroids = []
count = 0
stars = []
aliens = []
alienBullets = []
run = True
while run: #Quand la partie démarre
    clock.tick(60)
    count += 1
    if not gameover: #si ce n'est pas game over déclenche apparition
        if count % 50 == 0:
            ran = random.choice([1,1,1,2,2,3])
            asteroids.append(Asteroid(ran))
        if count % 1000 == 0:
            stars.append(Star())
        if count % 750 == 0:
            aliens.append(Alien())
        for i, a in enumerate(aliens):
            a.x += a.xv
            a.y += a.yv
            if a.x > sw + 150 or a.x + a.w < -100 or a.y > sh + 150 or a.y + a.h < -100:
                aliens.pop(i)
            if count % 60 == 0:
                alienBullets.append(AlienBullet(a.x + a.w//2, a.y + a.h//2))

            #En cas d'impact
            for b in playerBullets:
                if (b.x >= a.x and b.x <= a.x + a.w) or b.x + b.w >= a.x and b.x + b.w <= a.x + a.w:
                    if (b.y >= a.y and b.y <= a.y + a.h) or b.y + b.h >= a.y and b.y + b.h <= a.y + a.h:
                        aliens.pop(i)
                        if isSoundOn:
                            bangLargeSound.play()
                        score += 50
                        break

        for i, b in enumerate(alienBullets):
            b.x += b.xv
            b.y += b.yv
            if (b.x >= player.x - player.w//2 and b.x <= player.x + player.w//2) or b.x + b.w >= player.x - player.w//2 and b.x + b.w <= player.x + player.w//2:
                if (b.y >= player.y-player.h//2 and b.y <= player.y + player.h//2) or b.y + b.h >= player.y - player.h//2 and b.y + b.h <= player.y + player.h//2:
                    lives -= 1
                    alienBullets.pop(i)
                    break

        player.updateLocation()
        for b in playerBullets:
            b.move()
            if b.checkOffScreen():
                playerBullets.pop(playerBullets.index(b))

        #effets asteroides et son
        for a in asteroids:
            a.x += a.xv
            a.y += a.yv

            if (a.x >= player.x - player.w//2 and a.x <= player.x + player.w//2) or (a.x + a.w <= player.x + player.w//2 and a.x + a.w >= player.x - player.w//2):
                if(a.y >= player.y - player.h//2 and a.y <= player.y + player.h//2) or (a.y  +a.h >= player.y - player.h//2 and a.y + a.h <= player.y + player.h//2):
                    lives -= 1
                    asteroids.pop(asteroids.index(a))
                    if isSoundOn:
                        bangLargeSound.play()
                    break

            # collision balle et score
            for b in playerBullets:
                if (b.x >= a.x and b.x <= a.x + a.w) or b.x + b.w >= a.x and b.x + b.w <= a.x + a.w:
                    if (b.y >= a.y and b.y <= a.y + a.h) or b.y + b.h >= a.y and b.y + b.h <= a.y + a.h:
                        if a.rank == 3:
                            if isSoundOn:
                                bangLargeSound.play()
                            score += 10
                            na1 = Asteroid(2)
                            na2 = Asteroid(2)
                            na1.x = a.x
                            na2.x = a.x
                            na1.y = a.y
                            na2.y = a.y
                            asteroids.append(na1)
                            asteroids.append(na2)
                        elif a.rank == 2:
                            if isSoundOn:
                                bangSmallSound.play()
                            score += 20
                            na1 = Asteroid(1)
                            na2 = Asteroid(1)
                            na1.x = a.x
                            na2.x = a.x
                            na1.y = a.y
                            na2.y = a.y
                            asteroids.append(na1)
                            asteroids.append(na2)
                        else:
                            score += 30
                            if isSoundOn:
                                bangSmallSound.play()
                        asteroids.pop(asteroids.index(a))
                        playerBullets.pop(playerBullets.index(b))
                        break

        #Pour les poissons et activation  du mode rapidfire
        for s in stars:
            s.x += s.xv
            s.y += s.yv
            if s.x < -100 - s.w or s.x > sw + 100 or s.y > sh + 100 or s.y < -100 - s.h:
                stars.pop(stars.index(s))
                break
            for b in playerBullets:
                if (b.x >= s.x and b.x <= s.x + s.w) or b.x + b.w >= s.x and b.x + b.w <= s.x + s.w:
                    if (b.y >= s.y and b.y <= s.y + s.h) or b.y + b.h >= s.y and b.y + b.h <= s.y + s.h:
                        rapidFire = True
                        rfStart = count
                        stars.pop(stars.index(s))
                        playerBullets.pop(playerBullets.index(b))
                        break

        #conditions game over et redémarrage partie
        if lives <= 0:
            gameover = True

        if rfStart != -1:
            if count - rfStart > 500:
                rapidFire = False
                rfStart = -1

        #controle vaisseau
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.turnLeft()
        if keys[pygame.K_RIGHT]:
            player.turnRight()
        if keys[pygame.K_UP]:
            player.moveForward()
        if keys[pygame.K_SPACE]:
            if rapidFire:
                playerBullets.append(Bullet())
                if isSoundOn:
                    shoot.play()

    #controle parametre
    for event in pygame.event.get(): #arreter code si joueur quitte
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE: #touche de tir si pas de game over et de rapidFire
                if not gameover:
                    if not rapidFire:
                        playerBullets.append(Bullet())
                        if isSoundOn:
                            shoot.play()
            if event.key == pygame.K_m: #touche pour le son
                isSoundOn = not isSoundOn
            if event.key == pygame.K_TAB:
                if gameover: #en cas de game over AR de la partie
                    gameover = False
                    lives = 4
                    asteroids.clear()
                    aliens.clear()
                    alienBullets.clear()
                    stars.clear()
                    if score > highScore: #remplace le meilleur score si le score actuel est meilleur
                        highScore = score
                    score = 0

    #remet la fenetre du jeu
    redrawGameWindow()#boucle
pygame.quit() #le code s'arrête