import pyxel
import sys_fps
import sys_save
import stg_player as player
import stg_enemy as enemy
import stg_game_data as game_data

from enum import Enum

# =====================================
# 定数定義
# =====================================
APP_TITLE       = "SimpleSTG"  # タイトル
VENDOR_NAME     = "Kitayochi"  # 開発者名
SCREEN_WIDTH    = 256          # スクリーンサイズ幅
SCREEN_HEIGHT   = 180          # スクリーンサイズ高さ
DEBUG_PRINT     = 1            # デバッグ表示 (0:OFF/1:ON)
FPS_LIMIT       = 60           # FPS
FPS_PRINT       = False        # FPS表示 (True/False)
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
        pyxel.init(SCREEN_WIDTH, SCREEN_HEIGHT, title=APP_TITLE, fps=FPS_LIMIT)
        self.fps       = sys_fps.CFps()
        self.save_dir  = "./" #pyxel.user_data_dir(VENDOR_NAME, APP_TITLE)
        self.save_data = sys_save.CSaveData("game_data", self.save_dir)
        self.game_data = game_data.CGameData()
        self.scene     = SCENE_STATE.BOOT
        self.player    = player.CPlayer(100, 100)
        self.score     = 0
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
            pyxel.quit() # 終了

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
    # Scene: BOOT
    # --------------------
    def update_scene_boot(self):
        self.fps.visible(FPS_PRINT)
        loaded_data = self.save_data.load()
        if loaded_data:
            self.game_data.set_load_data(loaded_data)
        else:
            print("No save data found. Start new game.")
        self.scene = SCENE_STATE.TITLE

    def draw_scene_boot(self):
        self.debug_print(0, 0, "BOOT", 7)
        return

    # --------------------
    # Scene: TITLE
    # --------------------
    def update_scene_title(self):
        if pyxel.btnp(pyxel.KEY_RETURN) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_X):
            self.score = 0
            play_count = self.game_data.get_play_count()
            play_count = play_count + 1
            self.game_data.set_play_count(play_count)
            self.scene = SCENE_STATE.PLAYING

    def draw_scene_title(self):
        self.debug_print(0, 0, "TITLE", 7)
        pyxel.text(0, 10, f"HI-SCORE: {self.game_data.get_score()}", 7)
        pyxel.text(0, 20, f"PLAY COUNT: {self.game_data.get_play_count()}", 7)
        return

    # --------------------
    # Scene: PLAYING
    # --------------------
    def update_scene_playing(self):
        if pyxel.frame_count % ENEMY_INTARVAL == 0:
            enemy.CEnemy(pyxel.width, pyxel.rndi(0, pyxel.height - 4))

        self.score = self.score + 1
        self.player.update()
        enemy.update()
        enemy.cleanup()

        if pyxel.btnp(pyxel.KEY_END):
            self.scene = SCENE_STATE.GAMEOVER
        return

    def draw_scene_playing(self):
        self.debug_print(0, 0, "PLAYING", 7)
        pyxel.text(0, 10, f"SCORE: {self.score}", 7)
        self.player.draw()
        enemy.draw()
        return

    # --------------------
    # Scene: GAMEOVER
    # --------------------
    def update_scene_gameover(self):
        if pyxel.btnp(pyxel.KEY_RETURN) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_X):
            hi_score = self.game_data.get_score()
            if self.score > hi_score:
                self.game_data.set_score(self.score)
            save_data = self.game_data.get_save_data()
            self.save_data.save(save_data)
            self.scene = SCENE_STATE.TITLE
        return

    def draw_scene_gameover(self):
        self.debug_print(0, 0, "GAMEOVER", 7)
        pyxel.text(0, 10, f"SCORE: {self.score}", 7)
        return

    # --------------------
    # Util: Debug
    # --------------------
    def debug_print(self, x, y, text, color):
        if DEBUG_PRINT == 1:
            pyxel.text(x, y, text, color)
App()
