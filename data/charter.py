import pygame,random

#---------------------------------------------------
class Ships():
    def __init__(self):
        self.speed = 10
        self.life = True

        #Position:
        self.x = None
        self.y = None

        #Information Ships:
        self.size = None
        self.imagen_ships = None

        #Lasers:
        self.max = 8
        self.speed_laser = None
        self.imagen_laser = None
        self.list_laser = None
        self.size_laser = None

        self.limit = None
        self.direction = None

        #Destruccion:
        self.size_explotion = [50,50]
        self.imagen_kill = pygame.image.load("resources/explotion.png").convert_alpha()
        self.imagen_kill = pygame.transform.scale(self.imagen_kill, self.size_explotion)


    def __limits(self,lasers):
        if self.direction == "UP":
            return lasers[1]  > self.limit

        elif self.direction == "DOWN":
            return lasers[1] + self.size_laser[1] + self.speed_laser < self.limit


    def draw_ship(self,screen):
        screen.blit(self.imagen_ships,[self.x,self.y])


    def draw_lasers(self,screen):
        for laser in self.list_laser:
            screen.blit(self.imagen_laser, laser)


    def shot(self,valor = 100):
        if len(self.list_laser)<self.max:
            if self.direction == "UP":
                self.laser = (self.x + 25, self.y - 30 )
                self.list_laser.append(self.laser)


            elif self.direction == "DOWN":
                if self.x >0:
                    self.laser = (self.x + 25, self.y + 30)
                    porcentaje = -valor + 101
                    n = random.randint(0, porcentaje)
                    if n == 5:
                        self.list_laser.append(self.laser)


    def move_laser(self):
        self.L = []
        for laser in self.list_laser:
            if (self.__limits(laser)):
                self.L.append([laser[0], laser[1] + self.speed_laser])

        self.list_laser = self.L[::]
        #



    def colition(self,laser):
        r1 = pygame.Rect(self.x, self.y, self.size[0], self.size[1])
        r2 = pygame.Rect(laser[0], laser[1], self.size_laser[0], self.size_laser[1])
        return r1.colliderect(r2)

    def destruction(self,lasers):
        L = []
        for laser in lasers:
            if self.colition(laser):
                self.life = False
            else:
                L.append(laser)
        return L



# def moven_laser(self):
    #
    #
    #
    # def draw_elements(self,screen):
    #     for element in self.elements:
    #         screen.blit(self.imagen_element, [element[0], element[1]])
    #
    #
    #
class Player(Ships):
    def __init__(self):
        super().__init__()
        self.x = 300
        self.y = 300
        self.level = 1
        self.life = 150
        self.damage = 10

        # Information Ships:
        self.size = [60,60]
        self.imagen_ships = pygame.image.load("resources/pixel_ship_yellow.png").convert_alpha()
        self.imagen_ships = pygame.transform.scale(self.imagen_ships,self.size)


        # Lasers:
        self.max = 5000
        self.speed_laser = -5

        self.list_laser = []
        self.size_laser = [10, 31]
        self.imagen_laser = pygame.image.load("resources/pixel_laser_yellow.png").convert_alpha()
        self.imagen_laser  =pygame.transform.scale(self.imagen_laser,self.size_laser)

        self.limit = -50
        self.direction = "UP"



    def draw_ship(self,screen):
        screen.blit(self.imagen_ships,[self.x,self.y])
        #Life
        self.g_life = self.life/1.5

        if self.g_life>0:
            self.green = pygame.Rect(self.x - 20, self.y + 70, self.life / 1.5, 10)
            pygame.draw.rect(screen, [0, 255, 0], self.green)

        self.r_life = 150 - self.life

        if self.r_life>0:
            self.red = pygame.Rect(self.x - 20 + self.g_life, self.y + 70, self.r_life / 1.5, 10)
            pygame.draw.rect(screen, [255, 0, 0], self.red)

    def change_level(self):
        self.level += 1
        self.damage += 5
        if self.life + 50<150:
            self.life+=50
        else:
            self.life=150

    def move_ship(self,size):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE :
                    self.shot()


        keys = pygame.key.get_pressed()

        if keys[pygame.K_w] and self.y + self.speed > 15:
            self.y -= self.speed

        # if keys[pygame.K_SPACE] :
        #     self.shot(100)

        if keys[pygame.K_s] and self.y + self.speed + self.size[1] - 15 < size[1]:
            self.y += self.speed

        if keys[pygame.K_a] and self.x + self.speed > 0 + 10 :
            self.x -= self.speed

        if keys[pygame.K_d] and self.x + self.speed + self.size[0] < size[0] +15:
            self.x += self.speed

        self.move_laser()




class Enemy(Ships):
    def __init__(self,x,y,color,player):
        self.player = player #Un objeto

        self.dic = {"blue":["resources/pixel_ship_blue_small.png","resources/pixel_laser_blue.png"],
                    "red":["resources/pixel_ship_red_small.png","resources/pixel_laser_red.png"],
                    "green":["resources/pixel_ship_green_small.png","resources/pixel_laser_green.png"]}

        super().__init__()
        self.x = x
        self.y = y

        self.speed = 5
        self.level = 1

        # Information Ships:
        self.size = [60,60]
        self.imagen_ships = pygame.image.load(self.dic[color][0]).convert_alpha()
        self.imagen_ships = pygame.transform.scale(self.imagen_ships,self.size)
        self.imagen_ships = pygame.transform.rotate(self.imagen_ships, 180)

        # Lasers:
        self.max = 2
        self.speed_laser = 5

        self.list_laser = []
        self.size_laser = [10, 31]




        self.imagen_laser = pygame.image.load(self.dic[color][1]).convert_alpha()
        self.imagen_laser  =pygame.transform.scale(self.imagen_laser,self.size_laser)


        self.limit = 550
        self.direction = "DOWN"


    def change_level(self,level):
        self.level = level
        self.max += level



    def comparation(self,pos1,pos2):
        r1 = pygame.Rect(pos1[0],pos1[1],self.size[0]+15,self.size[1])
        r2 = pygame.Rect(pos2[0],pos2[1],self.size_laser[0],self.size_laser[1])
        return r1.colliderect(r2)


    def move_ship(self,size):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    self.shot()


        L1 = []
        L2 = []
        L3 = []
        L4 = []
        L5 = []

        for laser in self.player.list_laser:
            pos1 = [self.x-10, self.y]
            pos2 = [laser[0] ,self.y]
            if self.comparation(pos1,pos2):
                if laser[1]<self.y + 100:
                    L1.append(laser[0])
                    L2.append(laser[1])
                    L3.append(laser[1])

        if len(L1)>0 and len(L2)>0:
            L3.sort()

            for i in L3:
                L4.append(L1[L2.index(i)])
                L5.append(L2[L2.index(i)])

            self.varX = L4[0]
            self.varY = L5[0]
            del L1,L2,L3,L4,L5

            if self.varX + 5 - (self.x + self.size[0]/2)>0:
                self.x-=self.speed
            elif self.varX + 5 - (self.x + self.size[0]/2 )<0:
                self.x+= self.speed
            else:
                self.shot(90)


        else:
            self.y+=1
            self.shot(15)

        self.move_laser()