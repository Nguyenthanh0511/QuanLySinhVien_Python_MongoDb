import pymongo
import random
from faker import Faker
from config.db import db
from app.Models.HoatDongNgoaiKhoa import HoatDongNgoaiKhoa
from app.Views.HoatDongNgoaiKhoaView import HoatDongNgoaiKhoaView

fake = Faker()

def GenDataHoatDongNgoaiKhoa(num_records):
    hoat_dong_list = []
    
    for _ in range(num_records):
        ma_hd = fake.unique.random_int(min=100, max=999)  # Unique activity code
        ten_hd = random.choice(['Chạy bộ từ thiện', 'Ngày hội sách', 'Lớp học kỹ năng mềm', 'Hoạt động bảo vệ môi trường', 'Thể thao ngoài trời'])
        
        hoat_dong = {
            "MaHD": ma_hd,
            "TenHD": ten_hd
        }
        
        hoat_dong_list.append(hoat_dong)
    return hoat_dong_list

def insert_hoat_dong_to_mongo(hoat_dong_data):
    try:
        # MongoDB connection
        client = pymongo.MongoClient("mongodb+srv://hoang:hoang@quanlysinhvien.kjj0s.mongodb.net/")
        db = client["QuanLySinhVien_Ver2"]
        collection = db["HoatDongNgoaiKhoa"]

        # Insert data
        result = collection.insert_many(hoat_dong_data)
        print(f"Inserted {len(result.inserted_ids)} record(s) into the 'HoatDongNgoaiKhoa' collection.")
    except pymongo.errors.ConnectionFailure as e:
        print(f"Connection failed: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        client.close()

# Generate and insert data for 10 extracurricular activities
hoat_dong_data = GenDataHoatDongNgoaiKhoa(10)
insert_hoat_dong_to_mongo(hoat_dong_data)

class HoatDongNgoaiKhoaController:
    def __init__(self):
        pass
      
    def getALL(self):
        hoatDongNgoaiKhoaDb = db.HoatDongNgoaiKhoa.find()
        hoatDongNgoaiKhoaLists = [HoatDongNgoaiKhoa(**hoatDongNgoaiKhoa) for hoatDongNgoaiKhoa in hoatDongNgoaiKhoaDb]
        HoatDongNgoaiKhoaView().ShowKhoa(hoatDongNgoaiKhoaLists)
        
    def CreateHoatDongNgoaiKhoa(self):
        try:
            hoatDongNgoaiKhoa = HoatDongNgoaiKhoaView().InputHoatDongNgoaiKhoa()
            hoatDongNgoaiKhoaInsert = db.HoatDongNgoaiKhoa.insert_one(hoatDongNgoaiKhoa)
            if hoatDongNgoaiKhoaInsert.acknowledged:
                print("Hoat dong ngoai khoa created successfully!")
            else:
                print("Error creating Hoat dong ngoai khoa.")
            return hoatDongNgoaiKhoaInsert
        except Exception as e:
            print(e)