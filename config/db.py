import pymongo
import unittest
try:
    client = pymongo.MongoClient("mongodb+srv://hoang:hoang@quanlysinhvien.kjj0s.mongodb.net/")
    db = client["QuanLySinhVien"]
    print("Connection to MongoDB Atlas successful!")
except pymongo.errors.ConnectionFailure as e:
    self.fail(f"Connection failed: {e}")
except Exception as e:
    self.fail(f"Unexpected error: {e}")
# for i in db.sinh_vien.find({}).limit(5):
#     print(i)
