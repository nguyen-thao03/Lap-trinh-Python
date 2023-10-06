import functools
import math
from pathlib import Path
from Bai3 import PhanSo

class DanhSachPhanSo:
    def __init__(self, danh_sach = []) -> None:
        self.ds_phan_so = list(danh_sach)
        '''if danh_sach :
            self.ds_phan_so = list(danh_sach)
        else:
            self.ds_phan_so = []'''

    def them(self, ps: PhanSo):
        self.ds_phan_so.append(ps)

    def xuat(self):
        for ps in self.ds_phan_so:
            print(ps, end='\t')
        print()

    def docTuFile(self, tenfile):
        base_path = Path(__file__).parent
        file_path = (base_path / tenfile).resolve()
        with open(file_path, 'r', encoding='utf-8') as f:
            for hang in f:
                du_lieu = hang.split('/')
                self.them(PhanSo(int(du_lieu[0]), int(du_lieu[1])))
    
    # đếm phân số âm trong danh sách - cách 1
    def demPhanSoAm(self):
        dem = 0
        for ps in self.ds_phan_so:
            if ps.laPhanSoAm():
                dem += 1 
        return dem
    
    # đếm phân số âm trong danh sách - cách 2
    def demPhanSoAmSS(self):
        dem = 0
        for ps in self.ds_phan_so:
            # chỉ so sánh được nếu có hàm ghi đè toán tử "<"
            if ps < 0: 
                dem += 1 
        return dem

    # tìm giá trị phân số dương nhỏ nhất
    def timGiaTriPsDuongNhoNhat(self):
        gt_nho_nhat = 1_000_000_000
        for ps in self.ds_phan_so:
            x = ps.tinhGiaTri()
            if x > 0 and x < gt_nho_nhat:
                gt_nho_nhat = x
        return gt_nho_nhat
    
    # tìm danh sách phân số dương nhỏ nhất - cách 1
    def timDSPhanSoDuongNhoNhat(self):
        gt_nho_nhat = self.timGiaTriPsDuongNhoNhat()
        kq = DanhSachPhanSo()
        for ps in self.ds_phan_so:
            if math.isclose(ps.tinhGiaTri(),gt_nho_nhat):
                kq.them(ps)
        return kq
    
    # tìm danh sách phân số dương nhỏ nhất - cách 2
    def timDSPhanSoDuongNhoNhat_C2(self):
        gt_nho_nhat = self.timGiaTriPsDuongNhoNhat()
        return DanhSachPhanSo([ps for ps in self.ds_phan_so if ps.tinhGiaTri() == gt_nho_nhat])

    # tìm phân số dương nhỏ nhất -> trả về phân số dương nhỏ nhất đầu tiên
    def timPhanSoDuongNhoNhat(self):
        ps_nho_nhat = PhanSo(1_000_000)
        for ps in self.ds_phan_so:
            if ps > 0 and ps < ps_nho_nhat:
                ps_nho_nhat = ps
        return ps_nho_nhat

    # tìm phân số dương nhỏ nhất - dùng min --> chỉ trả về 1 phân số trong danh sách
    def timPsDuongNhoNhatDungMin(self):
        return min(self.ds_phan_so, key = lambda x: x > 0 == True)

    # lấy danh sách tất cả phân số âm
    def layDsPsAm(self):
        return DanhSachPhanSo([ps for ps in self.ds_phan_so if ps < 0])

    # tổng các phân số âm trong danh sách
    def tinhTongPsAm(self):
        tongAm = PhanSo()
        for ps in self.ds_phan_so:
            if ps < 0:
                tongAm += ps
        return tongAm
       

    # xóa phân số x trong mảng
    def xoaPhanSo(self, x: PhanSo):
        for ps in self.ds_phan_so:
            if ps == x:
                self.ds_phan_so.remove(ps) 

    # xóa phân số x trong mảng - cách 2
    def xoaPhanSoDungIn(self, x: PhanSo):
        while x in self.ds_phan_so:
            self.ds_phan_so.remove(x) 

    # sắp xếp danh sách phân số tăng theo mẫu
    def sapXepTangTheoMauChonTT(self):
        chieu_dai = len(self.ds_phan_so)
        
        for i in range(chieu_dai):
            vi_tri_min = i
            for j in range(i + 1, chieu_dai):
                if self.ds_phan_so[j].coMauNhoHon(self.ds_phan_so[vi_tri_min]):
                    vi_tri_min = j
            (self.ds_phan_so[i], self.ds_phan_so[vi_tri_min]) = (self.ds_phan_so[vi_tri_min], self.ds_phan_so[i])

    # sắp xếp danh sách phân số tăng theo mẫu
    def sapXepTangTheoMauDoiChoTT(self):
        chieu_dai = len(self.ds_phan_so)
        
        for i in range(chieu_dai):
            for j in range(i + 1, chieu_dai):
                if self.ds_phan_so[j].coMauNhoHon(self.ds_phan_so[i]):
                    (self.ds_phan_so[i], self.ds_phan_so[j]) = (self.ds_phan_so[j], self.ds_phan_so[i])
            
        
        

