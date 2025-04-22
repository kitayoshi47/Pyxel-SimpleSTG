import pyxel
import time

# =====================================
# 定数定義
# =====================================
FPS_PRINT_X  = 236  # FPS表示位置X
FPS_PRINT_Y  = 0    # FPS表示位置Y
FPS_INTERVAL = 0.3  # FPS更新間隔

# =====================================
# FPS計測クラス
# =====================================
class CFps:
    def __init__(self):
        self.time_start  = 0
        self.time_prev   = 0
        self.frame_count = 0
        self.fps         = 0
        self.is_visible  = True
        self.x           = FPS_PRINT_X
        self.y           = FPS_PRINT_Y
        self.interval    = FPS_INTERVAL

    def visible(self, flag):
        self.is_visible = flag

    def start(self):
        self.frame_count += 1
        self.time_start = time.time() - self.time_prev

    def end(self):
        if self.time_start >= self.interval:
            self.fps = self.frame_count / self.time_start
            self.frame_count = 0
            self.time_prev = time.time()

    def print(self):
        if self.is_visible == True:
            pyxel.text(self.x, self.y, str(self.fps)[:5], 7)
