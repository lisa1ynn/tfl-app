import pygame

class Stops:
    def __init__(self, screen, image, x, y, text):
        self.screen = screen
        self.image = pygame.transform.scale(pygame.image.load(image), (40, 40))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.font = pygame.font.SysFont("Arial",10)
        self.text = text

    def blitme(self):
        self.screen.blit(self.image, (self.rect.x, self.rect.y))
        txtsurf = self.font.render(self.text, True, (0, 0, 0))
        text_rect = txtsurf.get_rect()
        text_rect.centerx = self.rect.x + self.rect.width // 2
        text_rect.y = self.rect.y - text_rect.height
        self.screen.blit(txtsurf, text_rect)

class TubeStops(Stops):
    def __init__(self, screen, x, y, text):
        super().__init__(screen, image="images/tube-station4.bmp", x=x, y=y, text=text)
        # Tube-Stop-specific attributes or behaviors can be added here

class BusStops(Stops):
    def __init__(self, screen, x, y, text):
        super().__init__(screen, image="images/bus-stop.bmp", x=x, y=y, text=text)
        # Bus-stop-specific attributes or behaviors can be added here