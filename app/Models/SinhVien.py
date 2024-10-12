class SinhVien:
    def __init__(self,_id, ma_sv, ten_sv, tuoi, ngay_sinh, so_dien_thoai, dia_chi, ma_lop, create_date, create_by, last_update_date, last_update_by):
        self._id = _id
        self.ma_sv = ma_sv
        self.ten_sv = ten_sv
        self.tuoi = tuoi
        self.ngay_sinh = ngay_sinh
        self.so_dien_thoai = so_dien_thoai
        self.dia_chi = dia_chi
        self.ma_lop = ma_lop
        self.create_date = create_date
        self.create_by = create_by
        self.last_update_date = last_update_date
        self.last_update_by = last_update_by

    def to_dict(self):
        return {
            "_id":str(self._id),
            "ma_sv": self.ma_sv,
            "ten_sv": self.ten_sv,
            "tuoi": self.tuoi,
            "ngay_sinh": self.ngay_sinh,
            "so_dien_thoai": self.so_dien_thoai,
            "dia_chi": self.dia_chi,
            "ma_lop": self.ma_lop,
            "create_date": self.create_date,
            "create_by": self.create_by,
            "last_update_date": self.last_update_date,
            "last_update_by": self.last_update_by
        }
