import şarkı_projesi

import time



print("""
***************************************

Şarkı Kütüphanesine Hoşgeldiniz...

Yapmak istediğiniz işlemi aşşağıdan seçebilir ya da çıkmak için 'q' ya basabilirsiniz...

İşlemler:

1. Şarkıları Gör
2. Şarkı Sorgula
3. Şarkı Ekle
4. Şarkı Sil
5. Toplam Süreyi Gör

***************************************
""")

şarkılar = şarkı_projesi.Şarkılar()


while True:
    işlem = input("Yapacağınız işlemi giriniz:")

    if (işlem == "q"):
        print("Program sonlandırılıyor...")
        time.sleep(1)
        print("Program sonlandırıldı, yine bekleriz...")
        break
    elif (işlem == "1"):
        şarkılar.şarkıları_göster()
    elif (işlem == "2"):
        isim = input("Şarkının ismini giriniz:")
        print("Kontrol ediliyor...")
        time.sleep(1)
        şarkılar.şarkı_sorgula(isim)
    elif (işlem == "3"):
        isim = input("Eklemek istediğiniz şarkı ismi:")
        sanatçı = input("Eklemek istediğiniz sanatçı:")
        albüm = input("Eklemek istediğiniz albüm:")
        prodüksiyon = input("Eklemek istediğiniz prodüksiyon:")
        süre = input("Eklemek istediğiniz süre:")
        yeni_şarkı = şarkı_projesi.Şarkı(isim, sanatçı, albüm, prodüksiyon, süre)
        print("Şarkı ekleniyor...")
        time.sleep(1)
        şarkılar.şarkı_ekle(yeni_şarkı)
        print("Şarkı eklenmiştir.\nYeni şarkı listesi aşşağıdaki gibidir.")
        şarkılar.şarkıları_göster()
    elif (işlem == "4"):
        isim = input("Silmek istediğiniz şarkının ismini giriniz:")
        cevap = input("{} şarkısı silinsin mi? (E/H):".format(isim))

        if (cevap == "E"):
            print("Şarkı siliniyor...")
            time.sleep(1)
            şarkılar.şarkı_sil(isim)
            print("{} şarkısı listeden silinmiştir...".format(isim))
        elif (cevap == "H"):
            print("Silme işlemi iptal edildi...")
        else:
            print("Geçersiz giriş yaptınız.")

    elif (işlem == "5"):
        print("Toplam süre hesaplanıyor...")
        time.sleep(2)
        şarkılar.toplam_süre()