import pygame
from media.settings.settings import user_screen_w
from media.captures.actions.bird_media import fly

BIRD_W = 200
BIRD_H = 200
SPEED = 10
JUMP = 20

flyAnimation = []
for image in fly:
    flyAnimation.append(pygame.transform.scale(image, (BIRD_W, BIRD_H)))


class Bird(pygame.sprite.Sprite):
    def __init__(self, groups, x, y, width, height):
        super().__init__(groups)
        self.animCount = 0
        self.image = flyAnimation[self.animCount]
        self.rect = self.image.get_rect(x=x, bottom=y + height + 500)
        self.speedX = 0
        self.Left = False

    def update(self):

        if not self.Left:
            self.speedX = SPEED
            if self.rect.right > user_screen_w:
                self.speedX = 0
                self.Left = True
        else:
            self.speedX = -SPEED
            if self.rect.right < 150:
                self.speedX = 0
                self.Left = False

        self.rect.x += self.speedX
        self.animation()

    def animation(self):

        if self.speedX:
            self.animCount += 1
            if self.animCount == len(flyAnimation):
                self.animCount = 0

            self.image = flyAnimation[self.animCount]
            if self.speedX < 0:  # Если двигаюсь вправо,
                self.image = pygame.transform.flip(self.image, True, False)