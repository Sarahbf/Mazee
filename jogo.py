import pygame
import time
import sys
import os
from labirinto_estrutura1 import *
from labirinto_estrutura2 import *
from labirinto_estrutura3 import *
from funcoes import *

pygame.init()
pygame.display.init()
screen = pygame.display.set_mode((372,750))
pygame.display.set_caption("Menu")
screen.fill((255,255,255))

def button(w,h,x,y): #W = LARGURA, H = ALTURA, X E Y = POSIÇÃO DE ACORDO COM O PLANO CARTESIANO
    global audio
    global p #VARIÁVEL QUE RECEBE IMAGEM DO PLAYER ESCOLHIDA
    global menu_estado
    mouse = pygame.mouse.get_pos() #DETECTA A POSIÇÃO DO MOUSE
    click = pygame.mouse.get_pressed() #DETECTA SE CLICKAMOS COMO MOUSE
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        #VERIFICAÇÃO 1 (LARGURA): SE A POSIÇÃO DO MOUSE FOR MAIOR QUE A POSIÇÃO X DA LOCALIZAÇÃO DA IMAGEM NA TELA E MENOR QUE A POSIÇÃO X MAIS A LARGURA
        #OU SEJA, SE ESTÁ DENTRO DA DIMENSÃO X DA IMAGEM NO PLANO CARTESIANO.
        #VERIFICAÇÃO 2 (ALTURA): SE A POSIÇÃO DO MOUSE FOR MAIOR QUE A POSIÇÃO Y DA LOCALIZAÇÃO DA IMAGEM NA TELA E MENOR QUE A POSIÇÃO Y MAIS A ALTURA
        #OU SEJA, SE ESTÁ DENTRO DA DIMENSÃO Y DA IMAGEM NO PLANO CARTESIANO.        
        if click[0] == 1: #DETECTA SE O CLICK FOI COM O BOTÃO ESQUERDO
            if menu_estado == 1:    #TELA MENU PRINCIPAL
                if y == 100:                #PLAY           #OK
                    menu_estado = 3     #ALTERA O ESTADO DO MENU PARA IR PARA A TELA PRÉ-FASE 1
                elif y == 200:              #RANCKING       #FAZER
                    menu_estado = 6     #ALTERA O ESTADO DO MENU PARA IR PARA A TELA COM O RANKING
                elif y == 300:              #SAIR           #OK
                    menu_estado = 5     #ALTERA O ESTADO DO MENU PARA FECHAR A TELA
                elif y == 583:              #SOM            #FAZER
                    if audio == True:   #ALTERNA A IMAGEM DO VOLUME PARA LIGADO/DESLIGADO
                        audio = False
                    else:
                        audio = True
                    print(audio)
                elif y == 588:              #INSTRUÇÕES     #OK
                    menu_estado = 2     #ALTERA O ESTADO DO MENU PARA IR PARA A TELA COM AS INTRUÇÕES
            elif menu_estado == 2 or menu_estado == 6:  #TELA INSTRUÇÕES E RANKING
                if y == 587 and x == 73:    #VOLTAR         #OK
                    menu_estado = 1     #ALTERA O ESTADO DO MENU PARA VOLTAR PARA A TELA COM O MENU PRINCIPAL
                elif y == 587 and x == 214: #PLAY           #OK
                    menu_estado = 3     #ALTERA O ESTADO DO MENU PARA IR PARA A TELA PRÉ-FASE 1
            elif menu_estado == 3:  #TELA P/ ESCOLHER O PERSONAGEM
                if x == 100 and y ==100:
                    p = 1
                    menu_estado = 4     #ALTERA O ESTADO DO MENU PARA IR PARA A TELA DA FASE 1
                elif x == 225 and y == 100:
                    p = 2
                    menu_estado = 4     #ALTERA O ESTADO DO MENU PARA IR PARA A TELA DA FASE 1
                elif x == 100 and y == 200:
                    p = 3
                    menu_estado = 4     #ALTERA O ESTADO DO MENU PARA IR PARA A TELA DA FASE 1
                elif x == 225 and y == 200:
                    p = 4
                    menu_estado = 4     #ALTERA O ESTADO DO MENU PARA IR PARA A TELA DA FASE 1
                elif x == 163 and y == 300:
                    p = 5
                    menu_estado = 4     #ALTERA O ESTADO DO MENU PARA IR PARA A TELA DA FASE 1
                elif y == 587 and x == 73:  #VOLTAR         #OK
                    menu_estado = 1     #ALTERA O ESTADO DO MENU PARA VOLTAR PARA A TELA COM O MENU PRINCIPAL
                elif x == 215 and y == 588: #INSTRUÇÕES     #OK
                    menu_estado = 2     #ALTERA O ESTADO DO MENU PARA IR PARA A TELA COM AS INTRUÇÕES
                return p
        return menu_estado

