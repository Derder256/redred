import pygame 

WINDOW_SIZE = [800,600]
MAX_FPS(60)
window = pygame.Window("Tower Defense",WINDOW_SIZE)
surface = window.get_surface()
clock = pygame.Clock()
running = True
while running:
    for  event in pygame.evan.get():
        if event.type ==pygame.WINDOWCLOSE:
            running = False



    surface.fill("white") 



    window.flip()



    clock.tick(MAX_FPS)
    print(clock.get_fps())

