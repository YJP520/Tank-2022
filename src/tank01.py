#
# Tank 2022
# Time : 2022/08/24
# Author : YU,J.P
#

"""
    V1.0
"""


import pygame  # 游戏引擎安装成功


# 主逻辑类
class mainGame():
    def __init__(self):
        pass

    # 开始游戏
    def startGame(self):
        pass

    # 结束游戏
    def endGame(self):
        pass


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
    print('开始')
