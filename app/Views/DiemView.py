from app.Models.BangDiem import BangDiem
class BangDiemView:
    def __init__(self):
        pass
    
    def ShowBangDiem(self, BangDiemList):
        headers = ["MaBangDiem", "DiemKT_1", "DiemKT_2", "DiemGiuaKy", "DiemCuoiKy", "MaSv", "MaMonHoc"]
        print("|", end="")
        for header in headers:
            print(f"{header:20}|", end="")
        print()
        
    # Print table separator
        print("|", end="")
        for _ in headers:
            print("-" * 20 + "|", end="")
        print()
        
    # Print NganhHoc data
        for i in BangDiemList:
            print("|", end="")
            for key in headers:
                print(f"{i.to_dict()[key]:20}|", end="")
            print()
            
    def InputBangDiem(self):
        MaBangDiem = input("Enter MaBangDiem:")
        DiemKT_1 = input("Enter DiemKT_1:")
        DiemKT_2 = input("Enter DiemKT_2")
        DiemGiuaKy = input("Enter DiemGiuaKy")
        DiemCuoiKy = input("Enter DiemCuoiKy")
        MaSv = input("Enter MaSv")
        MaMonHoc = input("Enter MaMonHoc")
        
        BangDiemData = {
            "MaBangDiem": MaBangDiem,
            "DiemKT_1": DiemKT_1,
            "DiemKT_2": DiemKT_2,
            "DiemGiuaKy": DiemGiuaKy,
            "DiemCuoiKy": DiemCuoiKy,
            "MaSv": MaSv,
            "MaMonHoc": MaMonHoc,
        }
        bangDiem = BangDiem(**BangDiemData).to_dict()
        return bangDiem
    
    