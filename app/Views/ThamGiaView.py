# from app.Models.ThamGia import ThamGia
# from app.Models.Nghanh import ThamGia
# class ThamGiaView:
#     def __init__(self):
#         pass
    
#     def ShowNganhHoc(self, NganhHocList):
#         headers = ["MaNH", "TenNganhHoc", "MoTa"]
#         print("|", end="")
#         for header in headers:
#             print(f"{header:20}|", end="")
#         print()
        
#     # Print table separator
#         print("|", end="")
#         for _ in headers:
#             print("-" * 20 + "|", end="")
#         print()
        
#     # Print NganhHoc data
#         for i in NganhHocList:
#             print("|", end="")
#             for key in headers:
#                 print(f"{i.to_dict()[key]:20}|", end="")
#             print()
            
#     def InputNganhHoc(self):
#         MaNH = input("Enter MaNH:")
#         TenNganhHoc = input("Enter TenNganhHoc:")
#         MoTa = input("Enter MaTa")
        
#         NganhHocData = {
#             "MaNH": MaNH,
#             "TenNganhHoc": TenNganhHoc,
#             "MoTa": MoTa,
#         }
#         nganhHoc = NganhHoc(**NganhHocData).to_dict()
#         return nganhHoc
    
    