#pip install PyCryptodome

from Crypto.Cipher import AES
key = "abcdefghijklmnop"
cipher = AES.new(key.encode("utf8"), AES.MODE_ECB)
msg = cipher.encrypt(b"TechTutorialsX!!TechTutorialsX!!")
print(type(msg))
print(msg.hex())
decipher = AES.new(key.encode("utf8"), AES.MODE_ECB)
msg_dec = decipher.decrypt(msg)
print(msg_dec)
print(type(msg_dec))