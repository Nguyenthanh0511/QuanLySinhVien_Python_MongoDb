import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pymongo

class VisualizeTablesController:
    def __init__(self):
        # Kết nối MongoDB
        self.client = pymongo.MongoClient("mongodb+srv://hoang:hoang@quanlysinhvien.kjj0s.mongodb.net/")
        self.db = self.client["QuanLySinhVien_Ver2"]
        # Bộ sưu tập
        self.khoa_collection = self.db["Khoa"]
        self.hocbong_collection = self.db["HocBong"]
        self.sinhvien_collection = self.db["SinhVien"]
        self.thamgia_collection = self.db["ThamGia"]
        self.bangdiem_collection = self.db["BangDiem"]
        self.lophoc_collection = self.db["LopHoc"]
        self.nghanh_hoc = self.db["NganhHoc"]

    # 1. Thống kê số lượng sinh viên trong từng khoa và trực quan hóa
     # 1. Thống kê số lượng sinh viên theo khoa
    def visualize_students_per_department(self):
        result = self.nghanh_hoc.aggregate([
            {
                "$lookup": {
                    "from": "Khoa", 
                    "localField": "MaKhoa", 
                    "foreignField": "MaKhoa", 
                    "as": "Khoa"
                }
            },
            {"$unwind": "$Khoa"},
            {
                "$group": {
                    "_id": "$Khoa.TenKhoa", 
                    "MaSv": {"$sum": 1}
                }
            }
        ])
        # print(result.)
        data = pd.DataFrame(list(result))  # Chuyển đổi kết quả thành danh sách trước

        if data.empty:
            print("No data returned from aggregation. Please check your collections and data.")
            return

        data.rename(columns={'_id': 'TenKhoa'}, inplace=True)
        print(data)  # In ra để kiểm tra dữ liệu
            
        # # Visualize
        # plt.figure(figsize=(10, 6))
        # sns.barplot(data=data, x='TenKhoa', y='SoLuongSinhVien')
        # plt.title("Số lượng sinh viên theo khoa")
        # plt.xlabel("Tên Khoa")
        # plt.ylabel("Số lượng sinh viên")
        # plt.xticks(rotation=45)
        # plt.show()

    # 2. Tổng số học bổng và giá trị học bổng trung bình - trực quan hóa
    def visualize_scholarship_summary(self):
        
        total_scholarships = self.hocbong_collection.count_documents({})
        avg_scholarship_amount = self.hocbong_collection.aggregate([
            {"$group": {"_id": None, "Average": {"$avg": "$TienThuong"}}}
        ])
        avg_amount = list(avg_scholarship_amount)[0]['Average']
        plt.figure(figsize=(6, 4))
        sns.barplot(x=['Tổng học bổng', 'Giá trị TB học bổng'], y=[total_scholarships, avg_amount])
        plt.title("Tổng số học bổng và giá trị học bổng trung bình")
        plt.ylabel("Giá trị")
        plt.show()

    # 3. Thống kê số sinh viên tham gia hoạt động ngoại khóa và trực quan hóa
    def visualize_extracurricular_activity_participation(self):
        total_students = self.thamgia_collection.distinct("MaSv")
        total_activities = self.thamgia_collection.distinct("MaHd")
        plt.figure(figsize=(6, 4))
        sns.barplot(x=['Số sinh viên', 'Số hoạt động'], y=[len(total_students), len(total_activities)])
        plt.title("Số sinh viên và số hoạt động ngoại khóa")
        plt.ylabel("Số lượng")
        plt.show()

    # 4. Điểm trung bình các môn học của từng sinh viên - trực quan hóa
    def visualize_average_score_per_student(self):
        scores = self.bangdiem_collection.aggregate([
            {"$project": {"MaSv": 1, "DiemTrungBinh": {"$avg": ["$DiemKT_1", "$DiemKT_2", "$DiemGiuaKy", "$DiemCuoiKy"]}}},
            {"$group": {"_id": "$MaSv", "DiemTB": {"$avg": "$DiemTrungBinh"}}}
        ])
        data = pd.DataFrame(scores)
        plt.figure(figsize=(10, 6))
        sns.histplot(data=data, x='DiemTB', bins=20, kde=True)
        plt.title("Điểm trung bình của từng sinh viên")
        plt.xlabel("Điểm trung bình")
        plt.ylabel("Số lượng sinh viên")
        plt.show()

    # 5. Số lượng sinh viên trong mỗi lớp - trực quan hóa
    def visualize_student_count_per_class(self):
        class_stats = self.lophoc_collection.aggregate([
            {"$lookup": {"from": "SinhVien", "localField": "MaLop", "foreignField": "MaLop", "as": "SinhVien"}},
            {"$project": {"TenLop": 1, "SoLuongSinhVien": {"$size": "$SinhVien"}}}
        ])
        data = pd.DataFrame(class_stats)
        plt.figure(figsize=(10, 6))
        sns.barplot(data=data, x='TenLop', y='SoLuongSinhVien')
        plt.title("Số lượng sinh viên trong mỗi lớp")
        plt.xlabel("Tên Lớp")
        plt.ylabel("Số lượng sinh viên")
        plt.xticks(rotation=45)
        plt.show()

# Khởi tạo đối tượng và gọi các hàm trực quan hóa
visualize = VisualizeTablesController()
visualize.visualize_students_per_department()
# visualize.visualize_scholarship_summary()
# visualize.visualize_extracurricular_activity_participation()
# visualize.visualize_average_score_per_student()
# visualize.visualize_student_count_per_class()