def teclado(event,maze,screen,branco,player,total,q):
    global final
    global tempo_final
    global pos_p_y  #POSIÇÃO Y NO PLANO CARTESIANO DO PLAYER
    global pos_p_x  #POSIÇÃO X NO PLANO CARTESIANO DO PLAYER
    tecla = pygame.key.get_pressed()
    #if event.type == pygame.KEYDOWN: #DETECTA SE UMA TECLA FOI PRESSIONADA
    if tecla[K_RIGHT]:     #SE A TECLA PRESSIONADA FOR A SETA DIREITA
        print("direita")    #O PLAYER DESLOCARIA 1 NO X PARA DIREITA, ENTÃO X SOMA 1
        if maze[pos_p_y][(pos_p_x + 1)] == 0: #VERIFICA SE X+1 É UMA PAREDE OU CAMINHO
            print("caminho livre") #SE SIM
            pygame.draw.rect(screen,branco,((pos_p_x * q),(pos_p_y * q),q,q)) #DESENHA UM QUADRADO BRANCO NA POSIÇÃO ANTIGA
            pygame.display.flip()
            pos_p_x += 1  #ATUALIZA A POSIÇÃO DO PLAYER
            screen.blit(player,((pos_p_x * q),(pos_p_y * q))) #ALTERA A POSIÇÃO DA IMAGEM PARA A NOVA POSIÇÃO
        else:
            print("parede")
            
    elif tecla[K_LEFT]:    #SE A TECLA PRESSIONADA FOR A SETA ESQUERDA
        print("ESQUERDA")   #O PLAYER DESLOCARIA 1 NO X PARA ESQUERDA, ENTÃO X SUBTRAI 1
        if maze[pos_p_y][(pos_p_x - 1)] == 0: #VERIFICA SE X-1 É UMA PAREDE OU CAMINHO
            print("caminho livre") #SE SIM
            pygame.draw.rect(screen,branco,((pos_p_x * q),(pos_p_y * q),q,q)) #DESENHA UM QUADRADO BRANCO NA POSIÇÃO ANTIGA
            pygame.display.flip()
            pos_p_x -= 1 #ATUALIZA A POSIÇÃO DO PLAYER
            screen.blit(player,((pos_p_x * q),(pos_p_y * q))) #ALTERA A POSIÇÃO DA IMAGEM PARA A NOVA POSIÇÃO
        else:
            print("parede")

    elif tecla[K_UP]:      #SE A TECLA PRESSIONADA FOR A SETA PARA CIMA
        print("CIMA")       #O PLAYER DESLOCARIA 1 NO Y PARA CIMA, ENTÃO Y SUBTRAI 1
        if maze[(pos_p_y - 1)][pos_p_x] == 0: #VERIFICA SE Y-1 É UMA PAREDE OU CAMINHO
            print("caminho livre") #SE SIM
            pygame.draw.rect(screen,branco,((pos_p_x * q),(pos_p_y * q),q,q)) #DESENHA UM QUADRADO BRANCO NA POSIÇÃO ANTIGA
            pygame.display.flip()
            pos_p_y -= 1 #ATUALIZA A POSIÇÃO DO PLAYER
            screen.blit(player,((pos_p_x * q),(pos_p_y * q))) #ALTERA A POSIÇÃO DA IMAGEM PARA A NOVA POSIÇÃO
        else:
            print("parede")

    elif tecla[K_DOWN]:    #SE A TECLA PRESSIONADA FOR A SETA PARA BAIXO
        print("BAIXO")      #O PLAYER DESLOCARIA 1 NO Y PARA BAIXO, ENTÃO Y SOMA 1
        if maze[(pos_p_y + 1)][pos_p_x] == 0: #VERIFICA SE Y+1 É UMA PAREDE OU CAMINHO
            print("caminho livre") #SE SIM
            pygame.draw.rect(screen,branco,((pos_p_x * q),(pos_p_y * q),q,q)) #DESENHA UM QUADRADO BRANCO NA POSIÇÃO ANTIGA
            pygame.display.flip()
            pos_p_y += 1 #ATUALIZA A POSIÇÃO DO PLAYER
            screen.blit(player,((pos_p_x * q),(pos_p_y * q))) #ALTERA A POSIÇÃO DA IMAGEM PARA A NOVA POSIÇÃO
        elif maze[(pos_p_y + 1)][pos_p_x] == 2: #VERIFICA SE O PLAYER CHEGOU NO FINAL (SEMPRE DESCENDO)
            print("FIM <3")
            tempo_final += total #GRAVA O VALOR DO TEMPO FINAL
            print("Tempo da Fase 3: ",tempo_final)
            pos_p_x = 2 #VOLTA PARA A POSIÇÃO INICIAL
            pos_p_y = 3 #VOLTA PARA A POSIÇÃO INICIAL
            #final = True
            #fim() #CHAMA A ÚLTIMA TELA
        else:
            print("parede")
        pygame.display.flip()
        
