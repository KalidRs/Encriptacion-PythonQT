from PyQt5 import QtWidgets
from Windowbuttom import Ui_Windowbuttom  # Importa la interfaz de la ventana principal
from frmEncriptar import Ui_frmEncriptar  # Importa la interfaz de la ventana de encriptación

class Menu(QtWidgets.QMainWindow, Ui_Windowbuttom):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)  

        self.pushButton.clicked.connect(self.show_frm_encriptar)

    def show_frm_encriptar(self):
        # Crear la ventana de encriptación
        self.frm_encriptar = QtWidgets.QMainWindow()
        self.ui_frmencriptar = Ui_frmEncriptar()  # Instanciar la interfaz de encriptación
        self.ui_frmencriptar.setupUi(self.frm_encriptar)  # Configura la interfaz de la ventana de encriptación
        self.frm_encriptar.show()  # Mostrar la ventana de encriptación

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = Menu()  # Crear la ventana del menú
    window.show()  # Mostrar la ventana del menú
    app.exec_()
