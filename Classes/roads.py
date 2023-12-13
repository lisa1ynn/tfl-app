import pygame

class Roads:
    def __init__(self, screen):
        self.screen = screen

    def draw_roads(self):
        # busx road
        pygame.draw.line(self.screen,(0,0,0), (1000, 0), (1000, 1200))

        # busy road
        pygame.draw.line(self.screen, (0,0,0),(1600, 400), (450, 400))

        # holborn line
        pygame.draw.line(self.screen, (255,0,0), (1000, 1200), (400, 600),2)
        pygame.draw.line(self.screen,(255,0,0), (400, 600), (0, 600),2)

        # piccadilly line
        pygame.draw.line(self.screen, (0,0,255), (400, 0), (400, 1200),2)