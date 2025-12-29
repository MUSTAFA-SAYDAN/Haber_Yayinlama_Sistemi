def gerekli_alan_kontrol(data,gerekli_alanlar):
    if not data:
        return "Veri gönderilmedi"

    for alan in gerekli_alanlar:
        if alan not in data or not str(data[alan]).strip():
            return f"{alan} alanı zorunludur"

    return None
