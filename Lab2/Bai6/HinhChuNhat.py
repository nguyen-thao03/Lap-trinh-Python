# HinhChuNhat.py
import HinhHoc
class HinhChuNhat:
    def __init__(self, chieu_dai, chieu_rong):
        self.chieu_dai = chieu_dai
        self.chieu_rong = chieu_rong

    def TinhDienTich(self):
        return self.chieu_dai * self.chieu_rong