from Bai3 import PhanSo
class DanhSachPhanSo:
    def __init__(self):
        self.ds_phan_so = []
    
    def dem_phan_so_am(self):
        count = 0
        for phan_so in self.ds_phan_so:
            if phan_so.is_am():
                count += 1
        return count
    
    def tim_phan_so_duong_nho_nhat(self):
        min_phan_so = None
        for phan_so in self.ds_phan_so:
            if phan_so.is_duong():
                if min_phan_so is None or phan_so < min_phan_so:
                    min_phan_so = phan_so
        return min_phan_so
    
    def tim_vi_tri_phan_so(self, x):
        vi_tri = []
        for i in range(len(self.ds_phan_so)):
            if self.ds_phan_so[i] == x:
                vi_tri.append(i)
        return vi_tri
    
    def tinh_tong_phan_so_am(self):
        tong = PhanSo(0, 1)
        for phan_so in self.ds_phan_so:
            if phan_so.is_am():
                tong += phan_so
        return tong
    
    def xoa_phan_so(self, x):
        self.ds_phan_so = [phan_so for phan_so in self.ds_phan_so if phan_so != x]
    
    def xoa_phan_so_co_tu(self, x):
        self.ds_phan_so = [phan_so for phan_so in self.ds_phan_so if phan_so.tu_so != x]
    
    def sap_xep_tang_tu_so(self):
        self.ds_phan_so.sort(key=lambda phan_so: phan_so.tu_so)
    
    def sap_xep_giam_tu_so(self):
        self.ds_phan_so.sort(key=lambda phan_so: phan_so.tu_so, reverse=True)
    
    def sap_xep_tang_mau_so(self):
        self.ds_phan_so.sort(key=lambda phan_so: phan_so.mau_so)
    
    def sap_xep_giam_mau_so(self):
        self.ds_phan_so.sort(key=lambda phan_so: phan_so.mau_so, reverse=True)
    
    def them_phan_so(self, phan_so):
        self.ds_phan_so.append(phan_so)
    
    def hien_thi(self):
        for phan_so in self.ds_phan_so:
            print(phan_so)


# Tạo một danh sách phân số
ds = DanhSachPhanSo()

# Thêm các phân số vào danh sách
ds.them_phan_so(PhanSo(1, 2))
ds.them_phan_so(PhanSo(-3, 4))
ds.them_phan_so(PhanSo(5, -6))
ds.them_phan_so(PhanSo(7, 8))

# Đếm số phân số âm trong danh sách
so_phan_so_am = ds.dem_phan_so_am()
print(f"Số phân số âm trong danh sách là: {so_phan_so_am}")

# Tìm phân số dương nhỏ




class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return str(self.numerator) + "/" + str(self.denominator)

class FractionList:
    def __init__(self):
        self.fractions = []

    def count_negative_fractions(self):
        count = 0
        for fraction in self.fractions:
            if fraction.numerator < 0 or fraction.denominator < 0:
                count += 1
        return count

    def find_smallest_positive_fraction(self):
        positive_fractions = [fraction for fraction in self.fractions if fraction.numerator > 0 and fraction.denominator > 0]
        if len(positive_fractions) == 0:
            return None
        smallest_fraction = positive_fractions[0]
        for fraction in positive_fractions:
            if fraction.numerator * smallest_fraction.denominator < smallest_fraction.numerator * fraction.denominator:
                smallest_fraction = fraction
        return smallest_fraction

    def find_positions_of_fraction(self, x):
        positions = []
        for i, fraction in enumerate(self.fractions):
            if fraction.numerator == x.numerator and fraction.denominator == x.denominator:
                positions.append(i)
        return positions

    def sum_negative_fractions(self):
        total = 0
        for fraction in self.fractions:
            if fraction.numerator < 0 or fraction.denominator < 0:
                total += fraction.numerator / fraction.denominator
        return total

    def remove_fraction(self, x):
        self.fractions = [fraction for fraction in self.fractions if fraction.numerator != x.numerator or fraction.denominator != x.denominator]

    def remove_fractions_with_numerator(self, x):
        self.fractions = [fraction for fraction in self.fractions if fraction.numerator != x]

    def sort_fractions_asc(self):
        self.fractions.sort(key=lambda fraction: fraction.numerator / fraction.denominator)

    def sort_fractions_desc(self):
        self.fractions.sort(key=lambda fraction: fraction.numerator / fraction.denominator, reverse=True)

    def sort_fractions_by_numerator_asc(self):
        self.fractions.sort(key=lambda fraction: fraction.numerator)

    def sort_fractions_by_numerator_desc(self):
        self.fractions.sort(key=lambda fraction: fraction.numerator, reverse=True)

        # Tạo danh sách phân số
fraction_list = FractionList()
fraction_list.fractions = [Fraction(-1, 2), Fraction(3, 4), Fraction(-2, 5), Fraction(1, 3)]

# Kiểm tra số phân số âm trong danh sách
count_negative = fraction_list.count_negative_fractions()
print("Số phân số âm trong danh sách:", count_negative)  # Kết quả mong đợi: 25

# Tìm phân số dương nhỏ nhất
smallest_positive = fraction_list.find_smallest_positive_fraction()
print("Phân số dương nhỏ nhất:", smallest_positive)  # Kết quả mong đợi: 1/3

# Tìm vị trí của phân số x trong danh sách
x = Fraction(-2, 5)
positions = fraction_list.find_positions_of_fraction(x)
print("Vị trí của phân số", x, "trong danh sách:", positions)  # Kết quả mong đợi: [2]

# Tổng các phân số âm trong danh sách
sum_negative = fraction_list.sum_negative_fractions()
print("Tổng các phân số âm trong danh sách:", sum_negative)  # Kết quả mong đợi: -0.7

# Xóa phân số x trong danh sách
fraction_list.remove_fraction(x)
print("Danh sách sau khi xóa phân số", x, ":", fraction_list.fractions)  # Kết quả mong đợi: [-1/2, 3/4, 1/3]

# Xóa tất cả các phân số có tử là x
numerator_to_remove = 3
fraction_list.remove_fractions_with_numerator(numerator_to_remove)