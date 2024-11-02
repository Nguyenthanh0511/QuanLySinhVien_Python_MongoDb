import pymongo
import random
from faker import Faker
from config.db import db
from app.Models.Khoa import Khoa
from app.Views.KhoaView import KhoaView
from datetime import datetime

from bson import ObjectId
fake = Faker()

class KhoaController:
    def __init__(self):
        # MongoDB connection
        self.client = pymongo.MongoClient("mongodb+srv://hoang:hoang@quanlysinhvien.kjj0s.mongodb.net/")
        self.db = self.client["QuanLySinhVien_Ver2"]
        self.collection = self.db["Khoa"]
      
    def getALL(self):
        khoaDb = self.collection.find()
        khoaLists = [Khoa(**khoa) for khoa in khoaDb]
        KhoaView().ShowKhoa(khoaLists)
        
    def CreateKhoa(self):
        try:
            khoa = KhoaView().InputKhoa()
            khoaInsert = self.collection.insert_one(khoa)
            if khoaInsert.acknowledged:
                print("Khoa created successfully!")
            else:
                print("Error creating Khoa.")
            return khoaInsert
        except Exception as e:
            print(e)
    
    # def is_valid_date(self, date_value):
    #     """
    #     Kiểm tra xem giá trị ngày có hợp lý hay không.
    #     """
    #     if isinstance(date_value, str):
    #         try:
    #             # Kiểm tra nếu chuỗi có định dạng đúng YYYY-MM-DD
    #             datetime.strptime(date_value, "%Y-%m-%d")
    #             return True
    #         except ValueError:
    #             return False
    #     elif isinstance(date_value, datetime):
    #         return True
    #     else:
    #         return False
    
    def GenDataKhoa(self, num_records):
        """
        Generates random Khoa data and inserts it into the MongoDB 'khoa' collection.
        """
        try:
            khoa_list = []
            
            for _ in range(num_records):
                # Tạo ObjectId ngẫu nhiên
                id_khoa = ObjectId()
                ma_khoa = fake.unique.random_int(min=100, max=999)  # Unique department code
                ten_khoa = random.choice(['Khoa Công nghệ thông tin', 'Khoa Quản trị kinh doanh', 'Khoa Ngôn ngữ Trung Quốc'])
                dia_chi_vpk = fake.address().replace("\n", ", ")  # Office address
                sdt_khoa = fake.phone_number()  # Department phone number
                # Ngày thành lập ngẫu nhiên trong khoảng 30 năm trước
                ngay_thanh_lap = fake.date_between(start_date='-30y', end_date='today')
                # Kiểm tra kiểu dữ liệu
                print(f"Kiểu dữ liệu của ngay_thanh_lap: {type(ngay_thanh_lap)}")  # In ra kiểu dữ liệu
            
                # if isinstance(ngay_thanh_lap, datetime.date):  # Kiểm tra xem có phải là datetime.date không
                #     # Chuyển đổi ngày thành datetime
                #     ngay_thanh_lap_datetime = datetime.combine(ngay_thanh_lap, datetime.min.time())
                # else:
                #     raise ValueError("Ngày thành lập không phải là kiểu date hợp lệ.")
                khoa = {
                    "_id": id_khoa,
                    "MaKhoa": ma_khoa,
                    "TenKhoa": ten_khoa,
                    "DiaChiVPK": dia_chi_vpk,
                    "SDTKhoa": sdt_khoa,
                    "NgayThanhLap": ngay_thanh_lap
                }
                
                khoa_list.append(khoa)

            # Insert generated data into MongoDB
            result = self.collection.insert_many(khoa_list)
            print(f"Inserted {len(result.inserted_ids)} record(s) into the 'Khoa' collection.")
        except pymongo.errors.ConnectionFailure as e:
            print(f"Connection failed: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")
        finally:
            self.client.close()  # Ensure MongoDB connection is closed

# Usage example
khoa_controller = KhoaController()
khoa_controller.GenDataKhoa(10)  # Generate and insert 10 Khoa records