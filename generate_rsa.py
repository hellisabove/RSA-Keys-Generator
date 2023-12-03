from Crypto.Protocol.KDF import PBKDF2
from Crypto.Random import get_random_bytes
from Crypto.Random.random import randint
from Crypto.PublicKey import RSA
import getpass
import base64

def notrand(n):
	notrand.i += 1
	return PBKDF2(master, str(notrand.i), dkLen=n, count=1)

# generate salt and get password
password = getpass.getpass()
salt = get_random_bytes(32)
master = PBKDF2(password, salt, count=10000)

# generate rsa key
notrand.i = randint(0,9)
RSA_Key = RSA.generate(4096, randfunc=notrand)

# export rsa keys
open('public_rsa.pem','wb').write(RSA_Key.publickey().exportKey('PEM'))
open('private_rsa.pem','wb').write(RSA_Key.exportKey('PEM'))

# easy import of public key for code
print("Copy the following line in your code: ")
print("masterkey = RSA.importKey(base64.b64decode(b\"{}\"))".format(base64.b64encode(RSA_Key.publickey().exportKey()).decode()))
