from sinh_vien import SinhVien
import datetime

class SinhVienChinhQuy(SinhVien):
    def _init_(self, maSo: int, hoTen: str, ngaySinh: datetime, diemRL: int) -> None:
        super()._init_(maSo, hoTen, ngaySinh)
        self.diemRL = diemRL

    def _str_(self) -> str:
        return super()._str_() + f"\t{self.diemRL}"