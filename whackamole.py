import pygame
import random

def main():
    try:
        pygame.init()
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        x=0
        y=0
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type==pygame.MOUSEBUTTONDOWN:
                    if (event.pos[0]//32,event.pos[1]//32)==(x/32,y/32):
                        x = random.randrange(0, 20) * 32
                        y = random.randrange(0, 16) * 32
            screen.fill("light green")
            screen.blit(mole_image, mole_image.get_rect(topleft=(x+3, y+3)))
            for i in range(1,21):
                pygame.draw.line(screen,"dark blue",(32*i,0),(32*i,512))
            for i in range(1,17):
                pygame.draw.line(screen, "dark blue", (0,32*i), (640, 32*i))
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
