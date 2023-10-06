# HinhTron.py
import HinhHoc
import math
class HinhTron:
    def __init__(self, BanKinh):
        self.BanKinh = BanKinh

    def TinhDienTich(self):
        return self.BanKinh ** 2 * math.pi

