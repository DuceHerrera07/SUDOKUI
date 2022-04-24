import pygame

Fondo_blanco=(255,255,255)
color_negro= (0, 0, 0)
tamaño_Cuadro= 80
pygame.init()
size = (600, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Grid on PYGAME")
clock = pygame.time.Clock()
gameOver = False#BANDERA
while not gameOver:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = True
    screen.fill(color_negro)
    for i in range(1, size[0], tamaño_Cuadro + 1):
        for j in range(1, size[1], tamaño_Cuadro + 1):
            pygame.draw.rect(screen,Fondo_blanco, [i, j, tamaño_Cuadro, tamaño_Cuadro], 0)
    pygame.display.flip()
    clock.tick(1)
pygame.quit()