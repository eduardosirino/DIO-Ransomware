import os
import hashlib
import pyaes

folder_path = input("Digite o caminho da pasta para ser criptografada: ")

if not os.path.exists(folder_path):
    print(f"O caminho {folder_path} não existe.")
    quit()

key = input("Digite a senha para a criptografia: ")

key = hashlib.sha256(key.encode('utf-8')).digest()

aes = pyaes.AESModeOfOperationCTR(key)

for root, dirs, files in os.walk(folder_path):
    for file_name in files:
        file_path = os.path.join(root, file_name)
        
        with open(file_path, 'rb') as file:
            file_data = file.read()

        encrypted_data = aes.encrypt(file_data)

        os.remove(file_path)

        new_file_path = file_path + '.encrypt'

        with open(new_file_path, 'wb') as new_file:
            new_file.write(encrypted_data)

