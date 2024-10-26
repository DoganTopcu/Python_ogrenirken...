import sqlite3
import time




class Şarkı():
    def __init__(self,isim,sanatçı,albüm,prodüksiyon,süre):
        self.isim = isim
        self.sanatçı = sanatçı
        self.albüm = albüm
        self.prodüksiyon = prodüksiyon
        self.süre = süre
    def __str__(self):
        return "Şarkı ismi: {}\nSanatçı: {}\nAlbüm: {}\nProdüksiyon Şirketi: {}\nŞarkı süresi: {}\n".format(self.isim,self.sanatçı,self.albüm,self.prodüksiyon,self.süre)


class Şarkılar():
    def __init__(self):
        self.bağlantı_oluştur()

    def bağlantı_oluştur(self):
        self.bağlantı = sqlite3.connect("şarkılar.db")
        self.cursor = self.bağlantı.cursor()

        sorgu = "Create table if not exists şarkılar (İsim TEXT,Sanatçı TEXT,Albüm TEXT, Prodüksiyon TEXT,Süre İNT)"
        self.cursor.execute(sorgu)
        self.bağlantı.commit()

    def bağlantı_kes(self):
        self.bağlantı.close()

    def şarkı_ekle(self,şarkı):
        sorgu = "insert into şarkılar values(?,?,?,?,?)"
        self.cursor.execute(sorgu,(şarkı.isim,şarkı.sanatçı,şarkı.albüm,şarkı.prodüksiyon,şarkı.süre))
        self.bağlantı.commit()

    def şarkı_sil(self,isim):
        sorgu = "Delete from şarkılar where İsim = ?"
        self.cursor.execute(sorgu,(isim,))
        self.bağlantı.commit()

    def toplam_süre(self):
        sorgu = "select süre from şarkılar"
        self.cursor.execute(sorgu)
        süreler = self.cursor.fetchall()

        if (len(süreler) == 0):
            print("Listede şarkı bulunmuyor...")
        else:

            toplam_süre = sum([süre[0] for süre in süreler])

            dakika = toplam_süre // 60
            saniye = toplam_süre % 60

        print("Listedeki şarkıların toplam süresi: {} dakika {} saniyedir.".format(dakika,saniye))

    def şarkı_sorgula(self, isim):
        sorgu = "SELECT * FROM şarkılar WHERE İsim = ?"
        self.cursor.execute(sorgu, (isim,))
        şarkılar = self.cursor.fetchall()

        if len(şarkılar) == 0:
            print("Böyle bir şarkı bulunmuyor...")
        else:
            şarkı = Şarkı(şarkılar[0][0], şarkılar[0][1], şarkılar[0][2], şarkılar[0][3], şarkılar[0][4])
            print(şarkı)

    def şarkıları_göster(self):
        sorgu = "select * from şarkılar"
        self.cursor.execute(sorgu)
        şarkılar = self.cursor.fetchall()

        if (len(şarkılar) == 0):
            print("Listede şarkı bulunmuyor...")
        else:
            for i in şarkılar:
                şarkı = Şarkı(i[0],i[1],i[2],i[3],i[4])
                print(şarkı)


