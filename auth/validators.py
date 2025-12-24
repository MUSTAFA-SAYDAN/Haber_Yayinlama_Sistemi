def gerekli_alan_kontrol(veri,gerekli_alanlar):
    if not veri:
        return "Veri gonderilmedi"

    for alan in gerekli_alanlar:
        if alan not in veri or not str(veri[alan]).strip():
            return f"{alan} alani zorunludur"

    return None
