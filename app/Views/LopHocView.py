from app.Models.LopHoc import LopHoc
class LopHocView:
    def __init__(self) -> None:
        pass
    
    def ShowLopHoc(self, LopHocList):
        headers = ["MaLop", "TenLop", "SoLuongSinhVien"]
        print("|", end="")
        for header in headers:
            print(f"{header:20}|", end="")
        print()
        
    # Print table separator
        print("|", end="")
        for _ in headers:
            print("-" * 20 + "|", end="")
        print()
        
    # Print lopHoc data
        for i in LopHocList:
            print("|", end="")
            for key in headers:
                print(f"{i.to_dict()[key]:20}|", end="")
            print()
            
    def InputLopHoc(self):
        MaLop = input("Enter MaLop:")
        TenLop = input("Enter TenLop:")
        SoLuongSinhVien = input("Enter SoLuongSinhVien")
        
        LopHocData = {
            "MaLop": MaLop,
            "TenLop": TenLop,
            "SoLuongSinhVien": SoLuongSinhVien,
        }
        lopHoc = LopHoc(**LopHocData).to_dict()
        return lopHoc