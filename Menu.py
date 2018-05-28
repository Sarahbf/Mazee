'''
http://pt.audiomicro.com/comedia-com-efeitos-retro-pinga-cartoons-quadrinhos-funny-comedia-com-efeitos-retro-gotejamento-efeitos-sonoros-gratuitos-39633
TAMANHO DA TELA = 656x656
TAMANHO DA MATRIZ = 41x41
TAMANHO DE CADA QUADRADO = 16x16
'''
from time import sleep
import pygame
import sys
import os
from pygame import *
from labirinto_estrutura1 import *
from labirinto_estrutura2 import *
from labirinto_estrutura3 import *
from arq_ranking import *
from funcoes import *
import csv

pygame.init()
pygame.display.init()
screen = pygame.display.set_mode((372,750))
pygame.display.set_caption("Menu")
screen.fill((255,255,255))
mixer.init()
mixer.music.load('aqv_som.wav')


running = True
audio = True

menu_estado = 1 #VARIAVEL QUE DETERMINA O QUE APARECE NA TELA DO MENU
p = 0 #VARIAVEL QUE DETERMINA O PLAYER
tempo_final = 0


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
                elif y == 300:              #CREDITOS       #FAZER
                    menu_estado = 6     #ALTERA O ESTADO DO MENU PARA IR PARA A TELA COM OS CREDITOS
                elif y == 225:              #SAIR           #OK
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

def teclado(event,screen,branco,player,total,maze,q):
    global final,fase1,fase2,fase3,audio
    global tempo_final
    global pos_p_y  #POSIÇÃO Y NO PLANO CARTESIANO DO PLAYER
    global pos_p_x  #POSIÇÃO X NO PLANO CARTESIANO DO PLAYER
    fonte = pygame.font.Font(None, 25)
    tecla = pygame.key.get_pressed()
    if tecla[K_RIGHT]:     #SE A TECLA PRESSIONADA FOR A SETA DIREITA
        if audio == True:
            print("on")
            mixer.music.play()
        else:
            print("off")
        print("direita")    #O PLAYER DESLOCARIA 1 NO X PARA DIREITA, ENTÃO X SOMA 1
        if maze[pos_p_y][(pos_p_x + 1)] == 0: #VERIFICA SE X+1 É UMA PAREDE OU CAMINHO
            print("caminho livre") #SE SIM
            pygame.draw.rect(screen,branco,((pos_p_x * q),(pos_p_y * q),q,q)) #DESENHA UM QUADRADO BRANCO NA POSIÇÃO ANTIGA
            pygame.display.flip()
            pos_p_x += 1  #ATUALIZA A POSIÇÃO DO PLAYER
            screen.blit(player,((pos_p_x * q),(pos_p_y * q))) #ALTERA A POSIÇÃO DA IMAGEM PARA A NOVA POSIÇÃO
        elif maze[pos_p_y][(pos_p_x + 1)] == 2: #VERIFICA SE O PLAYER CHEGOU NO FINAL (SEMPRE DESCENDO)
            print("ir para fase 3")
            tempo_final += total #GRAVA O VALOR DO TEMPO FINAL
            print("Tempo da Fase 2: ",total)
            print("Tempo Total: ",tempo_final)
            pos_p_x = 2 #VOLTA PARA A POSIÇÃO INICIAL
            pos_p_y = 3 #VOLTA PARA A POSIÇÃO INICIAL
            fase1 = False
            fase2 = False
            fase3 = True
            pygame.draw.rect(screen,branco,(20,600,800,1000)) #DESENHA UM QUADRADO BRANCO PARA ATUALIZAR A FONTE DO RELÓGIO EM CIMA
            info_pfase = fonte.render("Prepare-se para a última fase!", True, (0,0,0))
            screen.blit(info_pfase, (20,600))
            pygame.display.flip()
            sleep(1)
            func_lab_fase3(player)
        else:
            print("parede")

    elif tecla[K_LEFT]:    #SE A TECLA PRESSIONADA FOR A SETA ESQUERDA
        if audio == True:
            print("on")
            mixer.music.play()
        else:
            print("off")
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
        if audio == True:
            print("on")
            mixer.music.play()
        else:
            print("off")
        print("CIMA")       #O PLAYER DESLOCARIA 1 NO Y PARA CIMA, ENTÃO Y SUBTRAI 1
        if maze[(pos_p_y - 1)][pos_p_x] == 0: #VERIFICA SE Y-1 É UMA PAREDE OU CAMINHO
            print("caminho livre") #SE SIM
            pygame.draw.rect(screen,branco,((pos_p_x * q),(pos_p_y * q),q,q)) #DESENHA UM QUADRADO BRANCO NA POSIÇÃO ANTIGA
            pygame.display.flip()
            pos_p_y -= 1 #ATUALIZA A POSIÇÃO DO PLAYER
            screen.blit(player,((pos_p_x * q),(pos_p_y * q))) #ALTERA A POSIÇÃO DA IMAGEM PARA A NOVA POSIÇÃO
        elif maze[(pos_p_y - 1)][pos_p_x] == 2: #VERIFICA SE O PLAYER CHEGOU NO FINAL (SEMPRE DESCENDO)
            print("ir para fase 2")
            tempo_final += total #GRAVA O VALOR DO TEMPO FINAL
            print("Tempo da Fase 1: ",tempo_final)
            fase1 = False
            fase2 = True
            pos_p_x = 1     #POSIÇÃO INICIAL X NO PLANO CARTESIANO DO PLAYER
            pos_p_y = 1     #POSIÇÃO INICIAL Y NO PLANO CARTESIANO DO PLAYER
            pygame.draw.rect(screen,branco,(20,600,800,1000)) #DESENHA UM QUADRADO BRANCO PARA ATUALIZAR A FONTE DO RELÓGIO EM CIMA
            info_pfase = fonte.render("Prepare-se para a próxima fase!", True, (0,0,0))
            screen.blit(info_pfase, (20,600))
            pygame.display.flip()
            sleep(1)
            func_lab_fase2(player)
        else:
            print("parede")

    elif tecla[K_DOWN]:    #SE A TECLA PRESSIONADA FOR A SETA PARA BAIXO
        if audio == True:
            print("on")
            mixer.music.play()
        else:
            print("off")
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
            final = True
            fim() #CHAMA A ÚLTIMA TELA
        else:
            print("parede")
        pygame.display.flip()

