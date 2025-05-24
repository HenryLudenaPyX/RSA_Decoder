from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from pathlib import Path
#Get current (relative) path to the actual directory:
current_dir = Path(__file__).parent.parent
#Create a private key with 2048 bits
private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
#Get the public key
public_key = private_key.public_key()

#Save the private key
with open((current_dir / "keys/private_key.pem"), "wb") as f:
    #Translating private_key to PEM with serialization
 f.write(private_key.private_bytes(
 serialization.Encoding.PEM,
 #SSL Format
 serialization.PrivateFormat.TraditionalOpenSSL,
 #Private key with no password (only testing)
 serialization.NoEncryption()
 ))
with open((current_dir / "keys/public_key.pem"), "wb") as f:
 f.write(public_key.public_bytes(
 serialization.Encoding.PEM,
 #Use public standard format
 serialization.PublicFormat.SubjectPublicKeyInfo
 ))