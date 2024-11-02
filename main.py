from config.db import db
from app.Controllers.SinhVienController import SinhVienController
from app.Controllers.LopHocController import LopHocController
from app.Controllers.KhoaController import KhoaController
from app.Controllers.NganhHocController import NganhHocController
from tabulate import tabulate
def main_menu_parent():
    print("\nMenu:")
    print("1. View relate to Sinh Vien")
    print("2. View relate to Khoa hoc")
    print("3. View relate to Lop")
    print("4. View relate to Khoa")
    print("5. View relate to NghanhHoc")
    print("6. View report")
    print("7. Exit")
    print("Enter your choice (1-7): ")
    choice = input()
    return choice

def main_menu_child():
    print("\nMenu:")
    print("1. Create")
    print("2. View all")
    print("3. View a specific object by ID")
    print("4. Update")
    print("5. Delete")
    print("6. Init Data")
    print("Enter your choice (1-6): ")
    choice = input()
    return choice

if __name__ == "__main__":
            
    while True:
        numberChoice = main_menu_parent()
        if numberChoice == "1":
            sinhViens = SinhVienController()
            numberChoiceChild = main_menu_child()
            if numberChoiceChild == "1":
                sinhViens.CreateSinhVien()
            elif numberChoiceChild == "2":
                sinhViens.GetAll()
            elif numberChoiceChild == "6": 
                for i in range(10):
                    print("Khoi tao lan :",i)
                    # sinhViens.GenDataSinhVien()
        elif numberChoice=="3":
            lops = LopHocController()
            numberChoiceChild = main_menu_child()
            if numberChoiceChild == "1":
                sinhViens.CreateSinhVien()
            elif numberChoiceChild == "2":
                sinhViens.GetAll()
            elif numberChoiceChild == "6": 
                lops.GenDataLopHoc(10)
                    # sinhViens.GenDataSinhVien()            
        elif numberChoice=="4":
            khoas = KhoaController()
            numberChoiceChild = main_menu_child()
            if numberChoiceChild == "1":
                sinhViens.CreateSinhVien()
            elif numberChoiceChild == "2":
                sinhViens.GetAll()
            elif numberChoiceChild == "6":
                khoas.GenDataKhoa(10)
        elif numberChoice=="5":
            nghanhHocs = NganhHocController()
            numberChoiceChild = main_menu_child()
            if numberChoiceChild == "1":
                sinhViens.CreateSinhVien()
            elif numberChoiceChild == "2":
                sinhViens.GetAll()
            elif numberChoiceChild == "6":
                nghanhHocs.GenDataNghanhHoc(10)