# title: Pyxel-SimpleSTG
# author: Kitayoshi
# desc: Simple STG
# site: https://github.com/kitayoshi47/Pyxel-SimpleSTG
# license: MIT
# version: 0.1

import pyxel
import time

from enum import Enum

#======================================
# 定数定義
#======================================
APP_TITLE       = "SimpleSTG"           # タイトル
SCREEN_WIDTH    = 256                   # スクリーンサイズ幅
SCREEN_HEIGHT   = 256                   # スクリーンサイズ高さ

class SCENE_STATE(Enum):
    BOOT     = 0
    TITLE    = 1
    PLAYING  = 2
    GAMEOVER = 3

#======================================
# FPS計測クラス
#======================================
FPS_INTERVAL = 0.5 # FPS更新間隔
FPS_PRINT    = 1   # FPS表示(0:OFF/1:ON)
class Fps:
    def __init__(self):
        self.time_start  = 0
        self.time_prev   = 0
        self.frame_count = 0
        self.fps         = 0

    def start(self):
        self.frame_count += 1
        self.time_start = time.time() - self.time_prev

    def end(self):
        if self.time_start >= FPS_INTERVAL:
            self.fps = self.frame_count / self.time_start
            self.frame_count = 0
            self.time_prev = time.time()

    def print(self, x, y):
        if FPS_PRINT == 1:
            pyxel.text(x, y, str(self.fps)[:5], 7)

#======================================
# 変数定義
#======================================
scene_state = SCENE_STATE.BOOT

#======================================
# アプリケーションクラス
#======================================
class App:
    # 初期化
    def __init__(self):
        self.fps = Fps()
        pyxel.init(SCREEN_WIDTH, SCREEN_HEIGHT, title=APP_TITLE)
        pyxel.run(self.update, self.draw)

    # 更新
    def update(self):
        self.fps.start()
        self.update_scene()
        self.fps.end()

    # 更新(実処理)
    def update_scene(self):
        #ESCキーで終了
        if pyxel.btnp(pyxel.KEY_ESCAPE):
            pyxel.quit()

    # 描画
    def draw(self):
        pyxel.cls(0)
        self.fps.print(0, 0)

App()
