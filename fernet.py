from cryptography.fernet import Fernet
key = ''
f = Fernet(key)
token = ''
print(f.decrypt(token))