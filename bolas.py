import pygame as pg
import random

class Bola:
    def __init__(self, x, y, w=25, h=25, color = (255, 255, 255)):
        self.x = x
        self.y = y
        self.w = w 
        self.h = h 
        self.color = color

        self.vx = 0
        self.vy = 0

    def velocidad(self, vx, vy):
        self.vx = vx
        self.vy = vy 

    def mover (self, xmax, ymax):
        self.x += self.vx   
        self.y += self.vy

        if self.x <= 0 or self.x >= xmax - self.w:
            self.vx *= -1
        if self.y <= 0 or self.y >= xmax - self.h:
            self.vy *= -1    


pg.init()

pantalla_principal = pg.display.set_mode((800,600))
pg.display.set_caption("Bolitas rebotando")


bola = Bola(400, 300, h=50, color=(255, 255, 0))
bola.velocidad(5, 5)

bola1 = Bola(300, 300, 35, 35, (0,255,0))
bola1.velocidad(random.randint(-10, 10), random.randint(-10, 10))


game_over= False
while not game_over:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            game_over = True


    pantalla_principal.fill((0, 0, 255))
    bola.mover(800,600)
    bola1.mover(800,600)
    

    pg.draw.rect(pantalla_principal, bola.color, (bola.x,bola.y,bola.w,bola.h))
    pg.draw.rect(pantalla_principal, bola1.color, (bola1.x,bola1.y,bola1.w,bola1.h))
    pg.display.flip()
    


pg.quit()

