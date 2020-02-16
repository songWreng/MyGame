import pygame
class Ship():

    def __init__(self, AI_settings, screen):
        """初始化飞船并设置它的位置"""
        self.screen = screen
        self.ai_setting = AI_settings

        # 加载飞船的图像并获取其外界矩形
        self.image = pygame.image.load(self.ai_setting.ship_photo_path)
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每艘飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        # 在飞船的属性f_centerx 存储小数值(游戏需要)
        self.f_centerx = float(self.rect.centerx)

        # 移动的标志
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """根据移动标志来调整飞机的位置"""
        # 更新飞船的f_centerx的值
        if self.moving_right and self.rect.right < self.screen_rect.right: # 限制范围避免移出屏幕
            self.f_centerx += self.ai_setting.ship_speed_factor
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.f_centerx -= self.ai_setting.ship_speed_factor
        
        # 根据self.f_centerx更新rect对象
        self.rect.centerx = self.f_centerx # 只保留整数部分
        

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)
