# import pymongo
# import random
# from faker import Faker
# from config.db import db
# from app.Models.ThamGia import ThamGia
# from app.Views.ThamGiaView import ThamGiaView

# # Initialize Faker instance
# fake = Faker()

# def GenDataThamGia(num_records):
#     tham_gia_list = []
    
#     for _ in range(num_records):
#         ma_sv = fake.unique.random_int(min=10000, max=99999)  # Random Student ID
#         ma_hd = fake.unique.random_int(min=1000, max=9999)  # Random Activity ID
#         thoi_gian = fake.date_time_between(start_date='-1y', end_date='now')  # Random date within the last year
#         dia_chi = fake.address().replace("\n", ", ")  # Address
#         diem_thuong = round(random.uniform(0, 10), 2)  # Reward points between 0 and 10
#         gioi_han_tham_gia = random.choice([True, False])  # Participation limit

#         tham_gia = {
#             "MaSv": ma_sv,
#             "MaHd": ma_hd,
#             "ThoiGian": thoi_gian.isoformat(),
#             "DiaChi": dia_chi,
#             "DiemThuong": diem_thuong,
#             "GioiHanThamGia": gioi_han_tham_gia
#         }
#         tham_gia_list.append(tham_gia)
#     return tham_gia_list

# def insert_tham_gia_to_mongo(tham_gia_records):
#     try:
#         client = MongoClient("mongodb+srv://hoang:hoang@quanlysinhvien.kjj0s.mongodb.net/")
#         db = client["QuanLySinhVien_Ver2"]
#         collection = db["ThamGia"]
        
#         result = collection.insert_many(tham_gia_records)
#         print(f"Inserted {len(result.inserted_ids)} records into 'tham_gia' collection.")
#     except Exception as e:
#         print(f"An error occurred: {e}")
#     finally:
#         client.close()

# # Generate data and insert it into MongoDB
# tham_gia_data = GenDataThamGia(10)
# insert_tham_gia_to_mongo(tham_gia_data)

# class ThamGiaController:
#     def __init__(self):
#         pass
      
#     def getALL(self):
#         thamGiaDb = db.ThamGia.find()
#         thamGiaLists = [ThamGia(**thamGia) for thamGia in thamGiaDb]
#         HoatDongNgoaiKhoaView().ShowKhoa(hoatDongNgoaiKhoaLists)
        
#     def CreateHoatDongNgoaiKhoa(self):
#         try:
#             hoatDongNgoaiKhoa = HoatDongNgoaiKhoaView().InputHoatDongNgoaiKhoa()
#             hoatDongNgoaiKhoaInsert = db.HoatDongNgoaiKhoa.insert_one(hoatDongNgoaiKhoa)
#             if hoatDongNgoaiKhoaInsert.acknowledged:
#                 print("Hoat dong ngoai khoa created successfully!")
#             else:
#                 print("Error creating Hoat dong ngoai khoa.")
#             return hoatDongNgoaiKhoaInsert
#         except Exception as e:
#             print(e)