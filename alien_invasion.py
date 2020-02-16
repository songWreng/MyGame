import pygame
import game_functions as gf

from ship import Ship
from settings import Settings

def run_game():
    # 初始化pygame、设置和屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    # 创建一艘飞船
    ship = Ship(ai_settings, screen)
    pygame.display.set_caption("Alien Invasion")

    # 开始游戏主循环
    while True:
        gf.check_events(ship)
        ship.update()
        gf.updata_screen(ai_settings, screen, ship)

run_game()