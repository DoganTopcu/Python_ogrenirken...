import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QPushButton, QDoubleSpinBox, QLineEdit, QLabel, QVBoxLayout, QHBoxLayout, QApplication
import requests

class Pencere(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.temizle = QPushButton("Temizle")
        self.dönüstür = QPushButton("Dönüştür")
        self.çıkış = QPushButton("Çıkış")
        self.miktar = QDoubleSpinBox()
        self.döviz1 = QLineEdit()
        self.döviz2 = QLineEdit()
        self.sonuç = QLabel("Sonuç")

        v_box = QVBoxLayout()

        üst_kutu = QHBoxLayout()
        üst_kutu.addWidget(self.miktar)
        üst_kutu.addWidget(self.döviz1)
        üst_kutu.addWidget(self.döviz2)

        v_box.addLayout(üst_kutu)

        v_box.addWidget(self.sonuç)

        buton_kutu = QHBoxLayout()
        buton_kutu.addWidget(self.temizle)
        buton_kutu.addWidget(self.dönüstür)
        buton_kutu.addWidget(self.çıkış)

        v_box.addLayout(buton_kutu)

        self.setLayout(v_box)

        self.temizle.clicked.connect(self.sil)
        self.çıkış.clicked.connect(self.Cikis)
        self.dönüstür.clicked.connect(self.Donustur)

        self.setWindowTitle("Döviz Çevirici")
        self.show()

    def sil(self):
        self.döviz1.clear()
        self.döviz2.clear()
        self.miktar.setValue(0)
        self.sonuç.setText("Sonuç")

    def Cikis(self):
        app.quit()

    def Donustur(self):
        api_key = "Kendi_API_Key'iniz..."
        url = "https://data.fixer.io/api/latest"

        params = {
            'access_key': api_key,
            'symbols': f'{self.döviz1.text()},{self.döviz2.text()}'
        }

        response = requests.get(url, params=params)
        json_verisi = response.json()

        try:
            rate1 = json_verisi["rates"][self.döviz1.text()]
            rate2 = json_verisi["rates"][self.döviz2.text()]
            miktar = self.miktar.value()
            sonuc = miktar * (rate2 / rate1)
            self.sonuç.setText(f"Sonuç: {sonuc:.2f}")
        except KeyError:
            self.sonuç.setText("Lütfen para birimlerini doğru girin.")
        except Exception as e:
            self.sonuç.setText("Dönüşüm hatası!")

app = QApplication(sys.argv)
pencere = Pencere()
sys.exit(app.exec())