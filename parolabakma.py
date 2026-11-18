def parola_istatistikleri(parola: str) -> dict:
    """Bir parolanin detayli istatistiklerini hesaplar (comprehension ile)."""
    return {
        "uzunluk": len(parola),
        "buyuk_harf": len([k for k in parola if k.isupper()]),
        "kucuk_harf": len([k for k in parola if k.islower()]),
        "rakam": len([k for k in parola if k.isdigit()]),
        "ozel_karakter": len([k for k in parola if not k.isalnum()]),
    }

def parola_gucunu_degerlendir(istatistik: dict) -> str:
    """Istatistiklere gore zayif/orta/guclu karari verir."""
    puan = 0
    if istatistik["uzunluk"] >= 8:
        puan += 1
    if istatistik["buyuk_harf"] > 0 and istatistik["kucuk_harf"] > 0:
        puan += 1
    if istatistik["rakam"] > 0:
        puan += 1
    if istatistik["ozel_karakter"] > 0:
        puan += 1

    if puan <= 1:
        return "zayıf"
    elif puan <= 3:
        return "orta"
    else:
        return "güçlü"


try:
    parola = input("Bir deneme parolası girin: ")
    if not parola:
        raise ValueError("Parola boş olamaz")
except ValueError as e:
    print(f"Hata: {e}")
    parola = "varsayilan123"

istatistik = parola_istatistikleri(parola)
karar = parola_gucunu_degerlendir(istatistik)

print("=" * 30)
print("PAROLA GÜÇ RAPORU")
print("=" * 30)
for anahtar, deger in istatistik.items():
    print(f"{anahtar}: {deger}")
print(f"KARAR: {karar.upper()}")