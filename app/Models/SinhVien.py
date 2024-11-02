class SinhVien:
    def __init__(self, MaSv, HoTen, GioiTinh, NgaySinh, DiaChi, Sdt, MaLop,MaNH, DiemRenLuyen, _id=None):
        self._id = _id
        self.MaSv = MaSv
        self.HoTen = HoTen
        self.GioiTinh = GioiTinh
        self.NgaySinh = NgaySinh
        self.DiaChi = DiaChi
        self.Sdt = Sdt
        self.MaLop = MaLop
        self.Lop_hoc = None
        self.MaNH = MaNH
        self.DiemRenLuyen = DiemRenLuyen
        # self.lop_hocs = []
        
    
    # def add_nganh_hoc(self, nganh_hoc):
    #     self.nganh_hocs.append(nganh_hoc)

    # def remove_nganh_hoc(self, nganh_hoc):
    #     self.nganh_hocs.remove(nganh_hoc)
        
    # def add_lop_hoc(self, lop_hoc):
    #     self.lop_hocs.append(lop_hoc)
        
    # def remove_lop_hoc(self, lop_hoc):
    #     self.lop_hocs.remove(lop_hoc)

    def to_dict(self):
        return {
            "_id": self._id,
            "MaSv": self.MaSv,
            "HoTen": self.HoTen,
            "GioiTinh": self.GioiTinh,
            "NgaySinh": self.NgaySinh,
            "DiaChi": self.DiaChi,
            "Sdt": self.Sdt,
            "MaLop": self.MaLop,
            # "nganh_hocs": [nganh_hoc.to_dict() for nganh_hoc in self.nganh_hocs],
            # "lop_hocs": [lop_hoc.to_dict() for lop_hoc in self.lop_hocs]
            "MaNH": self.MaNH,
            "DiemRenLuyen": self.DiemRenLuyen,
        }
