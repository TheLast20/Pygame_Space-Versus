import pygame,random

#---------------------------------------------------------------
#Funciones de apoyo

def screen_update(screen):
    #Background
    background = pygame.image.load("resources/background-black.png").convert_alpha()
    background = pygame.transform.scale(background,[500,500])
    screen.blit(background, [0, 0])

def screen_text(screen,jugador):
    # Title
    font = pygame.font.Font(None, 50)
    text = "Level: {}".format(str(jugador.level))
    screen.blit(font.render(text, 0, [255, 255, 255]), [0, 0])
    text = "Live: {}".format(str(jugador.life))
    screen.blit(font.render(text, 0, [255, 255, 255]), [350, 0])

def controlers(jugador,size):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and len(jugador.elements)<=10:
                #jugador.shot()
                None

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w] and jugador.y + jugador.speed > 0:
        jugador.y -= jugador.speed

    if keys[pygame.K_s] and jugador.y + jugador.speed + jugador.size[1] - 10 < size[1]:
        jugador.y += jugador.speed

    if keys[pygame.K_a] and jugador.x + jugador.speed > 0:
        jugador.x -= jugador.speed

    if keys[pygame.K_d] and jugador.x + jugador.speed + jugador.size[0] - 15 < size[1]:
        jugador.x += jugador.speed

def collid_nave(jugador,meteorite):
    rocks = meteorite.elements
    for rock in rocks:
        r1 = pygame.Rect(rock[0],rock[1],meteorite.size_element[0],meteorite.size_element[1])
        r2 = pygame.Rect(jugador.x,jugador.y,jugador.size[0],jugador.size[1])

        if r1.colliderect(r2):
            return True

    return False

def destroy(jugador,meteorite,screen):
    L = []
    L_lasers = []
    L_rock = []

    for n_rock in range(len(meteorite.elements)):
        for n_laser in range(len(jugador.elements)):
            r = meteorite.elements[n_rock]
            l = jugador.elements[n_laser]

            r1 = pygame.Rect(r[0], r[1], meteorite.size_element[0], meteorite.size_element[1])
            r2 = pygame.Rect(l[0], l[1], jugador.size_element[0], jugador.size_element[0])

            if r1.colliderect(r2):
                L_lasers.append(n_laser)
                L_rock.append(n_rock)
                L.append([r[0], r[1]])

    L1, L2 = [], []

    for i in range(len(jugador.elements)):
        if i not in L_lasers:
            L1.append(jugador.elements[i])

    for i in range(len(meteorite.elements)):
        if i not in L_rock:
            L2.append(meteorite.elements[i])

    jugador.elements = L1[::]
    meteorite.elements = L2[::]

    for i in L:
        screen.blit(jugador.imagen_kill, [i[0],i[1]])


