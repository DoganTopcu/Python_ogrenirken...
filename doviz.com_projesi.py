import requests
from bs4 import BeautifulSoup


url = "https://xn--dviz-5qa.com/"


response = requests.get(url)
html_content = response.content


soup = BeautifulSoup(html_content, "html.parser")


tablo = soup.find("table", {"class": "table table-striped table-sm"})


sıra = tablo.find_all("tr")


kur_listesi = []


for i in sıra[1:]:
    sütunlar = i.find_all("td")


    if len(sütunlar) > 3:
        döviz_adi = sütunlar[1].text.strip().lower()
        aliş = sütunlar[2].text.strip()
        satiş = sütunlar[3].text.strip()


        kur_listesi.append({"Döviz": döviz_adi, "Alış": aliş, "Satış": satiş})


girdi = input("Hangi döviz/altın/borsa bilgisini öğrenmek istersiniz? (örn. dolar, euro, altın, borsa): ").lower()


bilgi_bulundu = False
for i in kur_listesi:
    if girdi in i["Döviz"]:
        print(f"{i['Döviz'].capitalize()} - Alış: {i['Alış']}, Satış: {i['Satış']}")
        bilgi_bulundu = True
        break


if not bilgi_bulundu:
    print("Böyle bir birim bulunmuyor...")