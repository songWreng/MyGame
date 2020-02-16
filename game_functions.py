import sys
import pygame

def check_keydown_events(event, ship):
    """响应按键"""
    if event.key == pygame.K_RIGHT:
        # 向右移动飞船
        print("You press the k_right")
        ship.moving_right = True
    if event.key == pygame.K_LEFT:
        # 向左移动飞船
        print("You press the k_left")
        ship.moving_left = True

def check_keyup_events(event, ship):
    """响应松开"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False 

def check_events(ship):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("You close the game")
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def updata_screen(ai_setting, screen, ship):
    """更新屏幕上的图像，并切换到新的屏幕"""
    # m每次循环时都要重绘屏幕
    screen.fill(ai_setting.bg_color)
    ship.blitme()
    # 让最近绘制的屏幕可见
    pygame.display.flip()
    