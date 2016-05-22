from ControleVersao.CtrlVersao import *
from Telas import *



class Aplicacao(Widget):
    def __init__(self, parent=None):
        super(Aplicacao, self).__init__(parent)
        self.setFixedSize(600, 400)
        self.setWindowTitle('GSM %s' % getVersion())
        create_table()

        self.AplicacaoLoad()

    def AplicacaoLoad(self):
        self.LayoutPrincipal = LayoutHorizontal()

        gradeBotoes = GridLayout()

        # Botões
        self.btnCadastroPessoas = Botao()
        self.btnCadastroPessoas.setIcon(QIcon('Imagens/pessoa_cad.ico'))
        self.btnCadastroPessoas.setIconSize(QSize(150, 150))
        self.btnCadastroPessoas.clicked.connect(self.btnCadastroPessoas_Click)

        self.btnCadastroItens = Botao()
        self.btnCadastroItens.setIcon(QIcon('Imagens/admin.png'))
        self.btnCadastroItens.setIconSize(QSize(150, 150))

        self.btnEntradaItens = Botao()
        self.btnEntradaItens.setIcon(QIcon('Imagens/entrada.ico'))
        self.btnEntradaItens.setIconSize(QSize(150, 150))

        self.btnSaidaItens = Botao()
        self.btnSaidaItens.setIcon(QIcon('Imagens/saida.ico'))
        self.btnSaidaItens.setIconSize(QSize(150, 150))

        self.btnHistorico = Botao()
        self.btnHistorico.setIcon(QIcon('Imagens/his.png'))
        self.btnHistorico.setIconSize(QSize(150, 150))

        self.btnGraficos = Botao()
        self.btnGraficos.setIcon(QIcon('Imagens/graf.ico'))
        self.btnGraficos.setIconSize(QSize(150, 150))

        self.btnDebug = Botao()
        self.btnDebug.setIcon(QIcon('Imagens/admin2.png'))
        self.btnDebug.setIconSize(QSize(150, 150))

        gradeBotoes.addWidget(self.btnEntradaItens, 0, 1)
        gradeBotoes.addWidget(self.btnSaidaItens, 0, 2)
        gradeBotoes.addWidget(self.btnCadastroPessoas, 0, 3)
        gradeBotoes.addWidget(self.btnHistorico, 1, 1)
        gradeBotoes.addWidget(self.btnGraficos, 1, 2)
        gradeBotoes.addWidget(self.btnDebug, 1, 3)

        self.LayoutPrincipal.addLayout(gradeBotoes)
        self.setLayout(self.LayoutPrincipal)

    def btnCadastroPessoas_Click(self):
        frmPessoas = frmCadastroPessoas(self)
        frmPessoas.setModal(True)
        frmPessoas.show()
        frmPessoas.exec_()


if __name__ == '__main__':
    root = QApplication(sys.argv)
    app = Aplicacao(None)
    app.show()
    root.exec_()
