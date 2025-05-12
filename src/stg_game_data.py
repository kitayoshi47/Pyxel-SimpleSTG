# =====================================
# ゲームデータクラス
# =====================================
class CGameData:
    def __init__(self):
        self.score      = 0     # スコア
        self.play_count = 0     # プレイ回数

    # --------------------
    # 保存データを生成
    # --------------------
    def get_save_data(self):
        return {
            "score": self.score,
            "play_count": self.play_count,
        }

    # --------------------
    # 読み込みデータを設定
    # --------------------
    def set_load_data(self, data):
        self.score      = data.get("score", 0)
        self.play_count = data.get("play_count", 0)

    # --------------------
    # スコア
    # --------------------
    def get_score(self):
        return self.score
    def set_score(self, score):
        self.score = score

    # --------------------
    # プレイ回数
    # --------------------
    def get_play_count(self):
        return self.play_count
    def set_play_count(self, play_count):
        self.play_count = play_count

