import pygame
from threading import Timer

pygame.init()

display_width = 1200
display_height = 700
width = 40
height = 60
vel = 10

pygame.display.set_caption("First Game")
gameDisplay = pygame.display.set_mode((display_width,display_height))

walkRight = [pygame.transform.scale(pygame.image.load('player_run0.png'), (60, 120)), pygame.transform.scale(pygame.image.load('player_run1.png'), (60, 120))]
walkLeft = [pygame.transform.flip(pygame.transform.scale(pygame.image.load('player_run0.png'), (60, 120)), 1, 0), pygame.transform.flip(pygame.transform.scale(pygame.image.load('player_run1.png'), (60, 120)), 1, 0)]
walkRight2 = [pygame.transform.scale(pygame.image.load('player2_run0.png'), (60, 120)), pygame.transform.scale(pygame.image.load('player2_run1.png'), (60, 120))]
walkLeft2 = [pygame.transform.flip(pygame.transform.scale(pygame.image.load('player2_run0.png'), (60, 120)), 1, 0), pygame.transform.flip(pygame.transform.scale(pygame.image.load('player2_run1.png'), (60, 120)), 1, 0)]

player1Img = pygame.image.load('player.png')
player1Img = pygame.transform.scale(player1Img, (60, 120))

player2Img = pygame.image.load('player2.png')
player2Img = pygame.transform.scale(player2Img, (60, 120))

background = pygame.image.load('background.png')
background = pygame.transform.scale(background, (1200, 700))

shootingAnim = pygame.image.load('shooting0.png')
shootingAnim = pygame.transform.scale(shootingAnim, (60, 120))
lshootingAnim = pygame.transform.flip(shootingAnim, 1, 0)

shootingAnim2 = pygame.image.load('shooting0_2.png')
shootingAnim2 = pygame.transform.scale(shootingAnim2, (60, 120))
lshootingAnim2 = pygame.transform.flip(shootingAnim2, 1, 0)

def quit():
    pygame.quit()

