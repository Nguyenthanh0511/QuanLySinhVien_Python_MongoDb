from config.db import db
from app.Controllers.SinhVienController import SinhVienController
from tabulate import tabulate
def main_menu_parent():
    print("\nMenu:")
    print("1. View relate to Sinh Vien")
    print("2. View relate to Khoa hoc")
    print("3. View relate to Lop")
    print("4. View report")
    print("5. Exit")
    print("Enter your choice (1-5): ")
    choice = input()
    return choice

def main_menu_child():
    print("\nMenu:")
    print("1. Create")
    print("2. View all")
    print("3. View a specific object by ID")
    print("4. Update")
    print("5. Delete")
    print("6. Exit")
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
        