import random
import pymongo
from faker import Faker
from config.db import db
from app.Models.SinhVien import SinhVien
from app.Views.SinhVienView import SinhVienView
from datetime import datetime
# Tạo một đối tượng Faker để tạo dữ liệu giả

    
# for _ in range(10):  # Sinh 10 bản ghi
#     sinh_vien_id = GenDataSinhVien()
#     print(f"Sinh viên đã được thêm với ID: {sinh_vien_id}")
    
#Hiển thị thông tin
class SinhVienController:
    def __init__(self):
        pass
    
    def GetAll(self):
        sinhVienDb = db.SinhVien.find()
        sinhVienLists = [SinhVien(**sinhVien) for sinhVien in sinhVienDb]
        SinhVienView().ShowSinhVien(sinhVienLists)
        
    def CreateSinhVien(self):
        try:
            sinhVien = SinhVienView().InputSinhVien()
            sinhVienInsert = db.SinhVien.insert_one(sinhVien)
            if sinhVienInsert.acknowledged:
                print("Sinh vien created successfully!")
            else:
                print("Error creating sinh vien.")
            return sinhVienInsert
        except Exception as e:
            print(e)
            
    # def GenDataSinhVien(self):
    #     # Kết nối đến MongoDB
    #     client = pymongo.MongoClient("mongodb+srv://hoang:hoang@quanlysinhvien.kjj0s.mongodb.net/")
    #     db = client["QuanLySinhVien_Ver2"]
    #     collection = db["SinhVien"]
    #     fake = Faker()

    #     while True:
    #         ma_sv = f"SV{random.randint(1000, 9999)}"  # Tạo mã sinh viên ngẫu nhiên
            
    #         # Kiểm tra xem MaSV có đã tồn tại trong CSDL chưa
    #         if collection.find_one({"MaSV": ma_sv}) is None:
    #             # Sinh thông tin sinh viên mới nếu mã chưa tồn tại
    #             ngay_sinh = fake.date_between(start_date="-18y", end_date="today")
            
    #             # Đảm bảo ngay_sinh là một đối tượng datetime.date
    #             if isinstance(ngay_sinh, date):
    #                 ngay_sinh = datetime.combine(ngay_sinh, datetime.min.time())
                
    #                 sinh_vien = {
    #                     "MaSV": ma_sv,
    #                     "HoTen": fake.name(),
    #                     "GioiTinh": random.choice(["Nam", "Nữ"]),
    #                     "NgaySinh": ngay_sinh,  # Đã chuyển sang datetime.datetime
    #                     "DiaChi": fake.address(),
    #                     "Sdt": fake.phone_number(),
    #                     "MaLop": f"LOP{random.randint(10, 99)}"
    #                 }
    #             # Chèn dữ liệu vào MongoDB và trả về ID đã chèn
    #             result = collection.insert_one(sinh_vien)
    #             return result.inserted_id
    #         else:
    #             # Nếu MaSV bị trùng, tiếp tục vòng lặp để tạo mã mới
    #             continue
    
    def UpdateSinhVien(self):
        try:
            # Get the ID of the SinhVien to update
            sinhVienId = SinhVienView().InputSinhVienIdToUpdate()

            # Find the existing SinhVien document by ID
            existingSinhVien = db.SinhVien.find_one({"_id": sinhVienId})

            if existingSinhVien:
                # Get the updated SinhVien data from the user
                updatedSinhVien = SinhVienView().UpdatedSinhVienData(existingSinhVien)

                # Update the existing SinhVien document with the updated data
                result = db.sinh_vien.update_one({"_id": sinhVienId}, {"$set": updatedSinhVien})

                if result.modified_count == 1:
                    print("Sinh vien updated successfully!")
                else:
                    print("Error updating sinh vien.")
            else:
                print("Sinh vien not found.")
        except Exception as e:
            print(e)
            
    def DeleteSinhVien(self):
        try:
            # Get the ID of the SinhVien to delete
            sinhVienId = SinhVienView().InputSinhVienIdToUpdate()

            # Delete the SinhVien document by ID
            result = db.sinh_vien.delete_one({"_id": sinhVienId})

            if result.deleted_count == 1:
                print("Sinh viên đã được xóa thành công!")
            else:
                print("Không tìm thấy sinh viên để xóa.")
        except Exception as e:
            print("Lỗi khi xóa sinh viên:", str(e))