import pygame
import time
import os
import sys
from pygame import *

pygame.init()
pygame.display.init()

def menu_principal(screen,audio): #IMAGENS DOS BOTÕES DA TELA DO MENU PRINCIPAL
    imgPlay = pygame.image.load(os.path.join('Imagens/BtnPlay.png'))    #CARREGA A IMAGEM DO BOTÃO PLAY
    screen.blit(imgPlay,(61,100))     #EXIBE A IMAGEM DO BOTÃO
    imgCreditos = pygame.image.load(os.path.join('Imagens/BtnCreditos.png'))  #CARREGA A IMAGEM DO BOTÃO RANKING
    screen.blit(imgCreditos,(138,350))     #EXIBE A IMAGEM DO BOTÃO
    imgExit = pygame.image.load(os.path.join('Imagens/BtnExit.png'))    #CARREGA A IMAGEM DO BOTÃO SAIR
    screen.blit(imgExit,(61,225))     #EXIBE A IMAGEM DO BOTÃO
    if audio == True:
        imgSom = pygame.image.load(os.path.join('Imagens/BtnSomOn.png'))    #CARREGA A IMAGEM DO BOTÃO SOM LIGADO
        screen.blit(imgSom,(73,583))     #EXIBE A IMAGEM DO BOTÃO
    else:
        imgSom = pygame.image.load(os.path.join('Imagens/BtnSomOff.png'))   #CARREGA A IMAGEM DO BOTÃO SOM DESLIGADO
        screen.blit(imgSom,(73,583))     #EXIBE A IMAGEM DO BOTÃO    
    imgInstrucoes = pygame.image.load(os.path.join('Imagens/BtnInstrucoes.png'))
    screen.blit(imgInstrucoes,(215,588))     #EXIBE A IMAGEM DO BOTÃO

def intrucoes(screen): #IMAGENS DOS BOTÕES DA TELA DE INTRUÇÕES
    txt_inst = pygame.image.load(os.path.join('Imagens/texto_instru.png'))#CARREGA A IMAGEM DO BOTÃO BOLTAR    
    screen.blit(txt_inst,(0,0))
    imgInstVoltar = pygame.image.load(os.path.join('Imagens/BtnInstVoltar.png'))#CARREGA A IMAGEM DO BOTÃO BOLTAR    
    screen.blit(imgInstVoltar,(73,587))     #EXIBE A IMAGEM DO BOTÃO
    imgInstPlay = pygame.image.load(os.path.join('Imagens/BtnInstPlay.png'))    #CARREGA A IMAGEM DO BOTÃO PLAY
    screen.blit(imgInstPlay,(214,587))     #EXIBE A IMAGEM DO BOTÃO

def play(screen): #IMAGENS DOS BOTÕES DA TELA PRÉ-FASE 1
    imgInstVoltar = pygame.image.load(os.path.join('Imagens/BtnInstVoltar.png'))#CARREGA A IMAGEM DO BOTÃO BOLTAR
    screen.blit(imgInstVoltar,(73,587))     #EXIBE A IMAGEM DO BOTÃO
    imgInstrucoes = pygame.image.load(os.path.join('Imagens/BtnInstrucoes.png'))#CARREGA A IMAGEM DO BOTÃO INSTRUÇÕES
    screen.blit(imgInstrucoes,(215,588))     #EXIBE A IMAGEM DO BOTÃO
    img_player1 = pygame.image.load(os.path.join('Imagens/player1.png'))    #CARREGA A IMAGEM DO BOTÃO PARA SELECIONAR O PLAYER 1
    screen.blit(img_player1,(100,100))     #EXIBE A IMAGEM DO BOTÃO
    img_player2 = pygame.image.load(os.path.join('Imagens/player2.png'))    #CARREGA A IMAGEM DO BOTÃO PARA SELECIONAR O PLAYER 2
    screen.blit(img_player2,(225,100))     #EXIBE A IMAGEM DO BOTÃO
    img_player3 = pygame.image.load(os.path.join('Imagens/player3.png'))    #CARREGA A IMAGEM DO BOTÃO PARA SELECIONAR O PLAYER 3
    screen.blit(img_player3,(100,200))     #EXIBE A IMAGEM DO BOTÃO
    img_player4 = pygame.image.load(os.path.join('Imagens/player4.png'))    #CARREGA A IMAGEM DO BOTÃO PARA SELECIONAR O PLAYER 4
    screen.blit(img_player4,(225,200))     #EXIBE A IMAGEM DO BOTÃO
    img_player5 = pygame.image.load(os.path.join('Imagens/player5.png'))    #CARREGA A IMAGEM DO BOTÃO PARA SELECIONAR O PLAYER 5
    screen.blit(img_player5,(163,300))     #EXIBE A IMAGEM DO BOTÃO

def creditos(screen): #IMAGENS DOS BOTÕES DA TELA COM O RANKING
    textoCredito = pygame.image.load(os.path.join('Imagens/TextoCreditos.png'))#CARREGA A IMAGEM DO BOTÃO BOLTAR
    screen.blit(textoCredito,(0,0))     #EXIBE A IMAGEM DO BOTÃO
    imgInstVoltar = pygame.image.load(os.path.join('Imagens/BtnInstVoltar.png'))#CARREGA A IMAGEM DO BOTÃO BOLTAR
    screen.blit(imgInstVoltar,(73,587))     #EXIBE A IMAGEM DO BOTÃO
    imgInstPlay = pygame.image.load(os.path.join('Imagens/BtnInstPlay.png'))    #CARREGA A IMAGEM DO BOTÃO BOLTAR
    screen.blit(imgInstPlay,(214,587))     #EXIBE A IMAGEM DO BOTÃO

def layout_ranking(screen): #IMAGENS DOS BOTÕES DA TELA DE INTRUÇÕES
    fundoMenu = pygame.image.load(os.path.join('Imagens/FundoMenu.png'))
    screen.blit(fundoMenu,(1,1))
    imgMenu = pygame.image.load(os.path.join('Imagens/BtnMenu.png')) #CARREGA A IMAGEM DO BOTÃO MENU
    imgMenu_ = pygame.transform.scale(imgMenu,(128,48)) #REDIMENSIONA O TAMANHO DA IMAGEM DO BOTÃO SAIR
    screen.blit(imgMenu_,(122,620))    #EXIBE A IMAGEM DO BOTÃO


#info_fase = fonte.render("FASE 1   -   TEMPO LIMITE: 1 MINUTO E 30 SEGUNDOS", True, (0,0,0))
#screen.blit(info_fase, (20,600))
