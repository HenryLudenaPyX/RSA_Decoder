# RSA Encrypter in Python
This project is a basic implementation of message encryption and decryption using the RSA library in Python.
## Objective:
- Demonstrate how public and private keys work in asymmetric cryptography.

## Requirements:
Project developed in Python **3.12.10**, necessary dependencies:

```bash
pip install rsa
pip install cryptography
```

## Operation:
Run the generator.py script, the script performs the following process:

1. Obtain the relative path to the home directory (RSA_Decoder)
2. Obtain a 2048-bit private key with exponent 65537 (standard, Fermat number)
3. Obtain the public key from the private key
4. Create two PEM-formatted files where the keys are stored, respectively, in the "keys" folder

Run the decrypt.py script, which does the following:

1. Obtains the relative path of the home directory (RSA_Decoder)
2. Obtains the path of the two previously generated keys
3. Loads the public and private keys
4. Declares a variable with the message to be encrypted
5. Encrypts the message with the public key
6. Decrypts the message with the private key
7. Displays the encrypted, decrypted, and original messages.