def func_Fase1(player,img_player):
    global fase1
    global fase
    while fase1 == True:
        if fase == 1:
            player = pygame.transform.scale(img_player,(27,27))
            if fase1 == True:
                #VARIAVEIS PARA CONTROLAR O TEMPO DO JOGO
                relogio = pygame.time.Clock()
                fonte = pygame.font.Font(None, 25)
                m = 0
                s = 60
                total = 0
                screen = pygame.display.set_mode((560,700)) #REDIMENSIONA O TAMANHO DA TELA
                pygame.display.set_caption("Labirinto")
                branco = (255,255,255)
                preto = (0,0,0)
                screen.fill(branco)
            lab_fase1(screen,maze,preto,player)
        
        
            if total < 150:
                for event in pygame.event.get():
                    teclado(event,maze,screen,branco,player,total,27) #CHAMA A FUNÇÃO DE TECLADO
                    
                if fase3 == False:
                    break
                #CONFIGURA O RELÓGIO
                total = m // s
                minutos = total // 60
                segundos = total % 60
                saida = "Tempo: {0:02}:{1:02}".format(minutos, segundos)
                texto = fonte.render(saida, True, (0,0,0))
                info_fase = fonte.render("FASE 1   -   TEMPO LIMITE: 1 MIN e 30 SEG", True, (0,0,0))
                pygame.display.flip()
                pygame.draw.rect(screen,branco,(540,680,200,20)) #DESENHA UM QUADRADO BRANCO PARA ATUALIZAR A FONTE DO RELÓGIO EM CIMA
                screen.blit(texto, (540,680))
                screen.blit(info_fase, (20,680))
                m += 1
                relogio.tick(50)
                pygame.display.flip()
            else:
                print("Tempo acabou")



