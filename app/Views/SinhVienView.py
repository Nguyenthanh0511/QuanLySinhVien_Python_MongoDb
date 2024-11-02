import datetime
from app.Models.SinhVien import SinhVien

class SinhVienView:
    def __init__(self):
        pass

    def ShowSinhVien(self, sinhVienLists):
        headers = ["MaSv", "HoTen", "GioiTinh", "NgaySinh", "DiaChi", "Sdt", "MaLop"]
        print("|", end="")
        for header in headers:
            print(f"{header:20}|", end="")
        print()

        # Print table separator
        print("|", end="")
        for _ in headers:
            print("-" * 20 + "|", end="")
        print()

        # Print student data
        for sv in sinhVienLists:
            print("|", end="")
            for key in headers:
                print(f"{sv.to_dict()[key]:20}|", end="")
            print()
    
    def InputSinhVien(self):
        ma_sv = input("Enter MaSv: ")
        ten_sv = input("Enter HoTen: ")
        gioi_tinh = input("Enter GioiTinh: ")
        ngay_sinh = input("Enter NgaySinh (yyyy-mm-dd): ")
        so_dien_thoai = input("Enter Sdt: ")
        dia_chi = input("Enter DiaChi: ")
        ma_lop = input("Enter MaLop: ")

        sinhVienData = {
            "MaSv": ma_sv,
            "HoTen": ten_sv,
            "GioiTinh": gioi_tinh,
            "NgaySinh": ngay_sinh,
            "DiaChi": dia_chi,
            "Sdt": so_dien_thoai,
            "MaLop": ma_lop,
        }
        sinhVien = SinhVien(**sinhVienData).to_dict()
        return sinhVien
    
    def InputSinhVienIdToUpdate(self):
        while True:
            sinhVienId = input("Nhập mã sinh viên cần cập nhật: ")

            # Kiểm tra xem người dùng có nhập giá trị không
            if not sinhVienId:
                print("Bạn chưa nhập mã sinh viên. Vui lòng thử lại.")
                continue

            # Kiểm tra xem mã sinh viên có phải là chuỗi ký tự không
            if not isinstance(sinhVienId, str):
                print("Mã sinh viên phải là một chuỗi ký tự. Vui lòng thử lại.")
                continue

            # Kiểm tra xem mã sinh viên có chỉ chứa các ký tự hợp lệ không (ví dụ: chữ và số)
            if not sinhVienId.isalnum():
                print("Mã sinh viên chỉ được chứa chữ và số. Vui lòng thử lại.")
                continue

            # Nếu vượt qua tất cả các kiểm tra, trả về mã sinh viên
            return sinhVienId
        
    def UpdatedSinhVienData(self, existingSinhVien):
        # Hiển thị thông tin sinh viên hiện tại
        self.ShowSinhVien([existingSinhVien])

        # Nhập thông tin mới
        ten_moi = input("Nhập tên mới (để trống nếu không muốn thay đổi): ")
        ngay_sinh_moi = input("Nhập ngày sinh mới (yyyy-mm-dd) (để trống nếu không muốn thay đổi): ")
        so_dien_thoai_moi = input("Nhập số điện thoại mới (để trống nếu không muốn thay đổi): ")
        dia_chi_moi = input("Nhập địa chỉ mới (để trống nếu không muốn thay đổi): ")
        ma_lop_moi = input("Nhập mã lớp mới (để trống nếu không muốn thay đổi): ")

        # Tạo một đối tượng SinhVien mới với thông tin cập nhật
        updated_sinh_vien = {
            "_id": existingSinhVien["_id"],
            "MaSv": existingSinhVien["MaSv"],
            "HoTen": ten_moi or existingSinhVien["HoTen"],
            "GioiTinh": existingSinhVien["GioiTinh"],  # Không cho phép cập nhật
            "NgaySinh": ngay_sinh_moi or existingSinhVien["NgaySinh"],
            "DiaChi": dia_chi_moi or existingSinhVien["DiaChi"],
            "Sdt": so_dien_thoai_moi or existingSinhVien["Sdt"],
            "MaLop": ma_lop_moi or existingSinhVien["MaLop"],
        }
        return updated_sinh_vien
