from extensions import db
from datetime import datetime

class Kullanici(db.Model):
    __tablename__ ="kullanicilar"

    id=db.Column(db.Integer,primary_key=True)
    kullanici_adi=db.Column(db.String(50),unique=True,nullable=False)
    email=db.Column(db.String(120),unique=True,nullable=False)
    sifre=db.Column(db.String(200),nullable=False)
    admin_mi=db.Column(db.Boolean,default=False)
    olusturulma_tarihi=db.Column(db.DateTime,default=datetime.utcnow)

    haberler=db.relationship("Haber",backref="yazar",lazy=True)

    def to_dict(self):
        return {
            "id":self.id,
            "kullanici_adi":self.kullanici_adi,
            "email":self.email,
            "admin_mi":self.admin_mi,
            "olusturulma_tarihi":self.olusturulma_tarihi.isoformat(),
            "haberler":[
                {
                    "id":h.id,
                    "baslik":h.baslik,
                    "yayimlanma_tarihi":h.yayimlanma_tarihi.isoformat(),
                    "yayinda_mi":h.yayinda_mi
                }
                for h in self.haberler
            ]
        }

    def __repr__(self):
        return f"<Kullanici{self.kullanici_adi}>"
    

class Kategori(db.Model):
    __tablename__ = "kategoriler"

    id=db.Column(db.Integer,primary_key=True)
    ad=db.Column(db.String(100),unique=True,nullable=False)

    haberler=db.relationship("Haber",backref="kategori",lazy=True)

    def to_dict(self):
        return {
            "id":self.id,
            "ad":self.ad,
            "haberler":[
                {
                    "id":h.id,
                    "baslik":h.baslik,
                    "yayimlanma_tarihi":h.yayimlanma_tarihi.isoformat(),
                    "yayinda_mi":h.yayinda_mi
                } 
                for h in self.haberler
            ]
        }

    def __repr__(self):
        return f"<Kategori {self.ad}>"