def func_lab_fase1(player):
    global fase1,pos_p_x,pos_p_y
    global final_perdeu
    pos_p_x = 2     #POSIÇÃO INICIAL X NO PLANO CARTESIANO DO PLAYER
    pos_p_y = 3     #POSIÇÃO INICIAL Y NO PLANO CARTESIANO DO PLAYER
    if fase1 == True:
        #VARIAVEIS PARA CONTROLAR O TEMPO DO JOGO
        relogio = pygame.time.Clock()
        fonte = pygame.font.Font(None, 25)
        m = 0
        s = 60
        total = 0
        screen = pygame.display.set_mode((560,680)) #REDIMENSIONA O TAMANHO DA TELA
        pygame.display.set_caption("Labirinto")
        branco = (235,199,158)
        preto = (0,0,0)
        screen.fill(branco)
        fase1 = True
    
    lab_fase1(screen,maze1,preto,player) #DESENHA O LABIRINTO (ARQUIVO: labirinto_estrutura1)
    
    while fase1 == True:
        maze = maze1
        q = 27
        if total < 90:
            for event in pygame.event.get():
                teclado(event,screen,branco,player,total,maze,q) #CHAMA A FUNÇÃO DE TECLADO
            if fase1 == False:
                break
            #CONFIGURA O RELÓGIO
            total = m // s
            minutos = total // 60
            segundos = total % 60
            saida = "Tempo: {0:02}:{1:02}".format(minutos, segundos)
            texto = fonte.render(saida, True, (0,0,0))
            info_fase = fonte.render("FASE 1   -   TEMPO LIMITE: 1 MINUTO E 30 SEGUNDOS", True, (0,0,0))
            pygame.display.flip()
            pygame.draw.rect(screen,branco,(20,650,200,20)) #DESENHA UM QUADRADO BRANCO PARA ATUALIZAR A FONTE DO RELÓGIO EM CIMA
            screen.blit(texto, (20,650))
            screen.blit(info_fase, (20,600))
            m += 1
            relogio.tick(50)
            pygame.display.flip()
        else:
            print("Tempo acabou")
            pygame.draw.rect(screen,branco,(20,600,800,1000)) #DESENHA UM QUADRADO BRANCO PARA ATUALIZAR O TEXTO
            info_pfase = fonte.render("Tempo esgotado! Você será redirecionado para o menu.", True, (0,0,0))
            screen.blit(info_pfase, (20,600))
            fase1 = False
            final_perdeu = True
            menu_estado = 1
            pygame.display.flip()
            tela_fim_perdeu()

