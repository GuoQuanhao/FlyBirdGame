import pygame


class Pipeline(object):
    def __init__(self):
        self.wallX = 400
        self.score = 0
        self.pineUp = pygame.image.load('picture/top.png')
        self.pineDown = pygame.image.load('picture/bottom.png')

    def update_pipeline(self):
        self.wallX -= 5
        if self.wallX < -80:
            self.score += 1
            self.wallX = 400

    def empty(self):
        self.wallX = 400
        self.score = 0


