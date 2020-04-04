import sys, pygame
import os
import time
from Metodos import *
from Matrizes import *

_image_library = {}
pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont('arial', 30)
nome = pygame.font.SysFont('arial', 20)

screen = pygame.display.set_mode((550, 600))
clock = pygame.time.Clock()
resolvido = False

pygame.display.flip()

def exibe(mat):
    for i in range(9):
        for j in range(9):
            textsurface = myfont.render(str(mat[i][j]), False, (0, 0, 0))
            screen.blit(textsurface, ((56 * i) + 40,((56 * j) + 35)))

def get_image(path):
    global _image_library
    image = _image_library.get(path)
    if image == None:
        canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
        image = pygame.image.load(canonicalized_path)
        _image_library[path] = image
    return image

screen.fill((0, 168, 204))
pygame.display.flip()
screen.blit(get_image('background.png'), (20, 20))

def resolve(mat):
    l = [0, 0]
    if (not find_empty_location(mat, l)):
        return True

    row = l[0]
    col = l[1]

    for num in range(1, 10):

        if (verificacao(mat, row, col, num)):

            mat[row][col] = num
            screen.blit(get_image('background.png'), (20, 20))
            pygame.event.get()
            exibe(mat)
            pygame.display.flip()
            time.sleep(0.1)
            if (resolve(mat)):
                return True

            mat[row][col] = 0

    return False

exibe(matriz)
while not resolvido:
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            resolvido = True
    if(resolve(matriz)):
        screen.blit(get_image('background.png'), (20, 20))
        pygame.display.flip()
        exibe(matriz)
        textsurface = myfont.render('Resolvido!', False, (0, 0, 0))
        screen.blit(textsurface, (500, 600))
        pygame.display.flip()
        time.sleep(10)
        resolvido = True
    exibe(matriz)
    clock.tick(300)

screen.blit(get_image('background.png'), (20, 20))
pygame.display.flip()
