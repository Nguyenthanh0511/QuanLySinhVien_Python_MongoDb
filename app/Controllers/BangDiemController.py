import pymongo
import random
from faker import Faker
from config.db import db
from app.Models.BangDiem import BangDiem
from app.Views.DiemView import BangDiemView
# hàm sinh dữ liệu ngẫu nhiên cho NghanhHoc
fake = Faker()

def GenDataBangDiem(num_records):
    bang_diem_list = []
    
    for _ in range(num_records):
        ma_bang_diem = fake.unique.random_int(min=10000, max=99999)  # Tạo mã bảng điểm duy nhất
        diem_kt_1 = round(random.uniform(0, 10), 2)  # Điểm kiểm tra 1
        diem_kt_2 = round(random.uniform(0, 10), 2)  # Điểm kiểm tra 2
        diem_giua_ky = round(random.uniform(0, 10), 2)  # Điểm giữa kỳ
        diem_cuoi_ky = round(random.uniform(0, 10), 2)  # Điểm cuối kỳ
        ma_sv = fake.random_int(min=10000, max=99999)  # Mã sinh viên
        ma_mon_hoc = fake.random_int(min=100, max=999)  # Mã môn học

        bang_diem = {
            "MaBangDiem": ma_bang_diem,
            "DiemKT_1": diem_kt_1,
            "DiemKT_2": diem_kt_2,
            "DiemGiuaKy": diem_giua_ky,
            "DiemCuoiKy": diem_cuoi_ky,
            "MaSv": ma_sv,
            "MaMonHoc": ma_mon_hoc
        }
        bang_diem_list.append(bang_diem)
    
    return bang_diem_list

def insert_bang_diem_to_mongo(records):
    try:
        # Kết nối tới MongoDB
        client = pymongo.MongoClient("mongodb+srv://hoang:hoang@quanlysinhvien.kjj0s.mongodb.net/")
        db = client["QuanLySinhVien_Ver2"]
        collection = db["BangDiem"]

        # Thêm dữ liệu vào collection
        result = collection.insert_many(records)
        print(f"Inserted {len(result.inserted_ids)} records into BangDiem.")
    except pymongo.errors.ConnectionFailure as e:
        print(f"Connection failed: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        client.close()

# Sử dụng hàm để tạo dữ liệu giả cho 10 bản ghi BangDiem
records = GenDataBangDiem(10)

# Thêm các bản ghi vào MongoDB
insert_bang_diem_to_mongo(records)
        
        
# Hiển thị thông tin Ngành Học
class BangDiemController:
    def __init__(self):
        pass
      
    def getALL(self):
        bangDiemDb = db.BangDiem.find()
        bangDiemLists = [BangDiem(**bangDiem) for bangDiem in bangDiemDb]
        BangDiemView().ShowBangDiem(bangDiemLists)
        
    def CreateBangDiem(self):
        try:
            bangDiem = BangDiemView().InputBangDiem()
            bangDiemInsert = db.SinhVien.insert_one(bangDiem)
            if bangDiemInsert.acknowledged:
                print("Bang Diem created successfully!")
            else:
                print("Error creating Bang Diem.")
            return bangDiemInsert
        except Exception as e:
            print(e)
            
    