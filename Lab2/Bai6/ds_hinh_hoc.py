from HinhHoc import HinhHoc
class DanhSachHinhHoc:
    def __init__(self):
        self.ds_hinh_hoc = []
    
    #Them hinh vao danh sach
    def them_hinh(self, hinh_hoc):
        self.ds_hinh_hoc.append(hinh_hoc)

    #Xuat
    def xuat(self):
        for hinh_hoc in self.ds_hinh_hoc:
            print(hinh_hoc)

    
    
    #Tim hinh co dien tich lon nhat
    def tim_phan_so_duong_nho_nhat(self):
        min_phan_so = None
        for phan_so in self.ds_phan_so:
            if phan_so.is_duong():
                if min_phan_so is None or phan_so < min_phan_so:
                    min_phan_so = phan_so
        return min_phan_so
    
    #Tim hinh co dien tich nho nhat
    def tim_vi_tri_phan_so(self, x):
        vi_tri = []
        for i in range(len(self.ds_phan_so)):
            if self.ds_phan_so[i] == x:
                vi_tri.append(i)
        return vi_tri
    
    #Tim hinh tron nho nhat
    def tinh_tong_phan_so_am(self):
        tong = PhanSo(0, 1)
        for phan_so in self.ds_phan_so:
            if phan_so.is_am():
                tong += phan_so
        return tong
    
    #Xoa mot hinh hoc khoi danh sach
    def xoa_hinh(self, hh):
        self.ds_hinh_hoc = [hinh_hoc for hinh_hoc in self.ds_hinh_hoc if hinh_hoc != hh]
    
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
    
    


# Tạo một danh sách hình học
ds = DanhSachHinhHoc()

# Thêm các phân số vào danh sách
ds.them_phan_so(PhanSo(1, 2))
ds.them_phan_so(PhanSo(-3, 4))
ds.them_phan_so(PhanSo(5, -6))
ds.them_phan_so(PhanSo(7, 8))

# Đếm số phân số âm trong danh sách
so_phan_so_am = ds.dem_phan_so_am()
print(f"Số phân số âm trong danh sách là: {so_phan_so_am}")

# Tìm phân số dương nhỏ