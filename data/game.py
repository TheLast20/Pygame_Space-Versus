from data.charter import *
import pygame,random


def screen_update(screen,player,enemys):
    #Background
    background = pygame.image.load("resources/background-black.png").convert_alpha()
    background = pygame.transform.scale(background,[500,500])
    screen.blit(background, [0, 0])
    player.draw_ship(screen)
    for enemy in enemys:
        enemy.draw_ship(screen)

    title = pygame.font.Font(None,50)
    screen.blit(title.render("Level: {}".format(player.level),0,[255,255,255]),[20,10])





def move_charter(player,enemys,size,screen):
    player.move_ship(size)
    player.draw_lasers(screen)
    for enemy in enemys:
        enemy.move_ship(size)
        enemy.draw_lasers(screen)
    pygame.display.update()



def colition_laser(player,enemys):
    for enemy in enemys:
        L_laser_enemy = []
        for laser in enemy.list_laser:
            bandera1 = True
            L_laser_player = []
            for laser_player in player.list_laser:
                r1 = pygame.Rect(laser[0],laser[1],10,31)
                r2 = pygame.Rect(laser_player[0],laser_player[1],10,31)

                if r1.colliderect(r2):
                    bandera1 = False

                else:
                    L_laser_player.append(laser_player)

            player.list_laser = L_laser_player[::]

            if bandera1:
                L_laser_enemy.append(laser)

        enemy.list_laser = L_laser_enemy[::]


def destruction_enemys(player,enemys):
    L = []
    for enemy in enemys:
        L2 = enemy.destruction(player.list_laser)

        if enemy.life:
            L.append(enemy)

        player.list_laser = L2[::]
    enemys = L[::]
    return enemys

def create_enemys(player):
    enemys = []
    potition = []
    num = player.level + random.randint(4,6)
    for i in range(num):
        bandera = True
        while bandera:
            x = random.randint(0, 400)
            y = random.randint(-1000, 0)
            bandera = False

            for pos in potition:
                r1 = pygame.Rect(x, y, 60, 60)
                r2 = pygame.Rect(pos[0], pos[1], 60, 60)

                if r1.colliderect(r2):
                    bandera = True

        color = random.choice(["blue", "red", "green"])

        enemy = Enemy(x, y, color, player)
        enemy.change_level(player.level)
        enemys.append(enemy)
        potition.append([x, y])
    return enemys

def damage(player,enemys):
    for enemy in enemys:
        L= []
        for laser in enemy.list_laser:
            r1 = pygame.Rect(player.x,player.y,player.size[0],player.size[1])
            r2 = pygame.Rect(laser[0],laser[1],enemy.size_laser[0],enemy.size_laser[1])
            if r1.colliderect(r2):

                player.life-=player.damage
                print(player.life)
            else:
                L.append(laser)
        enemy.list_laser = L[::]








def game_space(screen):
    player = Player()

    size = screen.get_size()
    # Create Clock
    clock = pygame.time.Clock()
    game = True
    while game:
        round = True
        enemys = create_enemys(player)

        while round:
            move_charter(player, enemys, size, screen)
            colition_laser(player, enemys)
            enemys = destruction_enemys(player, enemys)

            damage(player, enemys)

            screen_update(screen, player, enemys)

            if player.life <= 0:
                round = False
                game = False

            elif len(enemys) == 0:
                round = False
                tik = 0
                while tik<200:
                    title = pygame.font.Font(None, 50)
                    move_charter(player, enemys, size, screen)
                    screen_update(screen,player,enemys)
                    screen.blit(title.render("Level Complete", 0, [255, 255, 255]), [220, 10])

                    tik+=1
                    clock.tick(60)
                player.change_level()



            clock.tick(60)



