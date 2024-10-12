from config.db import db
from app.Models.SinhVien import SinhVien
from app.Views.SinhVienView import SinhVienView
#Hiển thị thông tin
class SinhVienController:
    def __init__(selft):
        pass
    def GetAll(selft):
        sinhVienDb = db.sinh_vien.find()
        sinhVienLists = [SinhVien(**sinhVien) for sinhVien in sinhVienDb]
        SinhVienView().ShowSinhVien(sinhVienLists)
        
    def CreateSinhVien(self):
        try:
            sinhVien = SinhVienView().InputSinhVien()
            sinhVienInsert = db.sinh_vien.insert_one(sinhVien)
            if sinhVienInsert.acknowledged:
                print("Sinh vien created successfully!")
            else:
                print("Error creating sinh vien.")
            return sinhVienInsert
        except Exception as e:
            print(e)