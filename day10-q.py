# import pygame

# pygame.init()
# img = pygame.image.load('sq.png')
# white = (250,250,250)
# screen = pygame.display.set_mode((400,400))
# screen.fill(white)

# x = 0
# y = 0
# step =0 
# t = int(input())
# pygame.display.update()

# while True:
#     screen.fill(white)
#     screen.blit(img,(x,y))
#     x = x + 1
#     y = y +1
#     step = step +1
#     if step == t:
#         pygame.image.save(screen,'out.png')
#     pygame.display.update()
#     pygame.time.delay(10)
#     pygame.event.pump()
#################################
# import pygame

# pygame.init()
# screen = pygame.display.set_mode((800, 600))
# events = []

# while True:
#     event = pygame.event.wait()
#     if event.type == pygame.QUIT:
#         print('Quit')

#     if event.type == pygame.KEYDOWN:
#         print('Key Down')
#         print(event.key)
#         print(event.unicode)

#     if event.type == pygame.KEYUP:
#         print('Key Up')
#         print(event.key)

#     if event.type == pygame.MOUSEBUTTONDOWN:
#         print('Mouse Button Down')
#         print(event.pos)
#         print(event.button == pygame.BUTTON_RIGHT)
#         print(event.button == pygame.BUTTON_LEFT)

#     if event.type == pygame.MOUSEBUTTONUP:
#         print('Mouse Button Up')
#         print(event.pos)
#         print(event.button == pygame.BUTTON_RIGHT)
#         print(event.button == pygame.BUTTON_LEFT)

#     if event.type == pygame.MOUSEMOTION:
#         print('Mouse Motion')
#         print(event.pos)
#         print(event.rel)

#     event = pygame.event.poll()
#     events.append(event)

# print(events)
#############################
import pygame

pygame.init()
screen = pygame.display.set_mode([500, 500])

while True:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            exit()
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)
    pygame.display.flip()