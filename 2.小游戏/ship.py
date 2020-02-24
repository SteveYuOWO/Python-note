import pygame

class Ship():
    def __init__(self, screen):
        """初始化飞船并设置初始位置"""
        self.screen = screen

        # 加载飞船图像并获取外接矩形
        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 放在底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # 移动标志
        self.moving_right = False

    def biltme(self):
        """绘制飞船"""
        self.update()
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_right:
            self.rect.centerx += 10