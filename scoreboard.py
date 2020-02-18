import pygame.font
from pygame.sprite import Group
from ship import ShipLove

class Scoreboard():
    """显示得分信息的类"""

    def __init__(self, ai_settings, screen, stats):
        """初始化显示得分涉及的属性"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        # 显示得分信息时使用的字体设置
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # 准备初始化得分图像
        self.prep_score()
        # 准备包含最高分的图像
        self.prep_high_score()
        # 准备包含等级的初始图像
        self.prep_level()
        # 显示爱心
        self.prep_ships_love()
        # 显示暂停
        self.prep_stop()

    def prep_score(self):
        """将得分转化为一幅渲染的图像"""
        rounded_score = int(round(self.stats.score, -1))
        score_str = "Current Score: " + "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.ai_settings.bg_color)

        # 将得分放在屏幕右上角
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        """将最高得分转化为渲染的图像"""
        high_score = int(round(self.stats.high_score, -1))
        high_score_str = "Highest Score: " + "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.ai_settings.bg_color)

        # # 将最高分放在得分下方
        self.high_score_rect = self.high_score_image.get_rect()  
        self.high_score_rect.right = self.score_rect.right
        self.high_score_rect.top = self.score_rect.bottom + 10
        

    def prep_level(self):
        """将等级转化为渲染的图像"""
        self.level_image = self.font.render("Level: " + str(self.stats.level), True, self.text_color, self.ai_settings.bg_color)

        # 将等级放在屏幕顶部的中央
        self.level_rect = self.level_image.get_rect()
        self.level_rect.centerx = self.screen_rect.centerx
        self.level_rect.top = self.screen_rect.top

    def prep_ships_love(self):
        """显示还余下多少艘飞船"""
        self.ships_love = Group()
        for ship_number in range(self.stats.ships_left):
            love_ship = ShipLove(self.ai_settings, self.screen)
            love_ship.rect.x = 10 + ship_number * love_ship.rect.width
            love_ship.rect.y = 10
            self.ships_love.add(love_ship)

    def prep_stop(self):
        """显示暂停"""
        self.stop_image = self.font.render("PAUSE", True, (255, 255, 255), (0, 255, 0))
        self.stop_image_rect = self.stop_image.get_rect()
        # 将暂停放在屏幕的中央
        self.stop_image_rect.centerx = self.screen_rect.centerx
        self.stop_image_rect.centery = self.screen_rect.centery
        

    def show_score(self):
        """在屏幕上显示得分和最高得分"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships_love.draw(self.screen)
        if self.stats.game_stop and self.stats.game_active:
            self.screen.blit(self.stop_image, self.stop_image_rect)


