import numpy as np

FPS = 5000
FPS_PLAY = 48

W_WIDTH, W_HEIGHT = 150, 150

BLACK = np.array([0, 0, 0])
GRAY = np.array([128, 128, 128])
CRIMSON = np.array([220, 20, 60])
WHITE = np.array([255, 255, 255])
GREEN = np.array([34, 139, 34])

SNAKE_SIZE = 10
SNAKE_SEPARATION = 1
WALL_SIZE = SNAKE_SIZE
APPLE_SIZE = SNAKE_SIZE
APPLE_QTD = 1
SNAKE_ALIVE_PRIZE = -8e-3
SNAKE_EAT_ITSELF_PRIZE = -1.0
WALL_PRIZE = -1.0
APPLE_PRIZE = 1
APPLE_RELOAD_STEPS = FPS_PLAY * 10

KEY = {"UP": 1, "DOWN": 2, "LEFT": 3, "RIGHT": 4}

# Deep Learning Params
IMG_SIZE = 84
BATCH_SIZE = 64
GAMMA = 0.999
EPS_START = 0.9
EPS_END = 0.01
EPS_DECAY = 1500
EPOCHS = 10_000
TARGET_UPDATE = 1_000
MODEL_SAVE = 20_000
MEM_LENGTH = 7_000
MEM_CLEAN_SIZE = 7_000
LEARNING_RATE = 1e-7
MOMENTUM = 0.95
