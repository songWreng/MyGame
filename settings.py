class Settings():
    """存储《Alien Invasion》的所有设置的类"""
    def __init__(self):
        """初始化游戏的设置"""
        # 屏幕的设置
        self.screen_width = 990
        self.screen_height = 612
        self.bg_color = (230, 230, 230)

        # 飞船的设置
        self.ship_speed_factor = 1.5
        self.ship_photo_path = '.\Alien_Invasion\images\Ship.bmp'

        # 子弹的设置
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # 外星人的设置
        self.alien_photo_path = '.\Alien_Invasion\images\Alien.bmp'
        self.alien_speed_factor = 0.5
        self.fleet_drop_speed = 1
        self.fleet_direction = 1 # 1表示右移，-1表示左移
