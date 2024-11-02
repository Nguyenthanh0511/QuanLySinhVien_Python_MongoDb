from app.Models.NganhHoc import NganhHoc
class NganhHocView:
    def __init__(self):
        pass
    
    def ShowNganhHoc(self, NganhHocList):
        headers = ["MaNH", "MoTa", "TenNH", "MaKhoa", "MaSv"]
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
        for i in NganhHocList:
            print("|", end="")
            for key in headers:
                print(f"{i.to_dict()[key]:20}|", end="")
            print()
            
    def InputNganhHoc(self):
        MaNH = input("Enter MaNH:")
        TenNH = input("Enter TenNH:")
        MoTa = input("Enter MaTa")
        MaKhoa = input("Enter MaKhoa:")
        MaSv = input("Enter MaSv")
        
        NganhHocData = {
            "MaNH": MaNH,
            "TenNH": TenNH,
            "MoTa": MoTa,
            "MaKhoa": MaKhoa,
            "MaSv": MaSv,
        }
        nganhHoc = NganhHoc(**NganhHocData).to_dict()
        return nganhHoc
    
    