import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

pygame.mixer.music.set_volume(0.10)
pygame.mixer.music.load("BoxCat Games - Tricks.mp3")
pygame.mixer.music.play(-1)
barulho_colisao = pygame.mixer.Sound("smw_coin.wav")


largura = 1600
altura = 800
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Capture o Bandido")


fonte = pygame.font.SysFont("Arial", 40, True, True)
relogio = pygame.time.Clock()

x = largura / 2
y = altura / 2
x_azul = randint(40, 600)
y_azul = randint(50, 430)
fundo = pygame.transform.scale(
    pygame.image.load("banco.jpg"),
    (1600, 800)
)

pontos = 0


img_vermelho = pygame.transform.scale(
    pygame.image.load("pngegg (2).png"),
    (200, 200)
)
img_azul = pygame.transform.scale(
    pygame.image.load("pngegg (1).png"),
    (200, 200)
)


while True:
    relogio.tick(30)
    tela.fill((0, 0, 0))
    mensagem = f"Pontos: {pontos}"
    texto_formatado = fonte.render(mensagem, True, (0, 0, 0))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

   
    teclas = pygame.key.get_pressed()
    if teclas[K_a]:
        x -= 20
    if teclas[K_d]:
        x += 20
    if teclas[K_w]:
        y -= 20
    if teclas[K_s]:
        y += 20

    rect_vermelho = pygame.Rect(x, y, 200, 150)
    rect_azul = pygame.Rect(x_azul, y_azul, 40, 50)

    
    if rect_vermelho.colliderect(rect_azul):
        x_azul = randint(40, 1300)
        y_azul = randint(50, 600)
        pontos += 1
        barulho_colisao.play()

    tela.blit(fundo, (0, 0))
    tela.blit(img_vermelho, (x, y))
    tela.blit(img_azul, (x_azul, y_azul))
    tela.blit(texto_formatado, (400, 30))
   
    pygame.display.update()
