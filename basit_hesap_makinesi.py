print(""" **********
Python Hesap Makinesi

Bir İşlem Seçiniz ya da Çıkmak İçin 'q' ya basınız.
İşlemler:
1. Toplama
2. Çıkarma
3. Bölme
4. Çarpma
5. Üssünü Alma
6. Karekök
7. Logaritma
8. Dereceyi Radyana Çevir
9. Radyanı Dereceye Çevir
10. Sinüsü Bul
11. Cosinüsü Bul
12. Tanjantı Bul
13. Cotanjantı Bul
14. Fakröriyeli Bul
**********""")
import time
import math
while True:
    işlem = input("Yapılacak İşlemi Giriniz:")
    if (işlem == "q"):
        print("İşlem Sonlandırılıyor...")
        time.sleep(1)
        print("Yine Bekleriz...")
        break
    else:
        işlem = int(işlem)

        if (işlem == 1):
            sayı1 = int(input("Sayı giriniz:"))
            sayı2 = int(input("Sayı giriniz:"))
            print("{} + {} = {}".format(sayı1,sayı2,sayı1+sayı2))
        elif (işlem == 2):
            sayı1 = int(input("Sayı giriniz:"))
            sayı2 = int(input("Sayı giriniz:"))
            print("{} - {} = {}".format(sayı1, sayı2, sayı1 - sayı2))
        elif (işlem == 3):
            sayı1 = int(input("Sayı giriniz:"))
            sayı2 = int(input("Sayı giriniz:"))
            print("{} / {} = {}".format(sayı1, sayı2, sayı1 / sayı2))
        elif (işlem == 4):
            sayı1 = int(input("Sayı giriniz:"))
            sayı2 = int(input("Sayı giriniz:"))
            print("{} * {} = {}".format(sayı1, sayı2, sayı1 * sayı2))
        elif (işlem == 5):
            sayı1 = int(input("Sayının tabanını giriniz:"))
            sayı2 = int(input("Üssü giriniz:"))
            print("İşleminiz yapılıyor...")
            time.sleep(1)
            x = math.pow(sayı1,sayı2)
            print("{} üssü {} = {} dir".format(sayı1,sayı2,math.pow(sayı1,sayı2)))
        elif (işlem == 6):
            sayı1 = int(input("Sayı giriniz:"))
            print("İşleminiz yapılıyor...")
            time.sleep(1)
            x = math.sqrt(sayı1)
            print("{} sayısının karekökü {} dir".format(sayı1,math.sqrt(sayı1)))
        elif(işlem == 7):
            sayı1 = int(input(" sayıyı giriniz : "))
            sayı2 = int(input(" logaritmanın tabanını giriniz : "))
            print("işleminiz yapılıyor...")
            time.sleep(1)
            print("{} sayısının {} tabanında logaritması = {} ".format(sayı1,sayı2,math.log(sayı1,sayı2)))

        elif(işlem == 8):
            sayı1 = int(input(" Dereceyi giriniz : "))
            print("işlemniz yapılıyor...")
            time.sleep(1)
            print("{} derece = {} radyandır.".format(sayı1,math.degrees(sayı1)))

        elif(işlem == 9):
            sayı1 = int(input(" radyanı giriniz : "))
            print("işleminiz yapılıyor...")
            time.sleep(1)
            print("{} radyan {} derecedir.".format(sayı1,math.radians(sayı1)))

        elif(işlem == 10):
            a = input( "radyan için = R , derce için = D")
            if(a == "r" or a == "R"):
                sayı1 = int(input(" sayıyı giriniz : "))
                x = math.sin(sayı1)
                print("işleminiz yapılıyor...")
                time.sleep(1)
                print("sin {} = {} ".format(sayı1,x))
            elif(a == "d" or a == "D"):
                sayı1 = int(input(" Dereceyi giriniz : "))
                x = math.sin(sayı1)
                y = math.radians(x)
                print("işleminiz yapılıyor...")
                time.sleep(1)
                print("sin {} = {} ".format(sayı1,y))
        elif (işlem == 11):
            sayı1 = int(input(" dereceyi giriniz : "))
            print("işleminiz yapılıyor...")
            time.sleep(1)
            print("cos {} = {} ".format(sayı1, math.cos(sayı1)))

        elif (işlem == 12):
            sayı1 = int(input(" Dereceyi giriniz : "))
            print("işleminiz yapılıyor...")
            time.sleep(1)
            print("tanjant {} = {} ".format(sayı1, math.tan(sayı1)))

        elif (işlem == 13):
            sayı1 = int(input(" Dereceyi giriniz : "))
            print("işleminiz yapılıyor...")
            time.sleep(1)
            x = math.cos(sayı1) / math.sin(sayı1)
            print("cotanjant {} = {} ".format(sayı1, x))
        elif (işlem == 14):
            sayı1 = int(input("Sayı giriniz:"))
            print("İşleminiz yapılıyor...")
            time.sleep(1)
            print("{} sayısının faktöriyeli {} dir".format(sayı1,math.factorial(sayı1)))
        else:
            print("Geçersiz İşlem. Lütfen yukarıdaki işlemlerden birini seçiniz...")





