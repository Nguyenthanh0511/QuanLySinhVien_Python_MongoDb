class BangDiem:
    def __init__(self, MaBangDiem, DiemKT_1, DiemKT_2, DiemGiuaKy, DiemCuoiKy, MaSv, MaMonHoc,_id = None):
        self._id = _id
        self.MaBangDiem = MaBangDiem
        self.DiemKT_1 = DiemKT_1
        self.DiemKT_2 = DiemKT_2
        self.DiemGiuaKy = DiemGiuaKy
        self.DiemCuoiKy = DiemCuoiKy
        self.MaSv = MaSv
        self.MaMonHoc = MaMonHoc
        
    def to_dict(self):
        return {
            "_id": self._id,
            "MaBangDiem": self.MaBangDiem,
            "DiemKT_1": self.DiemKT_1,
            "DiemKT_2": self.DiemKT_2,
            "DiemGiuaKy": self.DiemGiuaKy,
            "DiemCuoiKy": self.DiemCuoiKy,
            "MaSv": self.MaSv,
            "MaMonHoc": self.MaMonHoc
        }
        