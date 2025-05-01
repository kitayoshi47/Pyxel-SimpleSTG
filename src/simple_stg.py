import pyxel
import sys_fps
import sys_save
import stg_player as player
import stg_enemy as enemy

from enum import Enum

# =====================================
# 定数定義
# =====================================
APP_TITLE       = "SimpleSTG"  # タイトル
SCREEN_WIDTH    = 256          # スクリーンサイズ幅
SCREEN_HEIGHT   = 180          # スクリーンサイズ高さ
DEBUG_PRINT     = 1            # デバッグ表示 (0:OFF/1:ON)
FPS_PRINT       = True         # FPS表示
ENEMY_INTARVAL  = 8            # 敵出現間隔

# =====================================
# シーン定義
# =====================================
class SCENE_STATE(Enum):
    BOOT     = 0
    TITLE    = 1
    PLAYING  = 2
    GAMEOVER = 3

# =====================================
# アプリケーションクラス
# =====================================
class App:
    # --------------------
    # 初期化
    # --------------------
    def __init__(self):
        pyxel.init(SCREEN_WIDTH, SCREEN_HEIGHT, title=APP_TITLE, fps=60)
        self.fps       = sys_fps.CFps()
        self.save_data = sys_save.CSaveData("Kitayochi", "simple_stg")
        self.scene     = SCENE_STATE.BOOT
        self.player    = player.CPlayer(100, 100)
        pyxel.run(self.update, self.draw)

    # --------------------
    # 更新
    # --------------------
    def update(self):
        self.fps.start()

        if self.scene == SCENE_STATE.BOOT:
            self.update_scene_boot()
        elif self.scene == SCENE_STATE.TITLE:
            self.update_scene_title()
        elif self.scene == SCENE_STATE.PLAYING:
            self.update_scene_playing()
        elif self.scene == SCENE_STATE.GAMEOVER:
            self.update_scene_gameover()
        self.fps.end()

        if pyxel.btnp(pyxel.KEY_ESCAPE):
            pyxel.quit() # ESCキーで終了

    # --------------------
    # 更新 [BOOT]
    # --------------------
    def update_scene_boot(self):
        self.fps.visible(FPS_PRINT)
        self.scene = SCENE_STATE.TITLE

    # --------------------
    # 更新 [TITLE]
    # --------------------
    def update_scene_title(self):
        if pyxel.btnp(pyxel.KEY_S):
            self.save_data.save("")
        if pyxel.btnp(pyxel.KEY_RETURN) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_X):
            self.scene = SCENE_STATE.PLAYING

    # --------------------
    # 更新 [PLAYING]
    # --------------------
    def update_scene_playing(self):
        if pyxel.frame_count % ENEMY_INTARVAL == 0:
            enemy.CEnemy(pyxel.width, pyxel.rndi(0, pyxel.height - 4))

        self.player.update()
        enemy.update()
        enemy.cleanup()

        if pyxel.btnp(pyxel.KEY_END):
            self.scene = SCENE_STATE.GAMEOVER
        return

    # --------------------
    # 更新 [GAMEOVER]
    # --------------------
    def update_scene_gameover(self):
        if pyxel.btnp(pyxel.KEY_RETURN) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_X):
            self.scene = SCENE_STATE.TITLE
        return

    # --------------------
    # 描画
    # --------------------
    def draw(self):
        pyxel.cls(0)
        self.fps.print()
        if self.scene == SCENE_STATE.BOOT:
            self.draw_scene_boot()
        elif self.scene == SCENE_STATE.TITLE:
            self.draw_scene_title()
        elif self.scene == SCENE_STATE.PLAYING:
            self.draw_scene_playing()
        elif self.scene == SCENE_STATE.GAMEOVER:
            self.draw_scene_gameover()

    # --------------------
    # 描画 [BOOT]
    # --------------------
    def draw_scene_boot(self):
        self.debug_print(0, 0, "BOOT", 7)
        return

    # --------------------
    # 描画 [TITLE]
    # --------------------
    def draw_scene_title(self):
        self.debug_print(0, 0, "TITLE", 7)
        return

    # --------------------
    # 描画 [PLAYING]
    # --------------------
    def draw_scene_playing(self):
        self.debug_print(0, 0, "PLAYING", 7)
        self.player.draw()
        enemy.draw()
        return

    # --------------------
    # 描画 [GAMEOVER]
    # --------------------
    def draw_scene_gameover(self):
        self.debug_print(0, 0, "GAMEOVER", 7)
        return

    # --------------------
    # Debug
    # --------------------
    def debug_print(self, x, y, text, color):
        if DEBUG_PRINT == 1:
            pyxel.text(x, y, text, color)
App()