def arquivo_Menu(): #CRIA A TELA DE MENU, COM OS BOTÕES DE ACORDO COM O ESTADO DO MENU
    global menu_estado      #VARIAVEL QUE DETERMINA O QUE APARECE NA TELA DO MENU
    global running
    global fase
    global fase1
    global fase2
    global fase3
    fase = 1
    final = False
    fase1 = False
    fase2 = False
    fase3 = False
    while running:
        for event in pygame.event.get():
            screen.fill((255,255,255))
            fundoMenu = pygame.image.load(os.path.join('Imagens/FundoMenu.png'))
            screen.blit(fundoMenu,(1,1))
            if event.type == pygame.QUIT:#FECHAR A TELA NO X
                menu_estado = 5     #ALTERA O ESTADO DO MENU PARA FECHAR A TELA
            if menu_estado == 1:    #TELA MENU PRINCIPAL
                menu_principal(screen,audio)    #ADICIONA OS BOTÕES DO MENU PRINCIPAL (ARQUIVO: funcoes)
                button(250,96,61,100)   #PCHAMA A FUNÇÃO DOS BOTÕES COM AS COORDENADAS DO BOTÃO LAY
                button(250,96,61,200)   #CHAMA A FUNÇÃO DOS BOTÕES COM AS COORDENADAS DO BOTÃO SCORE
                button(250,96,61,300)   #CHAMA A FUNÇÃO DOS BOTÕES COM AS COORDENADAS DO BOTÃO EXIT
                button(96,96,73,583)    #CHAMA A FUNÇÃO DOS BOTÕES COM AS COORDENADAS DO BOTÃO SOM
                button(96,96,215,588)   #CHAMA A FUNÇÃO DOS BOTÕES COM AS COORDENADAS DO BOTÃO INSTRUCOES
            elif menu_estado == 2:  #TELA INSTRUÇÕES
                intrucoes(screen)               #ADICIONA OS OBJETOS DA TELA DE INSTRUÇÕES (ARQUIVO: funcoes)
                button(96,96,73,587)    #CHAMA A FUNÇÃO DOS BOTÕES COM AS COORDENADAS DO BOTÃO VOLTAR
                button(96,96,214,587)   #CHAMA A FUNÇÃO DOS BOTÕES COM AS COORDENADAS DO BOTÃO PLAY
            elif menu_estado == 3:  #TELA P/ ESCOLHER PERSONAGEM
                play(screen)                    #ADICIONA OS OBJETOS DA TELA PRÉ-FASE 1 (ARQUIVO: funcoes)
                button(47,47,100,100)   #CHAMA A FUNÇÃO DOS BOTÕES COM AS COORDENADAS DO BOTÃO P1
                button(47,47,225,100)   #CHAMA A FUNÇÃO DOS BOTÕES COM AS COORDENADAS DO BOTÃO P2
                button(47,47,100,200)   #CHAMA A FUNÇÃO DOS BOTÕES COM AS COORDENADAS DO BOTÃO P3
                button(47,47,225,200)   #CHAMA A FUNÇÃO DOS BOTÕES COM AS COORDENADAS DO BOTÃO P4
                button(47,47,163,300)   #CHAMA A FUNÇÃO DOS BOTÕES COM AS COORDENADAS DO BOTÃO 94
                button(96,96,73,587)    #CHAMA A FUNÇÃO DOS BOTÕES COM AS COORDENADAS DO BOTÃO VOLTAR
                button(96,96,215,588)   #CHAMA A FUNÇÃO DOS BOTÕES COM AS COORDENADAS DO BOTÃO INSTRUCOES
            elif menu_estado == 4:  #TELA FASE 1                                                        **********************
                #COLOCA NA VARIÁVEL PLAYER A IMAGEM ESCOLHIDA NA TELA PRÉ-FASE 1
                if p == 1:
                    img_player = pygame.image.load(os.path.join('Imagens/player1.png'))
                elif p == 2:
                    img_player = pygame.image.load(os.path.join('Imagens/player2.png'))
                elif p == 3:
                    img_player = pygame.image.load(os.path.join('Imagens/player3.png'))
                elif p == 4:
                    img_player = pygame.image.load(os.path.join('Imagens/player4.png'))
                elif p == 5:
                    img_player = pygame.image.load(os.path.join('Imagens/player5.png'))
                fase1 = True
                player = pygame.transform.scale(img_player,(16,16))
                
                print("fase 1")
                func_Fase1(player,img_player)
                
            elif menu_estado == 5:  #FECHAR A TELA
                final = False
                fase2 = False
                fase3 = False
                running = False
            elif menu_estado == 6:  #TELA RANKING
                ranking(screen)                 #ADICIONA OS OBJETOS DA TELA COM O RANKING (ARQUIVO: funcoes)
                button(96,96,73,587)    #CHAMA A FUNÇÃO DOS BOTÕES COM AS COORDENADAS DO BOTÃO VOLTAR
                button(96,96,214,587)   #CHAMA A FUNÇÃO DOS BOTÕES COM AS COORDENADAS DO BOTÃO PLAY
                  
            pygame.display.flip()

running = True
final = False
fase1 = False
fase2 = False
fase3 = False
audio = True
total = 0
menu_estado = 1
p = 0
tempo_final = 0
fase = 1

arquivo_Menu()

print("fechar")
screen.fill((255,255,255))
pygame.quit()
quit()








