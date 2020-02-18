import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep
from button import Button
from scoreboard import Scoreboard

def fire_bullet(ai_settings, screen, ship, bullets):
    """处理飞船开火"""
    # 创建一颗子弹，并将其加入编组bullets中
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def check_keydown_events(event, ai_settings, screen, ship, bullets, stats):
    """响应按键"""
    if event.key == pygame.K_RIGHT:
        # 向右移动飞船
        # print("You press the k_right")
        ship.moving_right = True
    
    elif event.key == pygame.K_LEFT:
        # 向左移动飞船
        # print("You press the k_left")
        ship.moving_left = True

    elif event.key == pygame.K_SPACE:
        # 发射子弹
        # print("Fire")
        fire_bullet(ai_settings, screen, ship, bullets)

    elif event.key == pygame.K_q:
        # 退出游戏
        print("Quit the game")
        sys.exit()
    
    elif event.key == pygame.K_p:
        # 暂停游戏
        stats.game_stop = not stats.game_stop
        
    elif event.key == pygame.K_w:
        # 增大子弹宽度
        ai_settings.enlarge_bullet()

    elif event.key == pygame.K_s:
        ai_settings.ensmall_bullet()

def check_keyup_events(event, ship):
    """响应松开"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False 

def check_play_button(ai_settings,  screen, ship, aliens, bullets, 
            stats, play_button, mouse_x, mouse_y, sb):
    """在玩家单击Play按钮时开始新游戏"""
    if play_button.rect.collidepoint(mouse_x, mouse_y) and not stats.game_active:
        # 重置游戏设置
        ai_settings.initialize_dynamic_settings()

        # 隐藏光标
        pygame.mouse.set_visible(False)

        # 重置游戏统计信息
        stats.reset_stats()
        stats.game_active = True

        # 重置记分牌图像
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships_love()
        # 清空外星人列表和子弹列表
        aliens.empty()
        bullets.empty()

        # 创建一群新的外星人，并让飞船居中
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()


def check_events(ai_settings, screen, ship, aliens, bullets, stats, play_button, sb):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("You close the game")
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets, stats)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, ship, aliens, bullets,
                    stats, play_button, mouse_x, mouse_y, sb)

def update_screen(ai_settings, screen, ship, aliens, bullets, stats, play_button, sb):
    """更新屏幕上的图像，并切换到新的屏幕"""
    # 每次循环时都要重绘屏幕
    screen.fill(ai_settings.bg_color)

    # 在飞船后面重绘所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    
    ship.blitme()
    aliens.draw(screen)

    # 显示得分
    sb.show_score()

    # 如果游戏处于非活动状态，就绘制Play按钮
    if not stats.game_active:
        play_button.draw_button()

    # 让最近绘制的屏幕可见
    pygame.display.flip()

def update_bullets(ai_settings, screen, ship, aliens, bullets, stats, sb):
    """
    更新子弹的位置，并删除已消失的子弹;
    删除相撞的子弹和外星人;
    重新生成外星人。
    """
    # 更新子弹的位置
    bullets.update()

    # 删除已消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets, stats, sb)
   
def check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets, stats, sb):
    """相应子弹和外星人的碰撞"""
    # 检查是否有子弹击中了外星人，如果是这样，就删除相应的子弹和外星人
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    # 后面两个布尔值True告诉Pygame删除发生碰撞的子弹和外星人，
    # 如果想保留第一个图形(bullets)，可将第一个布尔值设为False，
    # 保留第二个图形(aliens)，可将第二个布尔值设为False

    if collisions:
        for tmpAlien in range(len(list(collisions.values())[0])):
            stats.score += ai_settings.alien_points
            sb.prep_score()
        check_high_score(stats, sb)

    if len(aliens) == 0:
        # 删除现有的子弹并新建一群外星人
        bullets.empty()
        ai_settings.increase_speed()

        # 如果整群外星人都被消灭，就提高一个等级
        stats.level += 1
        sb.prep_level()

        create_fleet(ai_settings, screen, ship, aliens)

def get_number_alien_x(ai_settings, alien_width):
    """计算每行可容纳多少个外星人"""
    available_space_x = ai_settings.screen_width - alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    # print("The number of aliens each line:", number_aliens_x)
    # print("Width:", alien_width)
    return number_aliens_x

def get_number_rows(ai_settings, ship_height, alien_height):
    """计算屏幕可容纳多少行外星人"""
    available_space_y = (ai_settings.screen_height - 5 * alien_height - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    # print("The number of row:", number_rows)
    return number_rows

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """创建一个外星然并将其放在当前行"""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.f_x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.f_x
    alien.rect.y = alien.rect.height*3 + 2 * alien.rect.height * row_number
    aliens.add(alien)
    # print("NO.", alien_number, "alien position:", (alien.rect.x, alien.rect.y))

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

def check_fleet_edges(ai_settings, aliens):
    """有外星人到达边缘时采取相应的措施"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break

def change_fleet_direction(ai_settings, aliens):
    """将整体外星人下移，并将它们改变方向"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def update_aliens(ai_settings, screen, ship, aliens, bullets, stats, sb):
    """检查是否有外星人位于屏幕边缘， 更新外星人群中所有外星人的位置"""
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    # 检测外星人和飞船之间的碰撞
    if pygame.sprite.spritecollideany(ship, aliens):
        # spritecollideany(精灵， 编组)检测编组成员是否与精灵发生碰撞，返回第一个与飞船碰撞的外星人
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets, sb)
        print("Ship hit!")
    
    # 检查是否有外星人到达屏幕底端
    check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets, sb)
          
def ship_hit(ai_settings, stats, screen, ship, aliens, bullets, sb):
    """响应被外星人碰撞的飞船"""
    if stats.ships_left >= 1:
        print(stats.ships_left)
        # 可用的船数减1
        stats.ships_left -= 1
        sb.prep_ships_love()

        # 清空外星人和子弹列表
        aliens.empty()
        bullets.empty()

        # 创建新的外星人并将飞船放到屏幕底端的中央
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

        # 暂停
        sleep(0.5)
    if stats.ships_left <= 0:
        stats.game_active = False
        pygame.mouse.set_visible(True)

def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets, sb):
    """检查是否有外星人到达了屏幕底端"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # 同飞船撞到一样进行处理
            ship_hit(ai_settings, stats, screen, ship, aliens, bullets, sb)
            break
    
def check_high_score(stats, sb):
    """检查是否诞生了新的最高得分"""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()

