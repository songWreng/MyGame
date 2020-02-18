class Settings():
    """存储《Alien Invasion》的所有设置的类"""
    def __init__(self):
        """初始化游戏的设置"""
        # 屏幕的设置
        self.screen_width = 1200
        self.screen_height = 640
        self.bg_color = (230, 230, 230)

        # 飞船的设置
        self.ship_photo_path = '.\Alien_Invasion\images\Ship.bmp'
        self.ship_limit = 3

        # 子弹的设置
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = (0, 0, 255)
        self.bullets_allowed = 3

        # 外星人的设置
        self.alien_photo_path = '.\Alien_Invasion\images\Alien.bmp'
        self.fleet_drop_speed = 30
        
        # 以什么样的速度加快游戏节奏
        self.speedup_scale = 1.1
        # 外星人点数的提高速度
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """初始化随游戏进行而变化的设置"""
        self.alien_speed_factor = 0.5
        self.bullet_speed_factor = 3
        self.ship_speed_factor = 1.5
        # 计分
        self.alien_points = 50
        
        self.fleet_direction = 1 # 1表示右移，-1表示左移

    def increase_speed(self):
        """提高速度设置"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
    
        self.alien_point = int(self.alien_points * self.score_scale)
        print(self.alien_points)