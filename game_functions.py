import sys
import pygame
from bullet import Bullet
from alien import Alien

def fire_bullet(ai_settings, screen, ship, bullets):
    """处理飞船开火"""
    # 创建一颗子弹，并将其加入编组bullets中
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """响应按键"""
    if event.key == pygame.K_RIGHT:
        # 向右移动飞船
        print("You press the k_right")
        ship.moving_right = True
    
    elif event.key == pygame.K_LEFT:
        # 向左移动飞船
        print("You press the k_left")
        ship.moving_left = True

    elif event.key == pygame.K_SPACE:
        # 发射子弹
        print("Fire")
        fire_bullet(ai_settings, screen, ship, bullets)

    elif event.key == pygame.K_q:
        # 退出游戏
        print("Quit the game")
        sys.exit()

def check_keyup_events(event, ship):
    """响应松开"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False 

def check_events(ai_settings, screen, ship, bullets):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("You close the game")
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def update_screen(ai_setting, screen, ship, aliens, bullets):
    """更新屏幕上的图像，并切换到新的屏幕"""
    # 每次循环时都要重绘屏幕
    screen.fill(ai_setting.bg_color)

    # 在飞船后面重绘所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    
    ship.blitme()
    aliens.draw(screen)

    # 让最近绘制的屏幕可见
    pygame.display.flip()

def update_bullets(bullets):
    """更新子弹的位置，并删除已消失的子弹"""
    # 更新子弹的位置
    bullets.update()

    # 删除已消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def get_number_alien_x(ai_settings, alien_width):
    """计算每行可容纳多少个外星人"""
    available_space_x = ai_settings.screen_width - alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    print("The number of aliens each line:", number_aliens_x)
    print("Width:", alien_width)
    return number_aliens_x

def get_number_rows(ai_settings, ship_height, alien_height):
    """计算屏幕可容纳多少行外星人"""
    available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    print("The number of row:", number_rows)
    return number_rows

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """创建一个外星然并将其放在当前行"""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.f_x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.f_x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)
    print("NO.", alien_number, "alien position:", (alien.rect.x, alien.rect.y))

def create_fleet(ai_settings, screen, ship, aliens):
    """创建外星人群"""
    # 创建外星人群，并计算一行可容纳多少个外星人
    # 外星人间距为外星人的宽度
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_alien_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

    # 创建第一行外星人
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)
         


