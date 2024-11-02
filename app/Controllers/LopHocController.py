import random
import pymongo
import faker
from config.db import db
from app.Models.LopHoc import LopHoc
from app.Views.LopHocView import LopHocView

# hàm sinh dữ liệu
import random
from pymongo import MongoClient

# Kết nối đến MongoDB
client = MongoClient('mongodb+srv://hoang:hoang@quanlysinhvien.kjj0s.mongodb.net/')  # Chỉnh sửa nếu cần
db = client['QuanLySinhVien_2']  # Tên database của bạn
lop_hoc_collection = db['LopHoc']  # Tạo collection LopHoc nếu chưa có

def sinh_du_lieu_lop_hoc(so_lop: int):
    data = []
    for i in range(so_lop):
        ma_lop = f"L{i+1:03}"  # Đặt mã lớp dạng L001, L002,...
        ten_lop = f"Lớp {i+1}"
        so_luong_sinh_vien = random.randint(20, 50)  # Random số lượng sinh viên từ 20 đến 50
        lop_hoc = {
            "MaLop": ma_lop,
            "TenLop": ten_lop,
            "SoLuongSinhVien": so_luong_sinh_vien
        }
        data.append(lop_hoc)
    return data

def luu_vao_mongodb(data):
    lop_hoc_collection.insert_many(data)
    print(f"Đã lưu {len(data)} lớp học vào MongoDB")

# Sử dụng hàm
so_lop = 10  # Số lượng lớp học muốn tạo
data = sinh_du_lieu_lop_hoc(so_lop)
luu_vao_mongodb(data)

# hiển thị thông tin
class LopHocController:
    def __init__(self) -> None:
        pass
    
    def GetAll(self):
        lopHocDb = db.SinhVien.find()
        lopHocLists = [LopHoc(**lopHoc) for lopHoc in lopHocDb]
        LopHocView().ShowLopHoc(lopHocLists)
    
    def CreateLopHoc(self):
        try:
            lopHoc = LopHocView().InputLopHoc()
            lopHocInsert = db.SinhVien.insert_one(lopHoc)
            if lopHocInsert.acknowledged:
                print("Lop hoc created successfully!")
            else:
                print("Error creating lop hoc.")
            return lopHocInsert
        except Exception as e:
            print(e)
    
    def GenDataLopHoc(self,num_classes):
        client = pymongo.MongoClient("mongodb+srv://hoang:hoang@quanlysinhvien.kjj0s.mongodb.net/")
        db = client["QuanLySinhVien_Ver2"]
        collection = db["LopHoc"]

        prefix_list = ["CNTT", "QTKD", "NNTQ"]
        lop_hoc_list = []

        for _ in range(num_classes):
            prefix = random.choice(prefix_list)
            suffix = f"{random.randint(1, 10):02d}"
            while True:
                ma_lop = f"{prefix}{suffix}"
                if collection.find_one({"MaLop":ma_lop}) is None:
                    ten_lop = ma_lop
                    so_luong_sv = random.randint(35, 45)

                    lop_hoc = LopHoc(MaLop=ma_lop, TenLop=ten_lop, SoLuongSinhVien=so_luong_sv)
                    lop_hoc_list.append(lop_hoc.to_dict())
                    break
                else:
                    continue
                
          # Insert generated data into MongoDB collection
        if lop_hoc_list:
            result = collection.insert_many(lop_hoc_list)
            print(f"Inserted {len(result.inserted_ids)} LopHoc documents into MongoDB.")
        else:
            print("No unique LopHoc documents to insert.")

        # Close the client connection only after all operations are done
        client.close()