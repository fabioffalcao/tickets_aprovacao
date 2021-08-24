from aprova import aprova_tickets
from PyQt5 import QtCore, QtGui, QtWidgets
import os

class Ui_mainAprova(object):
    def setupUi(self, mainAprova):

        path='.\driver\chromedriver.exe'
        if not os.path.isfile(path):
            error_dialog = QtWidgets.QMessageBox()
            error_dialog.setIcon(QtWidgets.QMessageBox.Warning)
            error_dialog.setWindowTitle("ERRO")
            error_dialog.setStandardButtons(QtWidgets.QMessageBox.Ok)            
            error_dialog.setText("ALERTA: Driver do Google Chrome não encontrado!!!")
            error_dialog.exec_()
            sys.exit(self)

        mainAprova.setObjectName("mainAprova")
        mainAprova.resize(343, 170)
        self.centralWidget = QtWidgets.QWidget(mainAprova)
        self.centralWidget.setObjectName("centralWidget")
        self.lblUserNewmonitor = QtWidgets.QLabel(self.centralWidget)
        self.lblUserNewmonitor.setGeometry(QtCore.QRect(40, 60, 71, 16))
        self.lblUserNewmonitor.setObjectName("lblUserNewmonitor")
        self.lblSenhaNewmonitor = QtWidgets.QLabel(self.centralWidget)
        self.lblSenhaNewmonitor.setGeometry(QtCore.QRect(40, 80, 71, 16))
        self.lblSenhaNewmonitor.setObjectName("lblSenhaNewmonitor")
        self.usrNewmonitor = QtWidgets.QLineEdit(self.centralWidget)
        self.usrNewmonitor.setGeometry(QtCore.QRect(100, 60, 113, 20))
        self.usrNewmonitor.setObjectName("usrNewmonitor")
        self.passNewmonitor = QtWidgets.QLineEdit(self.centralWidget)
        self.passNewmonitor.setGeometry(QtCore.QRect(100, 80, 113, 20))
        self.passNewmonitor.setObjectName("passNewmonitor")
        self.passNewmonitor.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passNewmonitor.returnPressed.connect(self.onClickBtnExecutar)
        self.btnExecutar = QtWidgets.QPushButton(self.centralWidget)
        self.btnExecutar.setGeometry(QtCore.QRect(230, 80, 75, 23))
        self.btnExecutar.setObjectName("btnExecutar")
        self.btnExecutar.clicked.connect(self.onClickBtnExecutar)
        self.lblNewmonitor = QtWidgets.QLabel(self.centralWidget)
        self.lblNewmonitor.setGeometry(QtCore.QRect(70, 0, 201, 51))
        self.lblNewmonitor.setObjectName("lblNewmonitor")
        self.progressBar = QtWidgets.QProgressBar(self.centralWidget)
        self.progressBar.setEnabled(True)
        self.progressBar.setGeometry(QtCore.QRect(10, 110, 321, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName("progressBar")
        self.progressBar.setValue(0)
        self.chkVisualizar = QtWidgets.QCheckBox(self.centralWidget)
        self.chkVisualizar.setGeometry(QtCore.QRect(230, 50, 91, 23))
        self.chkVisualizar.setObjectName("chkVisualizar")       
        mainAprova.setCentralWidget(self.centralWidget)
        self.mainToolBar = QtWidgets.QToolBar(mainAprova)
        self.mainToolBar.setObjectName("mainToolBar")
        mainAprova.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(mainAprova)
        self.statusBar.setObjectName("statusBar")
        mainAprova.setStatusBar(self.statusBar)

        self.retranslateUi(mainAprova)
        QtCore.QMetaObject.connectSlotsByName(mainAprova)

    def retranslateUi(self, mainAprova):
        _translate = QtCore.QCoreApplication.translate
        mainAprova.setWindowTitle(_translate("mainAprova", "Aprovação Tickets GMUD"))
        self.lblUserNewmonitor.setText(_translate("mainAprova", "Usuário:"))
        self.lblSenhaNewmonitor.setText(_translate("mainAprova", "Senha:"))
        self.btnExecutar.setText(_translate("mainAprova", "Executar"))
        self.lblNewmonitor.setText(_translate("mainAprova", "Digite as informações de\n"
"conexão com o Newmonitor"))
        self.chkVisualizar.setText(_translate("mainAprova", "Visualizar"))

    def onClickBtnExecutar(self):
        userNewmonitor = self.usrNewmonitor.text()
        passNewmonitor = self.passNewmonitor.text()

        if self.chkVisualizar.isChecked():
            headless = False
        else:
            headless = True

        error_dialog = QtWidgets.QMessageBox()
        error_dialog.setIcon(QtWidgets.QMessageBox.Warning)
        error_dialog.setWindowTitle("ERRO")
        error_dialog.setStandardButtons(QtWidgets.QMessageBox.Ok)

        msg_dialog = QtWidgets.QMessageBox()
        msg_dialog.setIcon(QtWidgets.QMessageBox.Information)
        msg_dialog.setWindowTitle("AVISO")
        msg_dialog.setStandardButtons(QtWidgets.QMessageBox.Ok)

        progresso = self.progressBar
        progresso.setValue(0)

        if len(userNewmonitor) > 0 and len(passNewmonitor) > 0:

            ticketsProcessados = aprova_tickets(userNewmonitor, passNewmonitor, progresso, headless) 
            if ticketsProcessados >= 0:           
                msg_dialog.setText("Foram aprovados "+str(ticketsProcessados)+" tickets!!!")
                msg_dialog.exec_()
            else:
                error_dialog.setText("ALERTA: Usuário ou Senha incorretos!!!")
                error_dialog.exec_()

        else:
            error_dialog.setText("ALERTA: Não pode conter campos vazios!!!")
            error_dialog.exec_()



if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    principal = QtWidgets.QMainWindow()
    ui = Ui_mainAprova()
    ui.setupUi(principal)
    principal.show()
    sys.exit(app.exec_())
