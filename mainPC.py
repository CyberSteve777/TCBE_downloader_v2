import os
import sys
from PyQt5.QtWidgets import *
from DownloaderUI import Ui_Form
from utils import ReleaseGetter


class GUIDownloader(Ui_Form, QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("TerrariaCraft-Bedrock Downloader")
        # self.setWindowIcon()
        self.getter = ReleaseGetter()
        self.initUI()
        self.show()

    def initUI(self):
        self.update_list()
        self.pushButton.clicked.connect(self.customPath)
        self.pushButton_2.clicked.connect(self.download)

    def customPath(self):
        path = QFileDialog.getExistingDirectory()
        self.lineEdit.setText(path)

    def download(self):
        download_path = self.lineEdit.text()
        if not os.path.isdir(download_path):
            er = QMessageBox.critical(self, "Error", "Error: Invalid path")
            if er:
                pass
        else:
            self.hide()
            version = self.comboBox.currentText()
            self.getter.download(version, download_path)
            self.show()
            ok = QMessageBox.information(self, "Success", f"Successfully downloaded to: {download_path}"
                                                          f"\nYou can close downloader")
            if ok:
                pass

    def update_list(self):
        self.comboBox.clear()
        self.getter.update()
        self.comboBox.addItems(self.getter.releases_list_str)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    g = GUIDownloader()
    sys.exit(app.exec())
