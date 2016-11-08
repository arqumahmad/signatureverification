import os
import pygame
from tablet import Tablet

pygame.init()

def main():
    """
    Simple Pygame to show off tablet pressure sensitivity.
    """
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Pressure Test")
    background = pygame.surface.Surface(screen.get_size())
    background.fill(pygame.Color("Black"))
    background = background.convert()
    screen.blit(background, (0,0))
    overlay = pygame.surface.Surface(screen.get_size(), flags=pygame.SRCALPHA, depth=32)
    overlay.convert_alpha()
    overlay.fill((0,0,0,0))

    # Create our tablet object:
    tablet = Tablet(screen)

    looping = True
    while looping:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                # allow for exit:
                looping = False

        overlay.fill((0,0,0,0))

        # Get our tablet data, and draw:
        tabletData = tablet.getData()
        # Debug print:

       # print tabletData



        button, x, y, pressure = tabletData

        
            print tabletData
            f1=open('temp.txt', 'a+')
            p=[]
            p= str(tabletData)
            f1.write(p + '\n')

        #Turn our pressure into a reasonabliy sized radius value:
        radius = 5
        # If user is pressing the LMB, draw:
        if button == 1 and pressure <=256:
            pygame.draw.circle(background, pygame.Color("green"), (x,y), radius)
        elif button == 1 and pressure >256 and pressure<=512:
            pygame.draw.circle(background, pygame.Color("blue"), (x,y), radius)
        elif button == 1 and pressure >512 and pressure <=1023:
            pygame.draw.circle(background, pygame.Color("red"), (x,y), radius)
        elif button == 0 and x!=0:
            pygame.draw.circle(background, pygame.Color("yellow"), (x,y), radius)

        # Draw our mouse pointer representation:
        pygame.draw.circle(overlay, pygame.Color("orange"), (x,y), 5)

        screen.blit(background, (0,0))
        screen.blit(overlay, (0,0))
        pygame.display.flip()

    pygame.quit()



if __name__ == "__main__":
    main()
