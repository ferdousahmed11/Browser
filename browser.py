'''from qtpy.QtCore import QUrl
from qtpy.QtWebEngineWidgets import QWebEngineView
from qtpy.QtWidgets import QApplication
import sys

app = QApplication(sys.argv)

view = QWebEngineView()
view.setUrl(QUrl("https://www.example.com"))
view.show()

sys.exit(app.exec_()) '''


#with all functions
from qtpy.QtCore import QUrl
from qtpy.QtWebEngineWidgets import QWebEngineView
from qtpy.QtWidgets import QApplication, QMainWindow, QToolBar, QLineEdit, QAction
import sys

class WebBrowser(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Web Browser")

        self.view = QWebEngineView()
        self.setCentralWidget(self.view)

        self.create_toolbar()

    def create_toolbar(self):
        toolbar = QToolBar()
        self.addToolBar(toolbar)

        back_action = QAction("Back", self)
        back_action.triggered.connect(self.view.back)
        toolbar.addAction(back_action)

        forward_action = QAction("Forward", self)
        forward_action.triggered.connect(self.view.forward)
        toolbar.addAction(forward_action)

        refresh_action = QAction("Refresh", self)
        refresh_action.triggered.connect(self.view.reload)
        toolbar.addAction(refresh_action)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.load_url)
        toolbar.addWidget(self.url_bar)

    def load_url(self):
        url = self.url_bar.text()
        if url.startswith("http://") or url.startswith("https://"):
            self.view.setUrl(QUrl(url))
        else:
            self.view.setUrl(QUrl("http://" + url))

if __name__ == "__main__":
    app = QApplication(sys.argv)

    browser = WebBrowser()
    browser.view.setUrl(QUrl("https://www.example.com"))
    browser.show()

    sys.exit(app.exec_())
