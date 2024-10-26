import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys


isimler = []
mailler = []

#Burada içerisinde mail adreslerinin olduğu bir dosya olmalı.
with open("mailler.txt", "r", encoding="utf-8") as file:
    for i in file.readlines():
        i = i.split(",")
        isimler.append(i[0].rstrip("\n"))
        mailler.append(i[1].rstrip("\n"))

mesaj = MIMEMultipart()


mesaj["From"] = "kendi_mailiniz"
mesaj["To"] = ", ".join(mailler)
mesaj["Subject"] = "İsimleriniz..."

ileti = """


Yazılmak istenen ileti...


"""
mesaj_gövdesi = MIMEText(ileti,"plain")
mesaj.attach(mesaj_gövdesi)

try:

    mail = smtplib.SMTP("smtp.gmail.com", 587)
    mail.ehlo()
    mail.starttls()

    mail.login("kendi_mailiniz", "kendi_şifreniz")
    mail.sendmail(mesaj["From"], mesaj["To"], mesaj.as_string())
    print("Mail başarıyla gönderildi!")

    mail.close()

except:
    sys.stderr.write("Bir sorun oluştu")
    sys.stderr.flush()