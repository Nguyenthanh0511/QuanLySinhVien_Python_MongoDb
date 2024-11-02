class Khoa:
    def __init__(self, MaKhoa, TenKhoa, DiaChiVPK, SDTKhoa, NgayThanhLap, _id = None):
        self._id = _id
        self.MaKhoa = MaKhoa
        self.TenKhoa = TenKhoa
        self.DiaChiVPK = DiaChiVPK
        self.SDTKhoa = SDTKhoa
        self.NgayThanhLap = NgayThanhLap    
       
    def to_dict(self):
        return {
            "_id": self._id,
            "MaKhoa": self.MaKhoa,
            "TenKhoa": self.TenKhoa,
            "DiaChiVPK": self.DiaChiVPK,
            "SDTKhoa": self.SDTKhoa,
            "NgayThanhLap": self.NgayThanhLap,
        }