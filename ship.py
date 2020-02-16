import pygame
class Ship():

    def __init__(self, screen):
        """初始化飞船并设置它的位置"""
        self.screen = screen

        # 加载飞船的图像并获取其外界矩形
        self.image = pygame.image.load('E:\python文档\Alien_Invasion\images\Ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每艘飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)
