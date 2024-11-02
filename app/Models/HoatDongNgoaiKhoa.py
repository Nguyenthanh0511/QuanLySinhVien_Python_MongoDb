class HoatDongNgoaiKhoa:
    def __init__(self, MaHD, TenHD,_id = None):
        self._id = _id
        self.MaHD = MaHD
        self.TenHD = TenHD    
       
    def to_dict(self):
        return {
            "_id": self._id,
            "MaHD": self.MaHD,
            "TenHD": self.TenHD,
        }