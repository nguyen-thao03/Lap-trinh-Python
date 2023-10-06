f = open("D:\CTK45A\Năm 3\Lập trình python\Lab2\sinhvien.txt", "r")
print(f.read())

def sapXepTangTheoHoTen(self):
        self.dssv.sort(key=lambda sv: sv.hoTen)
    # sắp xeeos giảm theo họ tên
def sapXepGiamTheoHoTen(self):
        self.dssv.sort(key=lambda sv: sv.hoTen, reverse=True)