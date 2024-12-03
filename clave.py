from cryptography.fernet import Fernet
clave = Fernet.generate_key()  # Genera la clave
print(clave)  # Imprime la clave generada
