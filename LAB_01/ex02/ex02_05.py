so_gio_lam = float(input("nhap so gio lam moi tuan :"))
luong_gio = float(input("nhap thu lao tren moi gio lam tieu chuan: "))
gio_tieu_chuan = 44 # so gio lam moi ngay
gio_vuot_chuan= max(0,so_gio_lam - gio_tieu_chuan)
thuc_linh = gio_tieu_chuan*luong_gio+gio_vuot_chuan*luong_gio*1.5
print(f"so tien thuc linh cua nhan vien:{thuc_linh}")