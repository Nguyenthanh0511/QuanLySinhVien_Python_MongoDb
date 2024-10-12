from config.db import db
from app.Controllers.SinhVienController import SinhVienController
from tabulate import tabulate
if __name__ == "__main__":
    #Viết menu (Chọn chức năng xem thông tin của các bảng)
    # print(db.sinh_vien.find({}).litmit(5))
    sinhViens = SinhVienController()
    
    # Table headers
    headers = ["_id", "ma_sv", "ten_sv", "tuoi", "ngay_sinh", "so_dien_thoai", "dia_chi", "ma_lop", "create_date", "create_by", "last_update_date", "last_update_by"]
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
    for i in sinhViens.GetAll():
        print("|", end="")
        for key in headers:
            print(f"{i.to_dict()[key]:20}|", end="")
        print()
            
        
        