from app.Models.HoatDongNgoaiKhoa import HoatDongNgoaiKhoa
class HoatDongNgaoiKhoaView:
    def __init__(self):
        pass
    
    def ShowHoatDongNgoaiKhoa(self, hoatDongNgoaiKhoaList):
        headers = ["MaHD", "TenHD"]
        print("|", end="")
        for header in headers:
            print(f"{header:20}|", end="")
        print()
        
    # Print table separator
        print("|", end="")
        for _ in headers:
            print("-" * 20 + "|", end="")
        print()
        
    # Print Khoa data
        for i in hoatDongNgoaiKhoaList:
            print("|", end="")
            for key in headers:
                print(f"{i.to_dict()[key]:20}|", end="")
            print()
            
    def InputHoatDongNgoaiKhoa(self):
        MaHD = input("Enter MaHD:")
        TenHD = input("Enter TenHD:")
        
        HoatDongNgoaiKhoaData = {
            "MaHD": MaHD,
            "TenHD": TenHD,
        }
        hoatDongNgoaiKhoa = HoatDongNgoaiKhoa(**HoatDongNgoaiKhoaData).to_dict()
        return hoatDongNgoaiKhoa
    
    