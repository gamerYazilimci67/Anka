import sys
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import * 
from PyQt5.QtGui import *

class AnkaBrowser(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("http://www.google.com"))  

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.load_url)
        self.url_bar.setPlaceholderText("URL girin...")
        self.url_bar.setFont(QFont("Lexend"))
        self.url_bar.setFixedHeight(25)
        self.url_bar.setStyleSheet("white-space: nowrap;")

        self.geri_buton = QPushButton()
        self.geri_buton.clicked.connect(lambda: self.browser.back())
        self.geri_buton.setIcon(QIcon("public/img/back.svg"))
        self.geri_buton.setFixedSize(QSize(25,25))
        self.geri_buton.setIconSize(self.geri_buton.size())
        self.ileri_buton = QPushButton()
        self.ileri_buton.clicked.connect(lambda: self.browser.forward())
        self.ileri_buton.setIcon(QIcon("public/img/forward.svg"))
        self.ileri_buton.setFixedSize(QSize(25,25))
        self.ileri_buton.setIconSize(self.ileri_buton.size())

        self.geri_buton.setStyleSheet("background: transparent; color: black; border: none;")
        self.ileri_buton.setStyleSheet("background: transparent; color: black; border: none;")
        
        self.geri_buton.setCursor(Qt.PointingHandCursor)
        self.ileri_buton.setCursor(Qt.PointingHandCursor)

        main_layout = QVBoxLayout()

        top_layout = QHBoxLayout()
        top_layout.addWidget(self.geri_buton)
        top_layout.addWidget(self.ileri_buton)
        top_layout.addWidget(self.url_bar)

        main_layout.addLayout(top_layout)  
        main_layout.addWidget(self.browser)

        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

        self.browser.urlChanged.connect(self.update_url)

        self.setWindowTitle("Anka")
        self.showMaximized()  
        self.setWindowIcon(QIcon("public/img/logo.ico"))
        self.resize(1920, 1080)
        self.setIconSize(QSize(500,500))



    def load_url(self):
        url = self.url_bar.text()
        if not url.startswith("http"):
            url = "http://" + url  
        self.browser.setUrl(QUrl(url))
    
    def update_url(self, url):
        self.url_bar.setText(url.toString())
   

anka = QApplication(sys.argv)      
anka_browser_window = AnkaBrowser()
anka_browser_window.show()  
sys.exit(anka.exec_())
