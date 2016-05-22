import sys
from Componentes import *
from Telas.frmPadrao import frmPadrao

class frmCadastroPessoas(frmPadrao):

    def __init__(self, parent= None):
        super(frmCadastroPessoas,self).__init__(parent)
        self.setFixedSize(800,600)
        self.setWindowTitle('Cadastro de Pessoas')
        self.frmCadastroPessoas_Load()

    def frmCadastroPessoas_Load(self):
        #layouts
        self.fLayout = FormLayout()
        self.gradeCheckBox = GridLayout()

        #definindo campos
        self.lblID = Label('Matricula')
        self.txtID = TextBox()
        self.txtID.setFixedWidth(150)

        self.lblNome = Label('Nome')
        self.txtNome = TextBox()
        #self.txtNome.setFixedWidth(350)

        self.lblFuncao = Label('Função')
        self.txtFuncao = TextBox()
        self.txtFuncao.setFixedWidth(350)

        self.lblTurno = Label('Turno')
        self.txtTurno = TextBox()
        self.txtTurno.setFixedWidth(100)

        self.lblCoord = Label('Coordenador')
        self.comboCoord = ComboBox()
        self.cbCoordenador()

        self.teste = Botao('criar ck')
        self.teste.clicked.connect(INTO())

        #adicionando campos ao layout
        self.fLayout.addRow(self.lblID,self.txtID)
        self.fLayout.addRow(self.lblNome,self.txtNome)
        self.fLayout.addRow(self.lblFuncao,self.txtFuncao)
        self.fLayout.addRow(self.lblTurno,self.txtTurno)
        self.fLayout.addRow(self.lblCoord,self.comboCoord)
        self.fLayout.addRow(self.teste)

        self.fLayout.addItem(self.gradeCheckBox)





        self.setLayout(self.fLayout)

    def cbCoordenador(self):
        for row in cbCoordenadorPop():
            self.comboCoord.addItem(row[1])

    def criarCKBOX(self):



        self.ck1 = CheckBox('')
        self.ck2 = CheckBox('')
        self.ck3 = CheckBox('')
        self.ck4 = CheckBox('')
        self.ck5 = CheckBox('')
        self.ck6 = CheckBox('')
        self.ck7 = CheckBox('')
        self.ck8 = CheckBox('')
        self.ck9 = CheckBox('')
        self.ck10 = CheckBox('')
        self.ck11 = CheckBox('')
        self.ck12 = CheckBox('')
        self.ck13 = CheckBox('')
        self.ck14 = CheckBox('')
        self.ck15 = CheckBox('')
        self.ck16 = CheckBox('')
        self.ck17 = CheckBox('')
        self.ck18 = CheckBox('')








if __name__ == '__main__':
    root = QApplication(sys.argv)
    app = frmCadastroPessoas(None)
    app.show()
    root.processEvents()
    root.exec_()
