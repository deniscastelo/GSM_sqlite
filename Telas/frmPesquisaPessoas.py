from Telas.frmPadrao import frmPadrao

class frmPesquisaPessoas(frmPadrao):

    def __init__(self, parent= None):
        super(frmPesquisaPessoas,self).__init__(parent)
        self.setFixedSize(800,600)
        self.setWindowTitle('Pesquisa de Pessoas')

'''
if __name__ == '__main__':
    root = QApplication(sys.argv)
    app = frmPesquisaPessoas(None)
    app.show()
'''
