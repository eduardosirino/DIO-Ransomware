import os
import hashlib
import pyaes

folder_path = input("Digite o caminho da pasta para ser descriptografada: ")
key = input("Digite a senha para a descriptografia: ")

key = hashlib.sha256(key.encode('utf-8')).digest()

aes = pyaes.AESModeOfOperationCTR(key)

for root, dirs, files in os.walk(folder_path):
    for file_name in files:
        if file_name.endswith('.encrypt'):
            file_path = os.path.join(root, file_name)

            with open(file_path, 'rb') as file:
                file_data = file.read()

            decrypted_data = aes.decrypt(file_data)

            os.remove(file_path)

            new_file_path = file_path.replace('.encrypt', '')

            with open(new_file_path, 'wb') as new_file:
                new_file.write(decrypted_data)

