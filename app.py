from PySide6 import QtWidgets
from PySide6.QtCore import QEvent

from ui_main import Ui_MainWindow

import random


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.coracao.setVisible(False)

        self.botao_nao.clicked.connect(self.moveButton)
        self.botao_sim.clicked.connect(self.bestOption)

        self.frame_nao.installEventFilter(self)
        self.frame_sim.installEventFilter(self)

    def moveButton(self):
        self.frame_nao.move(random.randint(0, 300), random.randint(0, 300))

    def bestOption(self):
        self.querNamorarCmg.setText("Você escolheu a melhor opção!!!")
        self.querNamorarCmg.setStyleSheet("QLabel{\n"
                                    "	font-size: 25px;\n"
                                    "	font-weight: bold;\n"
                                    "	color: rgb(255, 255, 255);\n"
                                    "}\n")
        self.botao_sim.setVisible(False)
        self.botao_nao.setVisible(False)
        self.coracao.setVisible(True)

    def eventFilter(self, obj, event):
        if event.type() == QEvent.Enter and obj == self.frame_nao:
            self.moveButton()
            return True
        else:
            return False


app = QtWidgets.QApplication([])

window = MainWindow()
window.show()

app.exec()