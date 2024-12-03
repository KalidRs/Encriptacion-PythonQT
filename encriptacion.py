from cryptography.fernet import Fernet


CLAVE = b"O48_qDFOB1r0PTM6mts3M0CZb3e6oj9xk15dKV6wJbI="  # La clave debe tener 32 caracteres (base64)


fernet = Fernet(CLAVE)

# Encriptar texto
def encriptar_texto(texto):
    texto_bytes = texto.encode('utf-8')
    texto_encriptado = fernet.encrypt(texto_bytes)
    return texto_encriptado.decode('utf-8')

def desencriptar_texto(texto_encriptado):
    texto_bytes = texto_encriptado.encode('utf-8')
    texto_desencriptado = fernet.decrypt(texto_bytes)
    return texto_desencriptado.decode('utf-8')

# Encriptar imagen
def encriptar_imagen(ruta_imagen):
    with open(ruta_imagen, 'rb') as f:  # Abrir imagen en modo binario
        imagen_bytes = f.read()  # Leer contenido binario
    imagen_encriptada = fernet.encrypt(imagen_bytes)
    return imagen_encriptada

# Desencriptar imagen
def desencriptar_imagen(imagen_encriptada, ruta_guardado):
    imagen_bytes = fernet.decrypt(imagen_encriptada)  # Desencriptar imagen
    with open(ruta_guardado, 'wb') as f:  # Guardar imagen desencriptada
        f.write(imagen_bytes)
