class NganhHoc:
    def __init__(self, MaNH, TenNH, MoTa, MaKhoa, MaSv, _id =None):
        self._id = _id,
        self.MaNH = MaNH,
        self.TenNH = TenNH,
        self.MoTa = MoTa,
        self.MaKhoa = MaKhoa,
        self.MaSv = MaSv,
        
    def to_dict(self):
        return {
            "_id": self._id,
            "MaNH": self.MaNH,
            "TenNH": self.TenNH,
            "MoTa": self.MoTa,
            "MaKhoa": self.MaKhoa,
            "MaSv": self.MaSv,
        }