def func_lab_fase2(player):
    player = pygame.transform.scale(player,(16,16))
    pos_p_x = 1     #POSIÇÃO INICIAL X NO PLANO CARTESIANO DO PLAYER
    pos_p_y = 1     #POSIÇÃO INICIAL Y NO PLANO CARTESIANO DO PLAYER
    global fase2,fase1,final_perdeu
    if fase2 == True:
        #VARIAVEIS PARA CONTROLAR O TEMPO DO JOGO
        relogio = pygame.time.Clock()
        fonte = pygame.font.Font(None, 25)
        m = 0
        s = 60
        total = 0
        screen = pygame.display.set_mode((560,680)) #REDIMENSIONA O TAMANHO DA TELA
        pygame.display.set_caption("Labirinto")
        branco = (247,202,201)
        preto = (0,0,0)
        screen.fill(branco)
        fase2 = True
    
    lab_fase2(screen,maze2,preto,player) #DESENHA O LABIRINTO (ARQUIVO: labirinto_estrutura2)
    
    while fase2 == True:
        maze = maze2
        q = 16
        if total < 180:
            for event in pygame.event.get():
                teclado(event,screen,branco,player,total,maze,q) #CHAMA A FUNÇÃO DE TECLADO
            if fase2 == False:
                break
            #CONFIGURA O RELÓGIO
            total = m // s
            minutos = total // 60
            segundos = total % 60
            saida = "Tempo: {0:02}:{1:02}".format(minutos, segundos)
            texto = fonte.render(saida, True, (0,0,0))
            info_fase = fonte.render("FASE 2   -   TEMPO LIMITE: 3 MINUTOS", True, (0,0,0))
            pygame.display.flip()
            pygame.draw.rect(screen,branco,(20,650,200,20)) #DESENHA UM QUADRADO BRANCO PARA ATUALIZAR A FONTE DO RELÓGIO EM CIMA
            screen.blit(texto, (20,650))
            screen.blit(info_fase, (20,600))
            m += 1
            relogio.tick(50)
            pygame.display.flip()
        else:
            print("Tempo acabou")
            pygame.draw.rect(screen,branco,(20,600,800,1000)) #DESENHA UM QUADRADO BRANCO PARA ATUALIZAR O TEXTO
            info_pfase = fonte.render("Tempo esgotado! Você será redirecionado para o menu.", True, (0,0,0))
            screen.blit(info_pfase, (20,600))
            fase1 = False
            fase2 = False
            final_perdeu = True
            menu_estado = 1
            pygame.display.flip()
            return tela_fim_perdeu()

