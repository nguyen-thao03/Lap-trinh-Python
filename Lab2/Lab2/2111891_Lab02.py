import datetime
class SinhVien:
    truong = "Đại học Đà Lạt"
    
    def _init_(self, maSo: int, hoTen: str, ngaySinh: datetime) -> None:
        self._maSo = maSo
        self._hoTen = hoTen
        self._ngaySinh = ngaySinh

        @property
        def maSo(self):
            return self._maSo

        @maSo.setter
        def maSo(self, maso):
            if self.laMaSoHopLe(maso):
                self._maSo = maso
        
        @staticmethod
        def laMaSoHopLe(maso: int):
            return len(str(maso)) == 7

        @classmethod
        def doiTenTruong(self, tenmoi):
            self.truong = tenmoi

        def _str_(self) -> str:
            return f"{self._maSo}\t{self._hoTen}\t{self._ngaySinh}"

        def xuat(self):
            print(f"{self._maSo}\t{self._hoTen}\t{self._ngaySinh}")
