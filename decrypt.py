import pyperclip
from colorama import Fore, Back, Style

import colorama
colorama.init()
print(Fore.BLUE + 'Encrypter/Decrypter by: ArasoOsara')

number = int(input("Channel Frequency: "))

encrypt = {num:number - num for num in range(32, 99999)}
decrypt = {value:key for key, value in encrypt.items()}

print(Fore.RED + 'Code to decrypt: ')
sentence = input("")
decrypted_string = sentence.translate(decrypt)

print(Fore.GREEN + 'Decrypted code: ')
print(decrypted_string)
pyperclip.copy(f'{decrypted_string}')

input()