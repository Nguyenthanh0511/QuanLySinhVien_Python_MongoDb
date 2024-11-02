import pymongo
import random
from faker import Faker
from config.db import db
from bson import ObjectId
from app.Models.NganhHoc import NganhHoc
from app.Views.NganhHocView import NganhHocView
from datetime import datetime
# hàm sinh dữ liệu ngẫu nhiên cho NghanhHoc
fake = Faker()
# Hiển thị thông tin Ngành Học
class NganhHocController:
    def __init__(self):
        pass
      
    def getALL(self):
        nganhHocDb = db.NghanhHoc.find()
        nganhHocLists = [NganhHoc(**nganhHoc) for nganhHoc in nganhHocDb]
        NganhHocView().ShowNganhHoc(nganhHocLists)
        
    def CreateSinhVien(self):
        try:
            nghanhHoc = NganhHocView().InputNganhHoc()
            nghanhHocInsert = db.SinhVien.insert_one(nghanhHoc)
            if nghanhHocInsert.acknowledged:
                print("Nghanh Hoc created successfully!")
            else:
                print("Error creating nghanh Hoc.")
            return nghanhHocInsert
        except Exception as e:
            print(e)
    
    def GenDataKhoa(self, num_records):
        """
        Tạo dữ liệu ngẫu nhiên cho NganhHoc và chèn vào bộ sưu tập MongoDB.
        """
        # Thiết lập kết nối đến MongoDB
        client = pymongo.MongoClient("mongodb+srv://hoang:hoang@quanlysinhvien.kjj0s.mongodb.net/")
        db = client["QuanLySinhVien_Ver2"]
        collection = db["Khoa"]

       # Dữ liệu cần chèn
        data_to_insert = [
            {
                "MaKhoa": "CNTT",
                "TenKhoa": "Khoa Công nghệ thông tin",
                "DiaChiVPK": "123 Đường A, Quận 1, TP.HCM",
                "SDTKhoa": "0123456789",
                "NgayThanhLap": datetime.strptime("2000-01-01", "%Y-%m-%d")
            },
            {
                "MaKhoa": "QTKD",
                "TenKhoa": "Khoa Quản trị kinh doanh",
                "DiaChiVPK": "456 Đường B, Quận 2, TP.HCM",
                "SDTKhoa": "0987654321",
                "NgayThanhLap": datetime.strptime("2005-05-20", "%Y-%m-%d")
            },
            {
                "MaKhoa": "NNTQ",
                "TenKhoa": "Khoa Ngôn ngữ Trung Quốc",
                "DiaChiVPK": "789 Đường C, Quận 3, TP.HCM",
                "SDTKhoa": "0912345678",
                "NgayThanhLap": datetime.strptime("2010-10-15", "%Y-%m-%d")
            }
        ]

        # Chèn dữ liệu vào MongoDB
        result = collection.insert_many(data_to_insert)
        print(f"Đã chèn {len(result.inserted_ids)} bản ghi vào bộ sưu tập 'Khoa'.")

# Sử dụng ví dụ
nganh_hoc_controller = NganhHocController()
# nganh_hoc_controller.GenDataNghanhHoc(10)  # Tạo 10 bản ghi ngẫu nhiên    
    