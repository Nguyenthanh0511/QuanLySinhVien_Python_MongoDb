from config.db import db
from app.Models.SinhVien import SinhVien
#Hiển thị thông tin
class SinhVienController:
    def __init__(selft):
        pass
    def GetAll(selft):
        sinhVienDb = db.sinh_vien.find()
        sinhVienLists = [SinhVien(**sinhVien) for sinhVien in sinhVienDb]
        return sinhVienLists
    
    