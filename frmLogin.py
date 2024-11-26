from PyQt5 import QtWidgets
from login import Ui_MainWindow  # Importa la interfaz del login
from Menu import Menu  # Importa la ventana de menú
from PyQt5.QtWidgets import QMessageBox

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):  
        super().__init__(*args, **kwargs)
        self.setupUi(self)  

        self.Aceptar.clicked.connect(self.validar)
        self.cancelar.clicked.connect(self.salir)  

    def validar(self):
        usuario = self.txtUsuario.text()
        contrasena = self.txtContrasena.text()

        # Contraseña y usuario
        if usuario == "kalid" and contrasena == "1234":
            self.mostrar_mensaje("Bienvenido", "Accedido correctamente.")
            self.openMenu()  
            self.hide() 
        else:
            self.mostrar_mensaje("Error", "Usuario o contraseña incorrectos.")

    def salir(self):
        msg_box = QMessageBox(self)
        msg_box.setIcon(QMessageBox.Question)
        msg_box.setWindowTitle("Confirmación")
        msg_box.setText("¿Estás seguro de que quieres cerrar la aplicación?")
        msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        
        if msg_box.exec_() == QMessageBox.Yes:
            self.close()

    def mostrar_mensaje(self, titulo, mensaje):
        msg_box = QtWidgets.QMessageBox(self)
        msg_box.setIcon(QtWidgets.QMessageBox.Information if titulo == "Bienvenido" else QtWidgets.QMessageBox.Critical)
        msg_box.setWindowTitle(titulo)
        msg_box.setText(mensaje)
        msg_box.exec_()

    def openMenu(self):
        opennewWindow = Menu(self) 
        opennewWindow.show() 

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow() 
    window.show() 
    app.exec_()
