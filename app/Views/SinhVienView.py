
from app.Models.SinhVien import SinhVien
class SinhVienView:
    def __init__(self):
        pass
    def ShowSinhVien(self, sinhVienLists):
        headers = ["ma_sv", "ten_sv", "tuoi", "ngay_sinh", "so_dien_thoai", "dia_chi", "ma_lop", "create_date", "create_by", "last_update_date", "last_update_by"]
        print("|", end="")
        for header in headers:
            print(f"{header:20}|", end="")
        print()

        # Print table separator
        print("|", end="")
        for _ in headers:
            print("-" * 20 + "|", end="")
        print()

        # Print student data
        for i in sinhVienLists:
            print("|", end="")
            for key in headers:
                print(f"{i.to_dict()[key]:20}|", end="")
            print()
    
    def InputSinhVien(self):
        ma_sv = input("Enter ma_sv: ")
        ten_sv = input("Enter ten_sv: ")
        tuoi = input("Enter tuoi: ")
        ngay_sinh = input("Enter ngay_sinh: ")
        so_dien_thoai = input("Enter so_dien_thoai: ")
        dia_chi = input("Enter dia_chi: ")
        ma_lop = input("Enter ma_lop: ")
        create_date = input("Enter create_date: ")
        create_by = input("Enter create_by: ")
        last_update_date = input("Enter last_update_date: ")
        last_update_by = input("Enter last_update_by: ")

        sinhVienData = {
            "ma_sv": ma_sv,
            "ten_sv": ten_sv,
            "tuoi": tuoi,
            "ngay_sinh": ngay_sinh,
            "so_dien_thoai": so_dien_thoai,
            "dia_chi": dia_chi,
            "ma_lop": ma_lop,
            "create_date": create_date,
            "create_by": create_by,
            "last_update_date": last_update_date,
            "last_update_by": last_update_by
        }
        sinhVien = SinhVien(**sinhVienData).to_dict()
        return sinhVien
