from sinh_vien_chinh_quy import SinhVienChinhQuy
from sinh_vien_phi_chinh_quy import SinhVienPhiCQ
from sinh_vien import SinhVien
import datetime
class DanhSachSv2:
    def _init_(self) -> None:
        self.dssv = []

    def themSV(self, sv):
        self.dssv.append(sv)

    def xuat(self):
        for sv in self.dssv:
            print(sv)

    def timSvTheoMs(self, ms: str):
        for i in range(len(self.dssv)):
            if self.dssv[i].mssv == ms:
                return i
            else:
                return -1

    def timSvTheoLoai(self, loai: str):
        if loai == "chinhquy":
            return [sv for sv in self.dssv if isinstance(sv, SinhVienChinhQuy)]
        return [sv for sv in self.dssv if isinstance(sv, SinhVienPhiCQ)]
    
    #tìm sinh viên có điểm rèn luyện từ 80 trở lên
    def timSV_DiemRL(self, diemRL:int):
        sinh_vien_diemrl_80 = []
        for i in range(len(self.dssv)):
            if self.dssv[i].diemRL >= 80:
                return sinh_vien_diemrl_80
        return -1

    #tìm sinh viên có trình độ cao đẳng sinh trước 15/8/1999
    def timSV_CD_TruocNgay(self, ngay: datetime):
        for i in range(len(self.dssv)):
            if self.dssv[i].ngay < ngay & self.dssv[i].trinhdo == "Cao đẳng":
                return i
        return -1