class player1(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.jumpCount = 20
        self.left = False
        self.right = False
        self.walkCount = 0
        self.isCrouch = False
        self.isShooting = False
        self.standing = False
        self.hitbox = (self.x + 1, self.y, 60, 120)
        self.health = 100
        self.visible = True
        
    def draw(self, gameDisplay):
        reset = 0
        if self.walkCount + 1 >= 6:
            self.walkCount = 0
        if reset < 1:
            if not (self.standing) and not self.isShooting: #moving
                if self.left:
                    gameDisplay.blit(walkLeft[self.walkCount // 3], (self.x, self.y))
                    self.walkCount += 1
                elif self.right:
                    gameDisplay.blit(walkRight[self.walkCount // 3], (self.x, self.y))
                    self.walkCount += 1         
                elif self.isCrouch and self.left:
                    gameDisplay.blit(pygame.transform.scale(walkLeft[self.walkCount // 3], (60, 60)), (self.x, self.y))
                    self.walkCount += 1
                elif self.isCrouch and self.right:
                    gameDisplay.blit(pygame.transform.scale(walkRight[self.walkCount // 3], (60, 60)), (self.x, self.y))
                    self.walkCount += 1
            elif self.standing and not self.isShooting: #not moving
                if self.isCrouch and self.right:
                    gameDisplay.blit(pygame.transform.scale(player1Img, (60, 60)), (self.x, self.y + 60))
                elif self.isCrouch and self.left:
                    gameDisplay.blit(pygame.transform.flip(pygame.transform.scale(player1Img, (60, 60)), 1, 0), (self.x, self.y + 60))
                elif self.right:
                    gameDisplay.blit(player1Img, (self.x, self.y))
                else:
                    gameDisplay.blit(pygame.transform.flip(player1Img, 1, 0), (self.x, self.y))
        if self.isShooting:
            player1Img.set_alpha(0)
            for m in walkRight:
                m.set_alpha(0)
            for n in walkLeft:
                n.set_alpha(0)
            reset += 1
        if self.visible == False:
            text = font.render("Player 2 Wins", 1, (250, 250, 250))
            gameDisplay.blit(text, (500, 10))
            
        pygame.draw.rect(gameDisplay, (255, 0, 0), (800, 200, 100, 20))
        if self.health > 0:
            pygame.draw.rect(gameDisplay, (0, 255, 0), (800, 200, 100 - (100 - self.health), 20))
        self.hitbox = (self.x + 1, self.y, 60, 120)
        pygame.draw.rect(gameDisplay, (255, 0, 0), self.hitbox, 2)
            

    def shootingAnimation(self):
        i = 0
        while i < 50:
            if self.right:
                gameDisplay.blit(shootingAnim, (player1.x, player1.y))
            if self.left:
                gameDisplay.blit(lshootingAnim, (player1.x, player1.y))
            self.isShooting = True
            pygame.display.update()
            i += 1
        self.isShooting = False
        self.reset = 0

    def hit(self):
        if self.health > 0:
            self.health -= 20
            if self.health > 0:
                pass
            else:
                self.visible = False
        else:
            self.visible = False
        print('hit')


class player2(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.jumpCount = 20
        self.left = False
        self.right = False
        self.walkCount = 0
        self.isCrouch = False
        self.isShooting = False
        self.standing = False
        self.hitbox = (self.x + 1, self.y, 60, 120)
        self.health = 100
        self.visible = True
        
    def draw(self, gameDisplay):
        reset = 0
        if self.walkCount + 1 >= 6:
            self.walkCount = 0
        if reset < 1:
            if not (self.standing) and not self.isShooting: #moving
                if self.left:
                    gameDisplay.blit(walkLeft2[self.walkCount // 3], (self.x, self.y))
                    self.walkCount += 1
                elif self.right:
                    gameDisplay.blit(walkRight2[self.walkCount // 3], (self.x, self.y))
                    self.walkCount += 1         
                elif self.isCrouch and self.left:
                    gameDisplay.blit(pygame.transform.scale(walkLeft2[self.walkCount // 3], (60, 60)), (self.x, self.y))
                    self.walkCount += 1
                elif self.isCrouch and self.right:
                    gameDisplay.blit(pygame.transform.scale(walkRight2[self.walkCount // 3], (60, 60)), (self.x, self.y))
                    self.walkCount += 1
            elif self.standing and not self.isShooting: #not moving
                if self.isCrouch and self.right:
                    gameDisplay.blit(pygame.transform.scale(player2Img, (60, 60)), (self.x, self.y + 60))
                elif self.isCrouch and self.left:
                    gameDisplay.blit(pygame.transform.flip(pygame.transform.scale(player2Img, (60, 60)), 1, 0), (self.x, self.y + 60))
                elif self.right:
                    gameDisplay.blit(player2Img, (self.x, self.y))
                else:
                    gameDisplay.blit(pygame.transform.flip(player2Img, 1, 0), (self.x, self.y))
        if self.visible == False:
            text = font.render("Player 1 Wins", 1, (250, 250, 250))
            gameDisplay.blit(text, (500, 10))
        
        pygame.draw.rect(gameDisplay, (255, 0, 0), (300, 200, 100, 20))
        if self.health > 0:
            pygame.draw.rect(gameDisplay, (0, 255, 0), (300, 200, 100 - (100 - self.health), 20))
        self.hitbox = (self.x + 1, self.y, 60, 120)
        pygame.draw.rect(gameDisplay, (255, 0, 0), self.hitbox, 2)
        
        if self.isShooting:
            player2Img.set_alpha(0)
            for m in walkRight2:
                m.set_alpha(0)
            for n in walkLeft2:
                n.set_alpha(0)
            reset += 1

    def shootingAnimation(self):
        i = 0
        while i < 50:
            if self.right:
                gameDisplay.blit(shootingAnim2, (player2.x, player2.y))
            if self.left:
                gameDisplay.blit(lshootingAnim2, (player2.x, player2.y))
            self.isShooting = True
            pygame.display.update()
            i += 1
        self.isShooting = False
        self.reset = 0

    def hit(self):
        if self.health > 0:
            self.health -= 20
            if self.health > 0:
                pass
            else:
                self.visible = False
        else:
            self.visible = False
        print('hit')
        
player1 = player1(500, 425, 60, 120)
player2 = player2(50, 425, 60, 120)
pews1 = []
pews2 = []

projectileAnim = pygame.image.load('projectile0.png')
projectileAnim = pygame.transform.scale(projectileAnim, (40, 40))

class projectile1(object):
    def __init__(self, x, y, facing):
        self.x = x
        self.y = y
        self.facing = facing
        self.vel = 30 * facing
        self.hitbox = (self.x + 1, self.y, 60, 120)
    def draw(self, gameDisplay):
        if player1.right:
            gameDisplay.blit(projectileAnim, (self.x, self.y))
        if player1.left:
            gameDisplay.blit(pygame.transform.flip(projectileAnim, 1, 0), (self.x, self.y))

        self.hitbox = (self.x + 1, self.y, 40, 40)
        pygame.draw.rect(gameDisplay, (255, 0, 0), self.hitbox, 2)
        
class projectile2(object):
    def __init__(self, x, y, facing):
        self.x = x
        self.y = y
        self.facing = facing
        self.vel = 30 * facing
    def draw(self, gameDisplay):
        gameDisplay.blit(pygame.transform.scale(pygame.image.load('projectile0.png'), (20, 20)), (player2.x, player2.y))
        
        
def redrawGameWindow():
    player1.draw(gameDisplay)
    player2.draw(gameDisplay)
    for pew in pews1:
        pew.draw(gameDisplay)
    for pew in pews2:
        pew.draw(gameDisplay)
    pygame.display.update() 

shootTime1 = 30
shootTime2 = 30
font = pygame.font.SysFont('comicfans', 30, True)

run = True
while run:

    clock = pygame.time.Clock()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
            
    #Player 1
    for pew in pews1:
        if pew.y - pew.hitbox[3] < player2.hitbox[1] + player2.hitbox[3] and pew.y + pew.hitbox[3] > player2.hitbox[1]:
            if pew.x + pew.hitbox[3] > player2.hitbox[0] and pew.x - pew.hitbox[3] + 90 < player2.hitbox[0] + player2.hitbox[3]:
                player2.hit()
                pews1.pop(pews1.index(pew))
        if pew.x < 1200 and pew.x > 0:
            pew.x += pew.vel
        else:
            pews1.pop(pews1.index(pew))
            
    if keys[pygame.K_f]:
        player1.standing = True
        if shootTime1 > 30:
            if player1.left:
                facing = -1
            else:
                facing = 1
            pews1.append(projectile1(round(player1.x + player1.width // 3 + facing * 20), round(player1.y + player1.height // 2 - 5), facing))
            player1.shootingAnimation()
            shootTime1 = 0
            
      
    if keys[pygame.K_a] and player1.x > player1.vel: 
        player1.x -= player1.vel
        player1.left = True
        player1.right = False
        player1.standing = False

    elif keys[pygame.K_d] and player1.x < 1200 - player1.width - player1.vel:  
        player1.x += player1.vel
        player1.left = False
        player1.right = True
        player1.standing = False
        
    elif keys[pygame.K_s]:
        player1.isCrouch = True
        player1.Standing = False
        
    else:
        player1.standing = True
        player1.isCrouch = False
        player1.walkCount = 0
        player1.isShooting = False
    
    if not(player1.isJump): 
        if keys[pygame.K_w] and player1.y > player1.vel:
            player1.isJump = True

        if keys[pygame.K_SPACE]:
            player1.isJump = True
    else:
        if player1.jumpCount >= -20:
            player1.y -= (player1.jumpCount * abs(player1.jumpCount)) * 0.20
            player1.jumpCount -= 4
            
        else: 
            player1.jumpCount = 20
            player1.isJump = False
    #player 2
    for pew in pews2:
        if pew.y - pew.hitbox[3] < player1.hitbox[1] + player1.hitbox[3] and pew.y + pew.hitbox[3] > player1.hitbox[1]:
            if pew.x + pew.hitbox[3] > player1.hitbox[0] and pew.x - pew.hitbox[3] + 90 < player1.hitbox[0] + player1.hitbox[3]:
                player1.hit()
                pews2.pop(pews2.index(pew))
        if pew.x < 1200 and pew.x > 0:
            pew.x += pew.vel
        else:
            pews2.pop(pews2.index(pew))
            
    
    if keys[pygame.K_PERIOD]:
        player2.standing = True
        if shootTime2 > 30:
            if player2.left:
                facing = -1
            else:
                facing = 1
            pews2.append(projectile1(round(player2.x + player2.width // 3 + facing * 20), round(player2.y + player2.height // 2 - 5), facing))
            player2.shootingAnimation()
            shootTime2 = 0
      
    if keys[pygame.K_LEFT] and player2.x > player2.vel: 
        player2.x -= player2.vel
        player2.left = True
        player2.right = False
        player2.standing = False

    elif keys[pygame.K_RIGHT] and player2.x < 1200 - player2.width - player2.vel:  
        player2.x += player2.vel
        player2.left = False
        player2.right = True
        player2.standing = False
        
    elif keys[pygame.K_DOWN]:
        player2.isCrouch = True
        player2.Standing = False
        
    else:
        player2.standing = True
        player2.isCrouch = False
        player2.walkCount = 0
    
    if not(player2.isJump): 
        if keys[pygame.K_UP] and player2.y > player2.vel:
            player2.isJump = True

        if keys[pygame.K_COMMA]:
            player2.isJump = True
    else:
        if player2.jumpCount >= -20:
            player2.y -= (player2.jumpCount * abs(player2.jumpCount)) * 0.20
            player2.jumpCount -= 4
            
        else: 
            player2.jumpCount = 20
            player2.isJump = False
    
    gameDisplay.fill((0,0,0))
    shootTime1 += 1
    shootTime2 += 1
    gameDisplay.blit(background, (0, 0))
    clock.tick(30)
    redrawGameWindow()
    
pygame.quit()
