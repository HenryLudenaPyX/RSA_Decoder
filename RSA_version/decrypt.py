import rsa
from pathlib import Path

# Get current (relative) path to the actual directory:
current_dir = Path(__file__).parent.parent

#Get path for public key :
abs_path_public = (current_dir / "keys/public_key.pem")

#Get path for private key:
abs_path_private = (current_dir / "keys/private_key.pem")

# Paso 1: Obtener claves pública y privada
# Cargar clave pública
with open(abs_path_public, "rb") as f:
    public_key = rsa.PublicKey.load_pkcs1_openssl_pem(f.read())

# Cargar clave privada
with open(abs_path_private, "rb") as f:
    private_key = rsa.PrivateKey.load_pkcs1(f.read())

# Paso 2: Mensaje original
mensaje = "Hola, mundo criptográfico!".encode('utf-8')

# Paso 3: Cifrar el mensaje con la clave pública
mensaje_cifrado = rsa.encrypt(mensaje, public_key)

# Paso 4: Descifrar con la clave privada
mensaje_descifrado = rsa.decrypt(mensaje_cifrado, private_key)

# Paso 5: Mostrar resultados
print("Mensaje original:", mensaje.decode())
print("Mensaje cifrado (bytes):", mensaje_cifrado)
print("Mensaje descifrado:", mensaje_descifrado.decode())