
from data.game import *

import pygame,random

def main():
    #Inicializo el sistema
    pygame.init()
    size = [500,500]
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Space_Batle")

    game = False
    while True:
        #Creo el Background
        background = pygame.image.load("resources/background-black.png").convert_alpha()
        background = pygame.transform.scale(background, [500, 500])

        fuente = pygame.font.Font(None,50)


        screen.blit(background, [0, 0])
        screen.blit(fuente.render("Press [SPACE] for init",0,[255,255,255]),[60,200])


        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE :
                    game = True
                    pygame.time.delay(500)

        if game:
            game_space(screen)

            pygame.quit()
            exit()



if __name__ == '__main__':
    main()
