import pygame
from pygame.sprite import Group
import game_functions as gf
from bullet import Bullet
from ship import Ship
from settings import Settings
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

def run_game():
    """游戏循环"""

    # 初始化pygame、游戏设置和屏幕
    pygame.init()
    pygame.display.set_caption("Alien Invasion") # 修改窗口标题
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    # 创建一艘飞船、一个子弹编组和一个外星人编组
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    # 创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)
    # 创建一个用于存储游戏统计信息的实例
    stats = GameStats(ai_settings)
    # 创建Play按钮
    play_button = Button(ai_settings, screen, "Play")
    # 创建积分牌
    sb = Scoreboard(ai_settings, screen, stats)

    # 开始游戏主循环
    while True:
        gf.check_events(ai_settings, screen, ship, aliens, bullets, stats, play_button)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets, stats, sb)
            gf.update_aliens(ai_settings, screen, ship, aliens, bullets, stats)
            
        gf.update_screen(ai_settings, screen, ship, aliens, bullets, stats, play_button, sb)

run_game()