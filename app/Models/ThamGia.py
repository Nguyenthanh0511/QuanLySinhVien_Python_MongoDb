class ThamGia:
    def __init__(self, MaSv, MaHD, ThoiGian, DiaChi, DiemThuong, GioiHanThamGia,_id = None):
        self._id = _id
        self.MaSv = MaSv
        self.MaHD = MaHD
        self.ThoiGian = ThoiGian
        self.DiaChi = DiaChi
        self.DiemThuong = DiemThuong    
        self.GioiHanThamGia = GioiHanThamGia
    def to_dict(self):
        return {
            "_id": self._id,
            "MaSv": self.MaSv,
            "MaHD": self.MaHD,
            "ThoiGian": self.ThoiGian,
            "DiaChi": self.DiaChi,
            "DiemThuong": self.DiemThuong,
            "GioiHanThamGia": self.GioiHanThamGia,
        }