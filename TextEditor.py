import sys
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtPrintSupport import *


class TextEditor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.current_file_path = None
        self.initUI()

    def initUI(self):
        self.text_edit = QTextEdit()
        self.setCentralWidget(self.text_edit)

        self.create_actions()
        self.create_menus()

        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle('Simple Text Editor')
        self.show()

    def create_actions(self):
        self.open_action = QAction('Open', self)
        self.open_action.setShortcut('Ctrl+O')
        self.open_action.triggered.connect(self.open_file)

        self.save_action = QAction('Save', self)
        self.save_action.setShortcut('Ctrl+S')
        self.save_action.triggered.connect(self.save_file)

        self.save_as_action = QAction('Save As', self)
        self.save_as_action.setShortcut('Ctrl+Shift+S')
        self.save_as_action.triggered.connect(self.save_file_as)

        self.exit_action = QAction('Exit', self)
        self.exit_action.setShortcut('Ctrl+Q')
        self.exit_action.triggered.connect(self.close)

        self.copy_action = QAction('Copy', self)
        self.copy_action.setShortcut('Ctrl+C')
        self.copy_action.triggered.connect(self.text_edit.copy)

        self.cut_action = QAction('Cut', self)
        self.cut_action.setShortcut('Ctrl+X')
        self.cut_action.triggered.connect(self.text_edit.cut)

        self.paste_action = QAction('Paste', self)
        self.paste_action.setShortcut('Ctrl+V')
        self.paste_action.triggered.connect(self.text_edit.paste)

        self.font_action = QAction('Font', self)
        self.font_action.triggered.connect(self.choose_font)


    def create_menus(self):
        menubar = self.menuBar()
        file_menu = menubar.addMenu('File')
        file_menu.addAction(self.open_action)
        file_menu.addAction(self.save_action)
        file_menu.addAction(self.save_as_action)
        file_menu.addAction(self.exit_action)

        edit_menu = menubar.addMenu('Edit')
        edit_menu.addAction(self.copy_action)
        edit_menu.addAction(self.cut_action)
        edit_menu.addAction(self.paste_action)

        settings_menu = menubar.addMenu('Settings')
        settings_menu.addAction(self.font_action)

    def open_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, 'Open File')
        if file_path:
            try:
                with open(file_path, 'r') as file:
                    text = file.read()
                    self.text_edit.setText(text)
                self.current_file_path = file_path
            except Exception as e:
                QMessageBox.critical(self, 'Error', str(e))

    def save_file(self):
        if not self.current_file_path:
            self.save_file_as()
        else:
            try:
                text = self.text_edit.toPlainText()
                with open(self.current_file_path, 'w') as file:
                    file.write(text)
            except Exception as e:
                QMessageBox.critical(self, 'Error', str(e))

    def save_file_as(self):
        file_path, _ = QFileDialog.getSaveFileName(self, 'Save File As')
        if file_path:
            try:
                text = self.text_edit.toPlainText()
                with open(file_path, 'w') as file:
                    file.write(text)
                self.current_file_path = file_path
            except Exception as e:
                QMessageBox.critical(self, 'Error', str(e))

    def choose_font(self):
        font, ok = QFontDialog.getFont(self.text_edit.font(), self)
        if ok:
            self.text_edit.setFont(font)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    editor = TextEditor()
    sys.exit(app.exec_())
