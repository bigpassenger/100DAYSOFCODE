import pygame
import sys

pygame.init()


screen = pygame.display.set_mode((300, 300))
white = (255, 255, 255)
screen.fill(white)


size = 1
color = (0, 0, 0)

def draw(method, name, args):
    global size, color
    if method == 'change':
        if name == 'size':
            size = int(args[0])  
        elif name == 'color':
            color = (int(args[0]), int(args[1]), int(args[2]))  
    elif method == 'draw':
        if name == 'line':
            pygame.draw.line(screen, color, (int(args[0]), int(args[1])), (int(args[2]), int(args[3])), size)
        elif name == 'circle':
            pygame.draw.circle(screen, color, (int(args[0]), int(args[1])), int(args[2]), size)
        elif name == 'polygon':
            points = [(int(args[i]), int(args[i + 1])) for i in range(0, len(args), 2)]
            pygame.draw.polygon(screen, color, points, size)
    pygame.display.update()

while True:
    order = input()
    if order == 'end drawing':
        pygame.image.save(screen, 'draw.png') 
        pygame.quit()
        sys.exit()
    else:
        parts = order.split()
        method = parts[0]  
        name = parts[1]  
        args = parts[2:]  
        draw(method, name, args)

