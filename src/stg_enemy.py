import pyxel

# =====================================
# 定数定義
# =====================================
MAX_NUM = 8

# =====================================
# エンティティ
# =====================================
enemies = []

def update():
    for entity in enemies:
        entity.update()

def draw():
    for entity in enemies:
        entity.draw()

def cleanup():
    for i in range(len(enemies) - 1, -1, -1):
        if not enemies[i].is_alive:
            del enemies[i]

# =====================================
# 敵クラス
# =====================================
class CEnemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.is_alive = True
        if len(enemies) < MAX_NUM:
            enemies.append(self)

    def update(self):
        self.x -= 2
        if self.x < 0:
            self.is_alive = False

    def draw(self):
        pyxel.text(self.x, self.y, "#", 7)
