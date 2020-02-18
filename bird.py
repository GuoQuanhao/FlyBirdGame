import pygame


class Bird(object):
    """Bird definition"""
    def __init__(self):
        self.birdRect = pygame.Rect(65, 50, 50, 50)
        self.birdStatus = [pygame.image.load('picture/1.png'),
                           pygame.image.load('picture/2.png'),
                           pygame.image.load('picture/dead.png')]
        self.status = 0
        self.birdX = 120
        self.birdY = 350
        self.jump = False
        self.jump_speed = 10
        self.gravity = 5
        self.dead = False

    def bird_update(self):
        if self.jump:
            self.jump_speed -= 1
            self.birdY -= self.jump_speed

        else:
            self.gravity += 0.2
            #self.birdY += self.gravity

        self.birdRect[1] = self.birdY

    def empty(self):
        self.status = 0
        self.birdX = 120
        self.birdY = 350
        self.jump = False
        self.jump_speed = 10
        self.gravity = 5
        self.dead = False
