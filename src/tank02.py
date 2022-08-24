#
# Tank 2022
# Time : 2022/08/24
# Author : YU,J.P
#

"""
    V1.0.3
        新增功能：
            创建游戏窗口 -- 用到游戏引擎的功能模块，阅读官方开发文档

"""

import pygame  # 游戏引擎安装成功

# 全局变量
COLOR_BACKGROND = pygame.Color(100, 100, 100)  # 背景颜色 RGB合成颜色

# 主逻辑类
class MainGame():
    window = None  # 游戏主窗口
    SCREEN_HEIGHT = 500  # 窗口高度
    SCREEN_WIDTH = 800 # 窗口宽度

    def __init__(self):
        pass

    # 开始游戏
    def startGame(self):
        pygame.display.init()  # 窗口初始化
        # 创建窗口加载窗口(借鉴官方文档)
        MainGame.window = pygame.display.set_mode([MainGame.SCREEN_WIDTH, MainGame.SCREEN_HEIGHT])
        # 设置游戏标题
        pygame.display.set_caption("坦克大战 V1.0.3")
        # 让窗口持续刷新操作
        while True:
            # 给窗口一个填充色
            MainGame.window.fill(COLOR_BACKGROND)

            pygame.display.update()


    # 结束游戏
    def endGame(self):
        print('谢谢使用！')
        exit()  # 结束python解释器


# 坦克类
class Tank():
    def __init__(self):
        pass

    # 坦克移动
    def move(self):
        pass

    # 坦克射击
    def shot(self):
        pass

    # 坦克展示
    def displayTank(self):
        pass


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


if __name__ == '__main__':
    MainGame().startGame()  # 开始游戏
