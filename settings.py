class Settings():
    """存储《Alien Invasion》的所有设置的类"""
    def __init__(self):
        """初始化游戏的设置"""
        # 屏幕的设置
        self.screen_width = 960
        self.screen_height = 590
        self.bg_color = (230, 230, 230)

        # 飞船的设置
        self.ship_speed_factor = 1.5
        self.ship_photo_path = 'E:\python文档\Alien_Invasion\images\Ship.bmp'

        # 子弹的设置
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3