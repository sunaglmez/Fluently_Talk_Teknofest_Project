import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QMessageBox
import subprocess

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Fluently Talk')
        self.setGeometry(500, 500, 350, 600)
        self.setStyleSheet("background-color: lightblue;")

        layout = QVBoxLayout()

        button1 = QPushButton('DAF', self)
        button1.setStyleSheet("background-color: plum;")
        button1.clicked.connect(self.on_button1_clicked)
        layout.addWidget(button1)

        button2 = QPushButton('Metronom', self)
        button2.setStyleSheet("background-color: lightgrey;")
        button2.clicked.connect(self.on_button2_clicked)
        layout.addWidget(button2)

        self.setLayout(layout)

    def on_button1_clicked(self):
        # Burada subprocess kullanarak başka bir Python dosyasını çalıştırıyoruz
        try:
            subprocess.run(["python3", r"C:\Users\gulus\OneDrive - st.biruni.edu.tr\Masaüstü\daf-generator-master\daf-generator-master\dafgen.py"])
        except FileNotFoundError:
            QMessageBox.critical(self, 'Error', 'dag.py dosyası bulunamadı.')
        except Exception as e:
            QMessageBox.critical(self, 'Error', f'Hata oluştu: {str(e)}')

    def on_button2_clicked(self):
        QMessageBox.information(self, 'Metronom', 'Seçenek 2 seçildi.')

import sys
import subprocess
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QMessageBox

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Fluently Talk')
        self.setGeometry(500, 500, 350, 600)
        self.setStyleSheet("background-color: lightblue;")

        layout = QVBoxLayout()

        button1 = QPushButton('DAF', self)
        button1.setStyleSheet("background-color: plum;")
        button1.clicked.connect(self.on_button1_clicked)
        layout.addWidget(button1)

        button2 = QPushButton('Metronom', self)
        button2.setStyleSheet("background-color: lightgrey;")
        button2.clicked.connect(self.on_button2_clicked)
        layout.addWidget(button2)

        self.setLayout(layout)

    def on_button1_clicked(self):
        try:
            subprocess.Popen(["python", r"C:\Users\gulus\OneDrive - st.biruni.edu.tr\Masaüstü\daf-generator-master\daf-generator-master\dafgen.py"])
        except FileNotFoundError:
            QMessageBox.critical(self, 'Error', 'dafgen.py dosyası bulunamadı.')
        except Exception as e:
            QMessageBox.critical(self, 'Error', f'Hata oluştu: {str(e)}')

    def on_button2_clicked(self):
        try:
            subprocess.Popen(["python", r"C:\Users\gulus\OneDrive - st.biruni.edu.tr\Masaüstü\HuanBu_Metronome-main\HuanBu_Metronome-main\src\huanbu.py"])
        except FileNotFoundError:
            QMessageBox.critical(self, 'Error', 'huanbu.py dosyası bulunamadı.')
        except Exception as e:
            QMessageBox.critical(self, 'Error', f'Hata oluştu: {str(e)}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
























