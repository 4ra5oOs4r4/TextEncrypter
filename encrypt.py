import pyperclip
from colorama import Fore, Back, Style

import colorama
colorama.init()
print(Fore.BLUE + 'Encrypter/Decrypter by: ArasoOsara')

number = int(input("Channel Frequency: "))

encrypt = {num:number - num for num in range(32, 99999)}
print(Fore.GREEN + 'Message to encrypt: ')
sentence = input("")
encrypted_string = sentence.translate(encrypt)

print(Fore.RED + 'Decrypted code: ')
print(Fore.RED + encrypted_string)
pyperclip.copy(f'{encrypted_string}')

input()