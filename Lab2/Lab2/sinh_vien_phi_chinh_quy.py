from sinh_vien import SinhVien
from datetime import datetime

class SinhVienPhiCQ(SinhVien):
    def _init_(self, maSo: int, hoTen: str, ngaySinh: datetime, trinhdo: str, tgdt: int) -> None:
        super()._init_(maSo, hoTen, ngaySinh)
        self.thoiGianDaoTao = tgdt
        self.trinhDo = trinhdo

    def _str_(self) -> str:
        return super()._str_() + f"\t{self.trinhDo}\t{self.thoiGianDaoTao}"