def func_lab_fase3(player):
    player = pygame.transform.scale(player,(14,14))
    global fase3,fase2,fase1,final_perdeu
    if fase3 == True:
        #VARIAVEIS PARA CONTROLAR O TEMPO DO JOGO
        relogio = pygame.time.Clock()
        fonte = pygame.font.Font(None, 25)
        m = 0
        s = 60
        total = 0
        screen = pygame.display.set_mode((560,680)) #REDIMENSIONA O TAMANHO DA TELA
        pygame.display.set_caption("Labirinto")
        branco = (50,153,204)
        preto = (0,0,0)
        screen.fill(branco)
        fase3 = True
    
    lab_fase3(screen,maze3,preto,player) #DESENHA O LABIRINTO (ARQUIVO: labirinto_estrutura3)
    
    while fase3 == True:
        maze = maze3
        pos_p_x = 2     #POSIÇÃO INICIAL X NO PLANO CARTESIANO DO PLAYER
        pos_p_y = 3     #POSIÇÃO INICIAL Y NO PLANO CARTESIANO DO PLAYER
        q = 14
        if total < 300:
            for event in pygame.event.get():
                teclado(event,screen,branco,player,total,maze,q) #CHAMA A FUNÇÃO DE TECLADO
            if fase3 == False:
                break
            #CONFIGURA O RELÓGIO
            total = m // s
            minutos = total // 60
            segundos = total % 60
            saida = "Tempo: {0:02}:{1:02}".format(minutos, segundos)
            texto = fonte.render(saida, True, (0,0,0))
            info_fase = fonte.render("FASE 3   -   TEMPO LIMITE: 5 MINUTOS", True, (0,0,0))
            pygame.display.flip()
            pygame.draw.rect(screen,branco,(20,650,200,20)) #DESENHA UM QUADRADO BRANCO PARA ATUALIZAR A FONTE DO RELÓGIO EM CIMA
            screen.blit(texto, (20,650))
            screen.blit(info_fase, (20,600))
            m += 1
            relogio.tick(50)
            pygame.display.flip()
        else:
            print("Tempo acabou")
            pygame.draw.rect(screen,branco,(20,600,800,1000)) #DESENHA UM QUADRADO BRANCO PARA ATUALIZAR O TEXTO
            info_pfase = fonte.render("Tempo esgotado! Você será redirecionado para o menu.", True, (0,0,0))
            screen.blit(info_pfase, (20,600))
            fase1 = False
            fase2 = False
            fase3 = False
            final_perdeu = True
            menu_estado = 1
            pygame.display.flip()
            tela_fim_perdeu()

