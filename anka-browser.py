import sys
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import * 
from PyQt5.QtGui import *

tab_name = "Google"

class AnkaBrowser(QMainWindow):
    def __init__(self):
        super().__init__()

        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)
        self.tabs.setTabsClosable(True)
        self.tabs.tabCloseRequested.connect(self.close_tab)
        self.setWindowIcon(QIcon("public/img/logo.ico"))

        self.add_new_tab(QUrl("https://www.google.com"), tab_name)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.load_url)
        self.url_bar.setPlaceholderText("URL...")
        self.url_bar.setFont(QFont("Lexend"))
        self.url_bar.setFixedHeight(25)
        self.url_bar.setStyleSheet("white-space: nowrap;")

        self.back_button = QPushButton()
        self.back_button.clicked.connect(self.browser_back)
        self.back_button.setIcon(QIcon("public/img/back.svg"))
        self.back_button.setFixedSize(QSize(25, 25))
        self.back_button.setIconSize(QSize(25, 25))
        self.back_button.setStyleSheet("background-color: transparent; border: none;")
        self.back_button.setCursor(QCursor(Qt.PointingHandCursor))
        
        self.forward_button = QPushButton()
        self.forward_button.clicked.connect(self.browser_forward)
        self.forward_button.setIcon(QIcon("public/img/forward.svg"))
        self.forward_button.setFixedSize(QSize(25, 25))
        self.forward_button.setIconSize(QSize(25, 25))
        self.forward_button.setStyleSheet("background-color: transparent; border: none;")
        self.forward_button.setCursor(QCursor(Qt.PointingHandCursor))

        self.new_tab_button = QPushButton()
        self.new_tab_button.clicked.connect(self.add_new_tab_button)
        self.new_tab_button.setIcon(QIcon("public/img/newtab.svg"))
        self.new_tab_button.setFixedSize(QSize(25, 25))
        self.new_tab_button.setIconSize(QSize(25, 25))
        self.new_tab_button.setStyleSheet("background-color: transparent; border: none;")
        self.new_tab_button.setCursor(QCursor(Qt.PointingHandCursor))
         
        
        top_layout = QHBoxLayout()
        top_layout.addWidget(self.back_button)
        top_layout.addWidget(self.forward_button)
        top_layout.addWidget(self.new_tab_button)
        top_layout.addWidget(self.url_bar)

        main_layout = QVBoxLayout()
        main_layout.addLayout(top_layout)  
        main_layout.addWidget(self.tabs)

        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

        self.setWindowTitle("Anka")
        self.showMaximized()  
        self.setWindowIcon(QIcon("public/img/logo.ico"))
        self.resize(1920, 1080)

        self.tabs.currentChanged.connect(self.update_url_from_tab)

        
    def add_new_tab(self, url, label):
        new_browser = QWebEngineView()
        new_browser.setUrl(url)
        self.tabs.addTab(new_browser, label)
        self.tabs.setCurrentWidget(new_browser)

        self.close_tab_button = QPushButton()
        self.close_tab_button.clicked.connect(lambda: self.close_tab(self.tabs.indexOf(new_browser)))
        self.close_tab_button.setCursor(QCursor(Qt.PointingHandCursor))

        new_browser.titleChanged.connect(lambda title: self.update_title(new_browser, title))
        new_browser.urlChanged.connect(lambda q: self.update_url(q))
        new_browser.setContextMenuPolicy(Qt.CustomContextMenu)
        new_browser.customContextMenuRequested.connect(self.show_context_menu)
    def close_tab(self, index):
        if self.tabs.count() == 1:
            exit()
        else:
            self.tabs.removeTab(index)

    def update_title(self, browser, title):
        index = self.tabs.indexOf(browser)
        self.tabs.setTabText(index, title if title else tab_name)

    def add_new_tab_button(self):
        self.add_new_tab(QUrl("https://www.google.com"), tab_name)

    def update_url(self, url):
        if isinstance(url, QUrl):
            self.url_bar.setText(url.toString())
        else:
            self.url_bar.clear()

    def update_url_from_tab(self):
        current_browser = self.tabs.currentWidget()
        if current_browser:
            current_url = current_browser.url()
            self.url_bar.setText(current_url.toString())

    def load_url(self):
        url = self.url_bar.text()
        if not url.startswith("http"):
            url = "https://" + url  
        current_browser = self.tabs.currentWidget()
        current_browser.setUrl(QUrl(url))

    def browser_back(self):
        current_browser = self.tabs.currentWidget()
        current_browser.back()

    def browser_forward(self):
        current_browser = self.tabs.currentWidget()
        current_browser.forward()
    
    def browser_reload(self):
        current_browser = self.tabs.currentWidget()
        current_browser.reload() 

    def show_context_menu(self, position):
        context_menu = QMenu(self)

        context_menu.addAction("Copy", self.browser_copy)
        context_menu.addAction("Paste", self.browser_paste)
        context_menu.addAction("Save", self.browser_save)
        context_menu.addAction("Back", self.browser_back)
        context_menu.addAction("Forward", self.browser_forward)
        context_menu.addAction("Reload", self.browser_reload)

        context_menu.exec_(self.tabs.currentWidget().mapToGlobal(position))

    def browser_copy(self):
        current_browser = self.tabs.currentWidget()
        current_browser.page().runJavaScript("window.getSelection().toString();", self.set_clipboard)

    def set_clipboard(self, text):
        clipboard = QApplication.clipboard()
        clipboard.setText(text)

    def browser_paste(self):
        clipboard = QApplication.clipboard()
        text = clipboard.text()
        current_browser = self.tabs.currentWidget()
        current_browser.page().runJavaScript(f"document.execCommand('insertText', false, '{text}');")

    def browser_save(self):
        current_browser = self.tabs.currentWidget()
        current_browser.page().toHtml(self.save_html)

    def save_html(self, html):
        file_name, _ = QFileDialog.getSaveFileName(self, "Kaydet", "", "HTML Dosyası (*.html);;Tüm Dosyalar (*)")
        if file_name:
            with open(file_name, 'w', encoding='utf-8') as file:
                file.write(html)

if __name__ == "__main__":
    app = QApplication(sys.argv)      
    anka_browser_window = AnkaBrowser()
    anka_browser_window.show()  
    sys.exit(app.exec_())
