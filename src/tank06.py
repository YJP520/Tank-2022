#
# Tank 2022
# Time : 2022/08/24
# Author : YU,J.P
#

"""
    V1.0.7
        新增功能：
            1.坦克类新增速度属性，用来控制坦克移动快慢
            2.事件处理:
                2.1 改变坦克方向
                2.2 修改坦克的位置（left,top）
                    取决于坦克的速度

"""

import pygame  # 游戏引擎安装成功

# 全局变量
VERSION = '坦克大战 V1.0.7'
COLOR_BACKGROND = pygame.Color(202, 231, 255)  # 背景颜色 RGB合成颜色 (156, 191, 238) (221, 227, 247) (202, 231, 255)
FONT = '方正粗黑宋简体'
COLOR_FONT = pygame.Color(24, 72, 172)  # 字体颜色 RGB合成颜色 24, 72, 172
SIZE_FONT = 24  # 字体大小
GETTEXT_X = 5  # 提示文字 x 坐标
GETTEXT_Y = 5  # 提示文字 y 坐标
TANK_X = 300  # 主战坦克坐标
TANK_Y = 300  # 主战坦克坐标
TANK_SPEED = 128  # 坦克移动速度

# 坦克类
class Tank():
    def __init__(self, left, top):
        # 从磁盘加载到的图片
        self.images = {
            'U': pygame.image.load('images/planeU.gif'),
            'D': pygame.image.load('images/planeD.gif'),
            'L': pygame.image.load('images/planeL.gif'),
            'R': pygame.image.load('images/planeR.gif')
        }
        self.direction = 'U'
        self.image = self.images[self.direction]
        # 坦克所在的区域 rect
        self.rect = self.image.get_rect()
        # 指定坦克初始化位置,分别是x,y轴的位置
        self.rect.left = left
        self.rect.top = top
        # 新增速度属性
        self.speed = TANK_SPEED


    # 坦克移动
    def move(self):
        if self.direction == 'L':
            self.rect.left -= self.speed
        elif self.direction == 'R':
            self.rect.left += self.speed
        elif self.direction == 'U':
            self.rect.top -= self.speed
        elif self.direction == 'D':
            self.rect.top += self.speed

    # 坦克射击
    def shot(self):
        pass

    # 坦克展示（将坦克这个surface绘制到窗口中 blit()）
    def displayTank(self):
        # 1.重新设置坦克的图片
        self.image = self.images[self.direction]
        # 2.将坦克加入到窗口中
        MainGame.window.blit(self.image, self.rect)


# 我方坦克
class MyTank(Tank):
    def __init__(self):
        pass


# 敌方坦克
class EnemyTank(Tank):
    def __init__(self):
        pass


# 子弹类
class Bullet():
    def __init__(self):
        pass

    # 子弹移动
    def move(self):
        pass

    # 展示子弹
    def displayBullet(self):
        pass


# 爆炸效果类
class Explode():
    def __init__(self):
        pass

    # 展示爆炸效果
    def displayExplode(self):
        pass


# 墙壁类
class Wall():
    def __init__(self):
        pass

    # 展示墙壁
    def displayWall(self):
        pass


# 音效类
class Music():
    def __init__(self):
        pass

    # 开始游戏音效
    def startPlay(self):
        pass


# 主逻辑类
class MainGame():
    window = None  # 游戏主窗口
    SCREEN_HEIGHT = 500  # 窗口高度
    SCREEN_WIDTH = 800  # 窗口宽度

    TANK_P1 = None   # 我方坦克

    def __init__(self):
        pass

    # 开始游戏
    def startGame(self):
        pygame.display.init()  # 窗口初始化
        # 创建窗口加载窗口(借鉴官方文档)
        MainGame.window = pygame.display.set_mode([MainGame.SCREEN_WIDTH, MainGame.SCREEN_HEIGHT])
        # 设置游戏标题
        pygame.display.set_caption(VERSION)
        # 加载主战坦克
        MainGame.TANK_P1 = Tank(TANK_X, TANK_Y)
        # 让窗口持续刷新操作
        while True:
            # 给窗口一个填充色
            MainGame.window.fill(COLOR_BACKGROND)
            # 在循坏中持续完成事件的获取
            self.getEvent()
            # 将绘制文字得到的小画布，放到窗口上
            MainGame.window.blit(self.getTextSurface("Remaining Tanks: %d" % 5), (GETTEXT_X, GETTEXT_Y))
            # 将我方坦克加载到窗口中
            MainGame.TANK_P1.displayTank()
            # 窗口的刷新
            pygame.display.update()

    # 左上角文字绘制的功能
    def getTextSurface(self, text):
        # 字体初始化模块
        pygame.font.init()
        # 选中一个合适的字体
        # fontList = pygame.font.get_fonts()  # 获取目前所有字体
        # for font in fontList:
        #     print(font)
        font = pygame.font.SysFont(FONT, SIZE_FONT)
        # 使用对应的字体完成相关内容的绘制
        textSurface = font.render(text, True, COLOR_FONT)
        return textSurface

    # 获取程序运行期间所有事件（鼠标事件，键盘事件）
    def getEvent(self):
        # 1.获取所有事件
        eventList = pygame.event.get()
        # 2.对事件进行判断处理（1.点击关闭按钮，2.按下键盘的某个按键）
        for event in eventList:
            # 判断event.type 是否QUIT，如果是退出的话，直接调用程序结束方法
            if event.type == pygame.QUIT:
                self.endGame()
            # 判断事件类型是否为按键按下，如果是，继续判断按键是哪一个按键，进行对应处理
            if event.type == pygame.KEYDOWN:
                # 判断具体是哪一个按键的处理
                if event.key == pygame.K_LEFT:  # 左方向键
                    print('坦克向左调头，移动')
                    # 修改坦克方向
                    MainGame.TANK_P1.direction = 'L'
                    # 完成移动操作（调用坦克的移动方法）
                    MainGame.TANK_P1.move()
                elif event.key == pygame.K_RIGHT:  # 右方向键
                    print('坦克向右调头，移动')
                    # 修改坦克方向
                    MainGame.TANK_P1.direction = 'R'
                    # 完成移动操作（调用坦克的移动方法）
                    MainGame.TANK_P1.move()
                elif event.key == pygame.K_UP:  # 上方向键
                    print('坦克向上调头，移动')
                    # 修改坦克方向
                    MainGame.TANK_P1.direction = 'U'
                    # 完成移动操作（调用坦克的移动方法）
                    MainGame.TANK_P1.move()
                elif event.key == pygame.K_DOWN:  # 下方向键
                    print('坦克向下调头，移动')
                    # 修改坦克方向
                    MainGame.TANK_P1.direction = 'D'
                    # 完成移动操作（调用坦克的移动方法）
                    MainGame.TANK_P1.move()
                elif event.key == pygame.K_SPACE:  # 空格键
                    print('坦克发射炮弹')

    # 结束游戏
    def endGame(self):
        print('谢谢使用！')
        exit()  # 结束python解释器


if __name__ == '__main__':
    MainGame().startGame()  # 开始游戏
