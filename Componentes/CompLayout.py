# -*- coding: utf-8 -*-
from Componentes import *

class TextBox(QLineEdit):
    def __init__(self, parent=None):
        super(TextBox, self).__init__(parent)
        self.setFont(QFont("Microsoft Sans Serif",14,QFont.Bold,False))


class Label(QLabel):
    def __init__(self, pText='', parent=None):
        super(Label, self).__init__(parent)
        self.setText(pText)
        self.setStyleSheet(open('style.css').read())


class CheckBox(QCheckBox):
    def __init__(self, pText='', parent=None):
        super(CheckBox, self).__init__(parent)

        self.setText(pText)

class ComboBox(QComboBox):
    def __init__(self, pText='', parent=None):
        super(ComboBox, self).__init__(parent)
        self.setFont(QFont("Microsoft Sans Serif",14,QFont.Bold,False))
        self.setEditable(False)



class OpcaoBotao(QRadioButton):
    def __init__(self, pText='', parent=None):
        super(OpcaoBotao, self).__init__(parent)
        self.setStyleSheet(open('style.css').read())
        self.setText(pText)

class Botao(QPushButton):
    def __init__(self, pText='', parent=None):
        super(Botao, self).__init__(parent)
        self.setStyleSheet(open('style.css').read())
        self.setText(pText)

class TBotao(QToolButton):
    def __init__(self, pText='', parent=None):
        super(TBotao, self).__init__(parent)
        self.setStyleSheet(open('style.css').read())
        self.setText(pText)


class LayoutVertical(QVBoxLayout):
    def __init__(self):
        super(LayoutVertical, self).__init__()


class LayoutHorizontal(QHBoxLayout):
    def __init__(self):
        super(LayoutHorizontal, self).__init__()


class Widget(QWidget):
    def __init__(self, parent=None):
        super(Widget, self).__init__()


class FormLayout(QFormLayout):
    def __init__(self):
        super(FormLayout, self).__init__()

class GridLayout(QGridLayout):
    def __init__(self):
        super(GridLayout, self).__init__()

class Frame(QGroupBox):
    def __init__(self):
        super(Frame, self).__init__()
        self.setStyleSheet(open('style.css').read())


class Dialog(QDialog):
    def __init__(self, parent=None):
        super(Dialog, self).__init__(parent)


class Grid(QTableWidget):
    def __init__(self, parent=None, qtde_linhas=0, qtde_colunas=0):
        super(Grid, self).__init__(parent)

        self.setRowCount(qtde_linhas)
        self.setColumnCount(qtde_colunas)

        self.resizeRowsToContents()
        self.setAlternatingRowColors(True)
        self.setSortingEnabled(True)
        self.setSelectionBehavior(QAbstractItemView.SelectRows)


class MessageBox(QMessageBox):
    def __init__(self, parent=None):
        super(MessageBox, self).__init__(parent)
        self.setWindowTitle('AVISO:')
        self.setWindowIcon(QIcon('icone.png'))
