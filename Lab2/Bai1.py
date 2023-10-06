#Bài 1: Cài đặt lớp Sinh viên và danh sách sinh viên như sau và hoàn thành các hàm còn trống (chưa có nội dung)
import datetime
f = open("D:\CTK45A\Năm 3\Lập trình python\Lab2\sinhvien.txt", "r")
print(f.read())
class SinhVien:
    #Biến của lớp, chung cho tất cả các đối tượng thuộc lớp
    truong = "Đại học Đà Lạt"
    # Hàm khởi tạo, hàm tạo lập: khởi gán các thuộc tính của đối tượng
    def __init__(self, maSo: int, hoTen: str, ngaySinh: datetime) -> None:
        self.__maSo = maSo
        self.__hoTen = hoTen
        self.__ngaySinh = ngaySinh

    # cho phép truy xuất tới thuộc tính từ bên ngoài thông qua trường maSO

    @property
    def maSo(self):
        return self.__maSo
    # cho phép thay đổi giá trị thuộc tính maSO
    @maSo.setter
    def maSo(self, maso):
        if self.laMaSoHopLe(maso):
            self.__maSo = maso
    # Phương thức tĩnh: ccas phương thức không truy xuất gì ddeeens thuộc tính, hành vi của lớp
    # những phương thức này không cần truyền tham số mặc định self
    # đây không phải lf một hành vi( phương thức) của một đối tượng thuộc lớp
    @staticmethod
    def laMaSoHopLe(maso:int):
        return len(str(maso))== 7
    # Phương thức của lớp, chỉ xuất tới các biến thành viên của lớp
    #không truy cuất được các thuộc tính riêng của đối tượng
    @classmethod
    def doiTenTruong(self, tenmoi):
        self.truong = tenmoi
    # tương tự ghi đè phương thức toString()
    def __str__(self) -> str:
        return f"{self.__maSo}\t{self.__hoTen}\t{self.__ngaySinh}"
    # hành vi của đối tượng sinh viên
    def Xuat(self):
        print(f"{self.__maSo}\t{self.__hoTen}\t{self.__ngaySinh}")

class DanhSachSv:
    def __init__(self) -> None:
        self.dssv = []
    def themSinhVien(self,sv: SinhVien):
        self.dssv.append(sv)
    def xuat(self):
        for sv in self.dssv:
            print(sv)

    # Tìm sinh viên theo mssv, nếu có trả về sinh viên
    def timSVTheoMssv(self, mssv: int):
        return [sv for sv in self.dssv if sv.mssv == mssv]
    # tìm sinh viên theo msssv. nếu có trả về vị trí của sinh viên trong danh sách
    def timVTSvTheoMssv(self, mssv:int):
        for i in range(len(self.dssv)):
            if self.dssv[i].mssv == mssv:
                return i
        return -1
    # xóa sinh viên có mã số mssv, thông báo xóa được hoặc không
    def xoaSVTheoMssv(self, maSo:int) -> bool:
        vt = self.timVTSvTheoMssv(maSo)
        if vt != -1:
            del self.dssv[vt]
            return True
        else:
            return False
   # Tìm sinh viên tên "Nam"
    def timSvTheoTen(self):
        for i in range(len(self.dssv)):
            if self.dssv[i].ten == "Nam":
                return i
        return -1

    # Tìm những sinh viên sinh trước ngày
    def timSvSinhTruocNgay(self, ngay: datetime):
        for i in range(len(self.dssv)):
            if self.dssv[i].ngay < ngay:
                return i
        return -1
    # Sắp xếp tăng theo họ tên
    def sapXepTangTheoHoTen(self):
        self.dssv.sort(key=lambda sv: sv.hoTen)
    # sắp xếp giảm theo họ tên
    def sapXepGiamTheoHoTen(self):
        self.dssv.sort(key=lambda sv: sv.hoTen, reverse=True)
    
ds_sv = DanhSachSv()
# Thêm sinh viên vào danh sách
# ...

# Sắp xếp tăng dần theo họ tên
ds_sv.sapXepTangTheoHoTen()
ds_sv.xuat()

# Sắp xếp giảm dần theo họ tên
ds_sv.sapXepGiamTheoHoTen()
ds_sv.xuat()