def fim():
    global menu_estado      #VARIAVEL QUE DETERMINA O QUE APARECE NA TELA DO MENU
    global final,tempo_final
    lista_ranking = []
    #REDIMENSIONA A TELA
    tela_fim = pygame.display.set_mode((372,750))
    pygame.display.set_caption("Menu")
    tela_fim.fill((255,255,255))

    def botao(w,h,x,y):
        mouse = pygame.mouse.get_pos() #DETECTA A POSIÇÃO DO MOUSE
        click = pygame.mouse.get_pressed() #DETECTA SE CLICKAMOS COMO MOUSE
        if x+w > mouse[0] > x and y+h > mouse[1] > y:
            if click[0] == 1:
                if y == 350: #Ranking
                    print("Ranking")
                    func_ranking(screen)
                    
                elif y == 620: #MENU
                    print("menu")
                    final = False
                    arquivo_Menu()

    while final == True:
        for event in pygame.event.get():
            fundoMenu = pygame.image.load(os.path.join('Imagens/FundoMenu.png'))
            tela_fim.blit(fundoMenu,(1,1))
            if event.type == pygame.QUIT: #FUNÇÃO PARA FECHAR A TELA
                print("sair")
                menu_estado = 5  #ALTERA O ESTADO DO MENU PARA FECHAR A TELA
                final = False
                fase3 = False
                running = False
                break
            
            imgRanking = pygame.image.load(os.path.join('Imagens/BtnRanking.png'))#CARREGA A IMAGEM DO BOTÃO SAIR
            tela_fim.blit(imgRanking,(61,350))     #EXIBE A IMAGEM DO BOTÃO
            imgMenu = pygame.image.load(os.path.join('Imagens/BtnMenu.png')) #CARREGA A IMAGEM DO BOTÃO MENU
            imgMenu_ = pygame.transform.scale(imgMenu,(128,48)) #REDIMENSIONA O TAMANHO DA IMAGEM DO BOTÃO SAIR
            tela_fim.blit(imgMenu_,(122,620))    #EXIBE A IMAGEM DO BOTÃO

            #main(screen)
            font = pygame.font.Font(None, 32)
            clock = pygame.time.Clock()
            input_box = pygame.Rect(100, 100, 130, 32)
            color_inactive = pygame.Color('lightskyblue3')
            color_active = pygame.Color('dodgerblue2')
            color = color_inactive
            active = False
            text = ''
            done = False
            try:
                nome_arquivo = ('ranking.txt')
                arquivo = open(nome_arquivo, 'a')
            except FileNotFoundError:
                print("Entrou")
                #arquivo = open(nome_arquivo, 'r')
                #arquivo.writelines(u'Arquivo criado pois nao existia')
            while not done:
                for event in pygame.event.get():
                    botao(250,96,61,350)   #CHAMA A FUNÇÃO DOS BOTÕES COM AS COORDENADAS DO BOTÃO MENU
                    botao(128,48,122,620)  #CHAMA A FUNÇÃO DOS BOTÕES COM AS COORDENADAS DO BOTÃO SAIR
                    pygame.display.flip()
                    menu_estado = 1     #ALTERA O ESTADO DO MENU PARA VOLTAR PARA O MENU PRICINPAL
                    if final == False:
                        break
                    if event.type == pygame.QUIT:
                        done = True
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if input_box.collidepoint(event.pos):
                            active = not active
                        else:
                            active = False
                        color = color_active if active else color_inactive
                    if event.type == pygame.KEYDOWN:
                        if active:
                            if event.key == pygame.K_RETURN:
                                print("Nome: " , text)
                                jogador = text
                                arquivo.write(text)
                                arquivo.write("\n")
                                arquivo.close()
                                text = ''
                                #done = True
                                gravar_ranking(jogador, tempo_final)
                                
                            elif event.key == pygame.K_BACKSPACE:
                                text = text[:-1]
                            else:
                                text += event.unicode
                txt_surface = font.render(text, True, color)
                width = max(200, txt_surface.get_width()+10)
                input_box.w = width
                screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
                pygame.draw.rect(screen, color, input_box, 2)
                pygame.display.flip()
                clock.tick(30)
            
            
    return arquivo_Menu()   #CHAMA A FUNÇÃO QUE EXIBE O MENU PRINCIPAL

