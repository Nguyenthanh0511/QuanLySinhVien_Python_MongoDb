class MonHoc:
    def __init__(self, MaMonHoc, TenMonHoc, SoTin, MaKhoa, _id =None):
        self._id = _id
        self.MaMonHoc = MaMonHoc
        self.TenMonHoc = TenMonHoc
        self.SoTin = SoTin
        self.MaKhoa = MaKhoa
        self.sinh_viens = []
        
    def add_sinh_vien(self, sinh_vien):
        self.sinh_viens.append(sinh_vien)
        
    def remove_sinh_vien(self, sinh_vien):
        self.sinh_viens.remove(sinh_vien)
        
    def to_dict(self):
        return {
            "_id": self._id,
            "MaMonHoc": self.MaMonHoc,
            "TenMonHoc": self.TenMonHoc,
            "SoTin": self.SoTin,
            "MaKhoa": self.MaKhoa,
            "sinh_viens": [sv.to_dict() for sv in self.sinh_viens]
        }