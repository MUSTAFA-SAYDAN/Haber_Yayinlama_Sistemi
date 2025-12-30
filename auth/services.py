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

    yeni_kullanici=Kullanici(
        kullanici_adi=kullanici_adi,
        email=email,
        sifre=sifre_hash
    )

    db.session.add(yeni_kullanici)
    db.session.commit()

    return{"mesaj":"Kullanici başarıyla kaydedildi"},201


def kullanici_giris(data):
    email=data.get("email")
    sifre=data.get("sifre")

    kullanici=Kullanici.query.filter_by(email=email).first()
    if not kullanici:
        return {"hata":"Email veya sifre hatalı"},401

    if not bcrypt.check_password_hash(kullanici.sifre,sifre):
        return {"hata":"Email veya sifre hatalı"},401

    payload = {
        "kullanici_id":kullanici.id,
        "admin_mi":kullanici.admin_mi,
        "exp":datetime.datetime.utcnow() + datetime.timedelta(hours=3)
    }

    token=jwt.encode(
        payload,
        current_app.config["SECRET_KEY"],
        algorithm="HS256"
    )

    return {"token":token},200

