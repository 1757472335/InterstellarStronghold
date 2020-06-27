# 角色控制
from source import constants as CO
from source.tools import get_image
import pygame
Sprite = pygame.sprite.Sprite


class PlayerCO(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.palayer1_img = pygame.image.load(CO.PLAYER_0_1) # 角色图片
        self.bullet_img = pygame.image.load(CO.BULLET_01) # 子弹图片

        self.p1_rect = self.palayer1_img.get_rect()
        self.p1_rect_x = self.p1_rect[2]
        self.p1_rect_y = self.p1_rect[3]

        self.speed_x = CO.SCR_X // 2 - 200  # 初始x移动速度
        self.speed_y = CO.SCR_Y//2  # 初始y移动速度

        self.change = 0  # 角色动画控制
        self.bullets = pygame.sprite.Group()  # bullets属性：子弹组，使用精灵组

    def player_load(self, Surface):
        # 加载地图图片
        palayer1_img = get_image(self.palayer1_img,0,0,self.p1_rect_x,self.p1_rect_y,CO.COLOR_LU,1)
        # self.lv_x = self.lv_x+30
        Surface.blit(palayer1_img,(self.speed_x,self.speed_y),self.p1_rect) # 图像，绘制的位置，绘制的截面框

    def pl_uodate_u(self):  # 角色上移
        self.speed_y = self.speed_y - 40

    def pl_uodate_d(self):  # 角色下移
        self.speed_y = self.speed_y + 40


    def pl_check(self):  # 检测是否超出屏幕

        if self.speed_y <= 0:
            self.speed_y = 0
        elif self.speed_y >= CO.SCR_Y - 100:
            self.speed_y = CO.SCR_Y - 100


    def change_p1(self):  # 控制角色动画
        if self.change == 0 :
            self.palayer1_img = pygame.image.load(CO.PLAYER_0_1)
            self.change = 1

        elif self.change == 1:
            self.palayer1_img = pygame.image.load(CO.PLAYER_0_2)
            self.change = 2

        elif self.change == 2:
            self.palayer1_img = pygame.image.load(CO.PLAYER_0_3)
            self.change = 0
    def get_p1_y(self):
        return self.speed_y

    # 发射子弹方法
    def shoot(self):
        print(self.p1_rect)
        bullet = Bullet(self.bullet_img, (self.speed_x,self.speed_y))
        # 将子弹添加到子弹组中
        self.bullets.add(bullet)

# 子弹
class Bullet(pygame.sprite.Sprite):
    # 构造方法，参数分别是子弹图片和起始位置
    def __init__(self, bullet_surface, bullet_init_pos):
        # 调用父类的构造方法
        pygame.sprite.Sprite.__init__(self)
        # 设置属性
        self.image = bullet_surface  # image属性：子弹图片
        self.rect = self.image.get_rect()  # rect属性：矩形
        self.rect.topleft = bullet_init_pos  # 矩形左上角坐标
        self.speed = 8  # speed属性：子弹移动速度

    # 移动方法
    def update(self):
        # 修改子弹坐标
        self.rect.right += self.speed
        # 如果子弹移出屏幕，则销毁子弹对象
        if self.rect.right > CO.SCR_X:
            self.kill()


