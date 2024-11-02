class LopHoc:
    def __init__(self, MaLop, TenLop, SoLuongSinhVien,_id = None):
        self._id = _id
        self.MaLop = MaLop
        self.TenLop = TenLop
        self.SoLuongSinhVien = SoLuongSinhVien
        self.sinh_viens = []
        
    def add_sinh_vien(self, sinh_vien):
        self.sinh_viens.append(sinh_vien)
        
    def remove_sinh_vien(self, sinh_vien):
        self.sinh_viens.remove(sinh_vien)    
       
    def to_dict(self):
        return {
            "_id": self._id,
            "MaLop": self.MaLop,
            "TenLop": self.TenLop,
            "SoLuongSinhVien": self.SoLuongSinhVien,
            "sinh_viens": [sinh_vien.to_dict() for sinh_vien in self.sinh_viens]
        }

# Generate data for 10 classes