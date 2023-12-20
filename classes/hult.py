import pygame

class Hult:
    def __init__(self, screen):
        self.screen = screen
        # load the image and get its rect
        self.image = pygame.transform.scale(pygame.image.load("images/hultlogo.bmp"),(80,80))
        self.rect = self.image.get_rect()

        self.rect.x = 700
        self.rect.y = 200

    def blitme(self):
        self.screen.blit(self.image, (self.rect.x, self.rect.y))