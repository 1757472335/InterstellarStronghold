# 角色控制
from source import constants as CO
from source.tools import get_image
import pygame
Sprite = pygame.sprite.Sprite


class PlayerCO(Sprite):

    def __init__(self,pltype):
        Sprite.__init__(self)
        self.bu_st = 0  # 当前子弹状态
        self.pltype = pltype
        if pltype == '1':
            self.image = pygame.image.load(CO.PLAYER_0_1)  # 角色图片
            self.health = 100
            self.health_img = pygame.image.load(CO.HEALTH_p1_10) #血量
            self.health_img_rect = self.health_img.get_rect()
            self.score1 = 0
            self.bullet_img = pygame.image.load(CO.BULLET_01)  # 子弹图片
            self.sound = pygame.mixer.Sound(CO.BU_SOU_01)  # 音效

        self.rect = self.image.get_rect()
        self.speed = 20

        self.speed_x = CO.SCR_X // 2 - 300  # 初始x移动速度
        self.speed_y = CO.SCR_Y//2  # 初始y移动速度

        self.rect.top = self.speed_x
        self.rect.left = self.speed_y

        self.change = 0  # 角色动画控制
        self.bullets = pygame.sprite.Group()  # bullets属性：子弹组，使用精灵组
        self.bu_st_tim = 0
        self.clock = pygame.time.Clock()

    def player_load(self, Surface):
        # 加载玩家图图片
        Surface.blit(self.image,self.rect) # 图像，绘制的位置，绘制的截面框

    #绘制玩家血量
    def draw_p1_health(self,Surface):
        # 加载玩家血量图图片
        if self.health >= 100:
            self.health_img = pygame.image.load(CO.HEALTH_p1_10)
        elif 90 <= self.health < 100:
            self.health_img = pygame.image.load(CO.HEALTH_p1_09)
        elif 80 <= self.health < 90:
            self.health_img = pygame.image.load(CO.HEALTH_p1_08)
        elif 70 <= self.health < 80:
            self.health_img = pygame.image.load(CO.HEALTH_p1_07)
        elif 60 <= self.health < 70:
            self.health_img = pygame.image.load(CO.HEALTH_p1_06)
        elif 50 <= self.health < 60:
            self.health_img = pygame.image.load(CO.HEALTH_p1_05)
        elif 40 <= self.health < 50:
            self.health_img = pygame.image.load(CO.HEALTH_p1_04)
        elif 30 <= self.health < 40:
            self.health_img = pygame.image.load(CO.HEALTH_p1_03)
        elif 20 <= self.health < 30:
            self.health_img = pygame.image.load(CO.HEALTH_p1_02)
        elif 10 <= self.health < 20:
            self.health_img = pygame.image.load(CO.HEALTH_p1_01)
        Surface.blit(self.health_img, (0, 0), self.health_img_rect)  # 图像，绘制的位置，绘制的截面框
        pass

    def draw_score(self, Surface, font_color=CO.FONT_COL):
        '''
        :param Surface: 屏幕
        :param font_color: 颜色
        :return:
        '''
        text = pygame.font.Font(CO.FONT_S,20)
        text_fm = text.render("SCORE :"+str(self.score1),True,font_color,None)
        Surface.blit(text_fm,(CO.SCR_X-300,20))

    def pl_uodate_u(self):  # 角色上移
        self.rect.top -= self.speed

    def pl_uodate_d(self):  # 角色下移
        self.rect.top += self.speed

    def pl_uodate_r(self):  # 角色右移动
        self.rect.right += 10

    def pl_uodate_l(self):  # 角色左移
        self.rect.right -= 0

    def pl_check(self):  # 检测是否超出屏幕
        if self.rect.top <= 0:
            self.rect.top = 0
        elif self.rect.top >= CO.SCR_Y - 100:
            self.rect.top = CO.SCR_Y - 100

    def change_p1(self):  # 控制角色动画
        if self.change == 0 :
            self.image = pygame.image.load(CO.PLAYER_0_1)
            self.change = 1

        elif self.change == 1:
            self.image = pygame.image.load(CO.PLAYER_0_2)
            self.change = 2

        elif self.change == 2:
            self.image = pygame.image.load(CO.PLAYER_0_3)
            self.change = 3

        elif self.change == 3:
            self.image = pygame.image.load(CO.PLAYER_0_4)
            self.change = 4

        elif self.change == 4:
            self.image = pygame.image.load(CO.PLAYER_0_5)
            self.change = 0

    def get_p1_pos(self):
        pos = self.rect.topleft
        return pos

    # 发射子弹方法
    def shoot(self):
        self.bu_st_tim +=1
        if self.bu_st == 0:
            if self.bu_st_tim % 5 ==0:

                bullet = Bullet(self.bullet_img, (self.rect.topleft[0],self.rect.topleft[1]+30))
                self.bullets.add(bullet)
                self.sound.play()
        if self.bu_st == 1:

            bullet = Bullet(self.bullet_img, (self.rect.topleft[0], self.rect.topleft[1] + 30))
            self.bullets.add(bullet)
            self.sound.play()




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
        self.speed = 80  # speed属性：子弹移动速度

    # 移动方法
    def update(self):
        # 修改子弹坐标
        self.rect.right += self.speed
        # 如果子弹移出屏幕，则销毁子弹对象
        if self.rect.right > CO.SCR_X:
            self.kill()



