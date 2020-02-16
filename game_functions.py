import sys
import pygame
def check_events():
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def updata_screen(ai_setting, screen, ship):
    """更新屏幕上的图像，并切换到新的屏幕"""
    # m每次循环时都要重绘屏幕
    screen.fill(ai_setting.bg_color)
    ship.blitme()
    # 让最近绘制的屏幕可见
    pygame.display.flip()
    