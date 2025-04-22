import pyxel

# =====================================
# プレイヤークラス
# =====================================
class CPlayer:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def update(self):
        if pyxel.btn(pyxel.KEY_LEFT) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_LEFT):
            self.x -= 1
        if pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_RIGHT):
            self.x += 1
        if pyxel.btn(pyxel.KEY_UP) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_UP):
            self.y -= 1
        if pyxel.btn(pyxel.KEY_DOWN) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_DOWN):
            self.y += 1

        if self.x < 0:
            self.x = 0
        if self.x > pyxel.width - 4:
            self.x = pyxel.width - 4

        if self.y < 0:
            self.y = 0
        if self.y > pyxel.height - 4:
            self.y = pyxel.height - 4

    def draw(self):
        pyxel.text(self.x, self.y, ">", 7)
