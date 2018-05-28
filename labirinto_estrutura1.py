#matriz[linha][coluna]
#img_player = pygame.image.load(os.path.join('Imagens/player4.png'))
#pygame.transform.scale(player,(13,13))

import pygame
import os
import time
pygame.init()
pygame.display.init()
pos_p_x = 2     #POSIÇÃO INICIAL X NO PLANO CARTESIANO DO PLAYER
pos_p_y = 3     #POSIÇÃO INICIAL Y NO PLANO CARTESIANO DO PLAYER
q = 27
t_matriz = 21

def lab_fase1(screen,maze1,preto,player): #DESESNHA O LABIRINTO
        parede = pygame.image.load(os.path.join('Imagens/parede1.png'))
        parede = pygame.transform.scale(parede,(27,27))
        porta = pygame.image.load(os.path.join('Imagens/porta1.png'))
        porta = pygame.transform.scale(porta,(27,27))
        pos_y = 0       #POSIÇÃO Y DA MATRIZ, DETERMINA A COLUNA/LARGURA
        for y in range(0,t_matriz): #determina a linha
            pos_x = 0   #POSIÇÃO X DA MATRIZ, DETERMINA A LINHA/ALTURA
            for x in range(0,t_matriz): #determina a coluna
                if x == pos_p_x and y == pos_p_y:
                    screen.blit(player,(pos_x,pos_y))
                if maze1[y][x] == 1:     #SE O VALOR DA LINHA Y E COLUNA X FOR IGUAL A 1
                    screen.blit(parede,(pos_x,pos_y))
                    time.sleep(0.01)
                if maze1[y][x] == 2:
                    screen.blit(porta,(pos_x,pos_y))
                pygame.display.flip()
                pos_x += q          
            pos_y += q


            #        5         10        15        20     
maze1 = [   [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1], #01    
            [1,0,0,0,1,0,0,0,1,0,1,0,0,0,0,0,1,0,0,0,1], #02
            [1,1,1,0,1,0,1,0,0,0,1,0,1,1,1,0,1,1,1,0,1], #03
            [1,0,0,0,1,0,1,0,1,0,1,0,1,0,0,0,1,0,0,0,1], #04
            [1,0,1,0,1,0,1,1,1,1,1,0,1,0,1,1,1,0,1,1,1], #05    
            [1,0,1,0,0,0,1,0,0,0,0,0,1,0,1,0,0,0,1,0,1], #06
            [1,0,1,1,1,1,1,0,1,1,1,1,1,0,1,0,1,0,1,0,1], #07
            [1,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,1], #08
            [1,1,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1], #09    
            [1,0,1,0,1,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,1], #10
            [1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,0,1,0,1,0,1], #11
            [1,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,1,0,1], #12
            [1,0,1,1,1,1,1,0,1,0,1,1,1,0,1,0,1,0,1,0,1], #13    
            [1,0,0,0,0,0,0,0,1,0,1,0,0,0,1,0,0,0,1,0,1], #14
            [1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,0,1], #15
            [1,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,1,0,1,0,1], #16     
            [1,1,1,0,1,1,1,1,1,0,1,0,1,1,1,0,1,0,1,0,1], #17    
            [1,0,0,0,1,0,0,0,0,0,1,0,0,0,1,0,1,0,0,0,1], #18
            [1,0,1,1,1,1,1,0,1,0,1,1,1,0,1,0,1,1,1,0,1], #19
            [1,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1], #20
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]] #21
            
