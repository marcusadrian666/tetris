# 导入pygame库
import pygame
import sys
import random

# 定义一些常量
SCREEN_WIDTH = 800 # 屏幕宽度
SCREEN_HEIGHT = 600 # 屏幕高度
GRID_SIZE = 20 # 方格大小
GRID_WIDTH = SCREEN_WIDTH / GRID_SIZE # 网格宽度
GRID_HEIGHT = SCREEN_HEIGHT / GRID_SIZE # 网格高度
FPS = 10 # 帧率

# 定义一些颜色
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (100, 100, 100)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)

# 定义一些形状，每个形状由四个方格组成，用列表表示每个方格的相对位置
SHAPES = [
    [[0, 0], [1, 0], [0, 1], [1, 1]], # 方块
    [[0, 0], [1, 0], [2, 0], [3, 0]], # 长条
    [[2, 0], [0, 1], [1, 1], [2, 1]], # L形
    [[0, 0], [0, 1], [1, 1], [2, 1]], # 反L形
    [[1, 0], [0, 1], [1, 1], [2, 1]], # T形
    [[1, 0], [2, 0], [0, 1], [1, 1]], # Z形
    [[0, 0], [1, 0], [1, 1], [2, 1]] # 反Z形
]

# 定义每种形状对应的颜色
SHAPES_COLORS = [
    YELLOW,
    CYAN,
    BLUE,
    ORANGE,
    MAGENTA,
    GREEN,
    RED
]

# 初始化pygame和字体库
pygame.init()
pygame.font.init()

# 创建一个窗口对象，设置标题和大小
screen = pygame.display.set_mode((SCREEN_WIDTH +200 , SCREEN_HEIGHT))
pygame.display.set_caption('Tetris')

# 创建一个时钟对象，用于控制帧率
clock = pygame.time.Clock()

# 创建一个字体对象，用于绘制文字
font = pygame.font.SysFont('arial',32)

# 定义一个函数，用于初始化游戏状态
def init_game():
    global grid # 网格，用二维列表表示，存储每个方格的颜色，初始值为None
    global score # 分数，初始值为0
    global speed # 下落速度，初始值为500毫秒，即每隔500毫秒下
