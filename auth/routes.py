from flask import Blueprint, request, jsonify
from auth.services import kullanici_kayit,kullanici_giris
from auth.validators import gerekli_alan_kontrol

auth_bp=Blueprint("auth",__name__)

@auth_bp.route("/kayit",methods=["POST"])
def kayit():
    veri=request.get_json()

    hata=gerekli_alan_kontrol(veri,["kullanici_adi","email","sifre"])
    if hata:
        return jsonify({"hata":hata}),400

    response,status=kullanici_kayit(veri)
    return jsonify(response),status


@auth_bp.route("/giris",methods=["POST"])
def giris():
    veri=request.get_json()

    hata=gerekli_alan_kontrol(veri,["email","sifre"])
    if hata:
        return jsonify({"hata":hata}),400

    response,status=kullanici_giris(veri)
    return jsonify(response),status