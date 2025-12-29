from flask import current_app
from extensions import db,bcrypt
from models import Kullanici
import jwt
import datetime

def kullanici_kayit(data):
    kullanici_adi=data.get("kullanici_adi")
    email=data.get("email")
    sifre=data.get("sifre")

    if Kullanici.query.filter_by(kullanici_adi=kullanici_adi).first():
        return {"hata":"Bu kullanıcı adı zaten kullanılıyor"},400
    
    if Kullanici.query.filter_by(email=email).first():
        return {"hata": "Bu email zaten kayitli"},400

    sifre_hash=bcrypt.generate_password_hash(sifre).decode("utf-8")

    yeni_kullanici = Kullanici(
        kullanici_adi=kullanici_adi,
        email=email,
        sifre=sifre_hash
    )

    db.session.add(yeni_kullanici)
    db.session.commit()

    return{"mesaj":"Kullanici başarıyla kaydedildi"},201

