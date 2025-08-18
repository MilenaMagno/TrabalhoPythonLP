import pygame

print('Setup start')
pygame.init()
window = pygame.display.set_mode(size=(600, 480))
print ('Loop End')
print('Loop start')
while true:
    #check for all events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() #close window
            quit() #end pygame
