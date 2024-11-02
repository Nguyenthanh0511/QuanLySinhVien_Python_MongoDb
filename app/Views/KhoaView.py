from app.Models.Khoa import Khoa
class KhoaView:
    def __init__(self):
        pass
    
    def ShowKhoa(self, KhoaList):
        headers = ["MaKhoa", "TenKhoa", "DiaChiVPK", "SDTKhoa", "NgayThanhLap"]
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
        for i in KhoaList:
            print("|", end="")
            for key in headers:
                print(f"{i.to_dict()[key]:20}|", end="")
            print()
            
    def InputKhoa(self):
        MaKhoa = input("Enter MaKhoa:")
        TenKhoa = input("Enter TenKhoa:")
        DiaChiVPK = input("Enter DiaChiVPK")
        SDTKhoa = input("Enter SDTKhoa:")
        NgayThanhLap = input("Enter NgayThanhLap")
        
        KhoaData = {
            "MaKhoa": MaKhoa,
            "TenKhoa": TenKhoa,
            "DiaChiVPK": DiaChiVPK,
            "SDTKhoa": SDTKhoa,
            "NgayThanhLap": NgayThanhLap,
        }
        khoa = Khoa(**KhoaData).to_dict()
        return khoa
    
    