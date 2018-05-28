import csv
import pygame
def func_ranking(screen):
    texto = csv.reader(open("aqv_ranking.csv","r"))
    lista_ranking = []
    for i in texto:
        if len(i) == 0: continue
        lista_ranking.append(i)
    for num in lista_ranking:
        num[0] = int(num[0])
    lista_ranking.sort(reverse = True)
    ranking = True
    while ranking:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        if len(lista_ranking) < 5:
            for line in range(0,len(lista_ranking) ,1):
                print(lista_ranking[line])
        else:
            for line in range(5,0,1):
                print(lista_ranking[line])
        ranking = False



def gravar_ranking(jogador, tempo_final):
    with open(r'aqv_ranking.csv','a') as ranking_lab:
        writer = csv.writer(ranking_lab)
        writer.writerow([tempo_final,jogador])#escreve variavel com nome do jogador e pontos desviados