def tela_fim_perdeu():
    x = 1
    global menu_estado      #VARIAVEL QUE DETERMINA O QUE APARECE NA TELA DO MENU
    global final_perdeu
    #REDIMENSIONA A TELA
    tela_fim = pygame.display.set_mode((372,750))
    pygame.display.set_caption("Menu")
    tela_fim.fill((255,255,255))
    img_perdeu = pygame.image.load(os.path.join('Imagens/texto_perdeu.png'))
    pygame.display.flip()

    def botao(w,h,x,y):
        mouse = pygame.mouse.get_pos() #DETECTA A POSIÇÃO DO MOUSE
        click = pygame.mouse.get_pressed() #DETECTA SE CLICKAMOS COMO MOUSE
        if x+w > mouse[0] > x and y+h > mouse[1] > y:
            if click[0] == 1:
                if y == 350: #Menu
                    print("menu")
                    final = False
                    arquivo_Menu()
                elif y == 620: #MENU
                    print("sair")
                    final_perdeu = False
                    fase2 = False
                    fase3 = False
                    fase1 = False
                    running = False
                    return final_perdeu
                
    while  final_perdeu == True:            
        for event in pygame.event.get():
            fundoMenu = pygame.image.load(os.path.join('Imagens/FundoMenu.png'))
            tela_fim.blit(fundoMenu,(1,1))
            tela_fim.blit(img_perdeu,(1,1))
            if event.type == pygame.QUIT: #FUNÇÃO PARA FECHAR A TELA
                print("sair")
                menu_estado = 5  #ALTERA O ESTADO DO MENU PARA FECHAR A TELA
                final_perdeu = False
                fase3 = False
                fase1 = False
                fase2 = False
                running = False
                break
            
            imgMenu = pygame.image.load(os.path.join('Imagens/BtnMenu.png')) #CARREGA A IMAGEM DO BOTÃO MENU
            tela_fim.blit(imgMenu,(61,350))     #EXIBE A IMAGEM DO BOTÃO
            imgExit_ = pygame.image.load(os.path.join('Imagens/BtnExit.png'))#CARREGA A IMAGEM DO BOTÃO SAIR
            imgExit = pygame.transform.scale(imgExit_,(128,48)) #REDIMENSIONA O TAMANHO DA IMAGEM DO BOTÃO SAIR
            tela_fim.blit(imgExit,(122,620))    #EXIBE A IMAGEM DO BOTÃO

            botao(250,96,61,350)   #CHAMA A FUNÇÃO DOS BOTÕES COM AS COORDENADAS DO BOTÃO MENU
            botao(128,48,122,620)  #CHAMA A FUNÇÃO DOS BOTÕES COM AS COORDENADAS DO BOTÃO SAIR
            pygame.display.flip()
            menu_estado = 1     #ALTERA O ESTADO DO MENU PARA VOLTAR PARA O MENU PRICINPAL
            if final_perdeu == False:
                break
        
        
    return arquivo_Menu()   #CHAMA A FUNÇÃO QUE EXIBE O MENU PRINCIPAL

def arquivo_Menu(): #CRIA A TELA DE MENU, COM OS BOTÕES DE ACORDO COM O ESTADO DO MENU
    global menu_estado      
    global running, fase1, fase2, fase3, final_perdeu,tempo_final
    final_perdeu = False
    final = False
    fase1 = False
    fase2 = False
    fase3 = False
    tempo_final = 0
    while running:
        for event in pygame.event.get():
            screen.fill((255,255,255))
            fundoMenu = pygame.image.load(os.path.join('Imagens/FundoMenu.png'))
            screen.blit(fundoMenu,(1,1))
            if event.type == pygame.QUIT:#FECHAR A TELA NO X
                menu_estado = 5     #ALTERA O ESTADO DO MENU PARA FECHAR A TELA
            if menu_estado == 1:    #TELA MENU PRINCIPAL
                menu_principal(screen,audio)    #ADICIONA OS BOTÕES DO MENU PRINCIPAL (ARQUIVO: funcoes)
                button(250,96,61,100)   #CHAMA A FUNÇÃO DOS BOTÕES COM AS COORDENADAS DO BOTÃO pLAY
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
            elif menu_estado == 6:  #TELA RANKING
                creditos(screen)                 #ADICIONA OS OBJETOS DA TELA COM O RANKING (ARQUIVO: funcoes)
                button(96,96,73,587)    #CHAMA A FUNÇÃO DOS BOTÕES COM AS COORDENADAS DO BOTÃO VOLTAR
                button(96,96,214,587)   #CHAMA A FUNÇÃO DOS BOTÕES COM AS COORDENADAS DO BOTÃO PLAY
            elif menu_estado == 5:  #FECHAR A TELA
                final = False
                fase1 = False
                fase2 = False
                fase3 = False
                running = False                
            elif menu_estado == 4:  #TELA FASE 1
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
                pos_p_x = 2     #POSIÇÃO INICIAL X NO PLANO CARTESIANO DO PLAYER
                pos_p_y = 3     #POSIÇÃO INICIAL Y NO PLANO CARTESIANO DO PLAYER
                
                final = True
                fase1 = True
                
                player = pygame.transform.scale(img_player,(27,27))
                print("fase 1")
                func_lab_fase1(player)
            
            pygame.display.flip()
    
arquivo_Menu()

print("fechar")
screen.fill((255,255,255))
pygame.quit()
quit()
