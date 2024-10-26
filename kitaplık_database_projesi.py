from kütüphane import *

print("""****************************************
Kütüphane Programımıza Hoşgeldiniz.

İşlemler:

1. Kitapları Göster
2. Kitap Sorgula
3. Kitap Ekle
4. Kitap Sil
5. Baskı Yükselt
6. Kitap Bilgilerini Güncelle

Çıkmak için 'q' ya basın.
****************************************""")


kütüphane = Kütüphane()


while True:
    işlem = input("Yapacağınız işlemi giriniz:")

    if (işlem == "q"):
        print("Program sonlandırılıyor...")
        print("Yine bekleriz...")
        break
    elif (işlem == "1"):
        kütüphane.kitapları_göster()

    elif (işlem == "2"):
        isim = input("Hangi kitabı istiyorsunuz?:")
        print("Kitap sorgulanıyor...")
        time.sleep(2)

        kütüphane.kitap_sorgula(isim)
    elif (işlem == "3"):
        isim = input("İsim:")
        yazar = input("Yazar:")
        yayınevi = input("yayınevi:")
        tür = input("Tür:")
        baskı = input("Baskı:")
        yeni_kitap = Kitap(isim,yazar,yayınevi,tür,baskı)
        print("Kitap ekleniyor...")
        time.sleep(2)
        kütüphane.kitap_ekle(yeni_kitap)
        print("Kitap eklendi...")
    elif (işlem == "4"):
        isim = input("Hangi kitabı silmek istiyorsunz?:")
        cevap = input("Emin misiniz? (E/H)")
        if (cevap == "E"):
            print("Kitap siiniyor...")
            time.sleep(1)
            kütüphane.kitap_sil(isim)
            print("Kitap silindi.")
    elif (işlem == "5"):
        isim = input("Hangi kitabın bskısını yükseltmek istiyorsunuz?:")
        print("Baskı yükseltiliyor...")
        time.sleep(1)
        kütüphane.baskı_yükselt(isim)
        print("Baskı yükseltildi.")
    elif (işlem == "6"):
        isim = input("Güncellemek istediğiniz kitabın ismini giriniz: ")

        sorgu = "SELECT * FROM kitaplar WHERE isim = ?"
        kütüphane.cursor.execute(sorgu, (isim,))
        kitaplar = kütüphane.cursor.fetchall()

        if len(kitaplar) == 0:
            print("Böyle bir kitap bulunmuyor...")
        else:
            mevcut_yazar, mevcut_yayınevi, mevcut_tür, mevcut_baskı = kitaplar[0][1], kitaplar[0][2], kitaplar[0][3], \
            kitaplar[0][4]

            yeni_yazar = input("Yeni yazar:")
            yeni_yayınevi = input("Yeni yayınevi:")
            yeni_tür = input("Yeni tür:")
            yeni_baskı = input("Yeni baskı:")

            yeni_baskı = int(yeni_baskı)

            kütüphane.kitap_güncelle(isim, yeni_yazar, yeni_yayınevi, yeni_tür, yeni_baskı)
            print(f"'{isim}' kitabı güncellendi.")


