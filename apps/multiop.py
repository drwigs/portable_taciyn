import random
import os
from time import sleep
import platform
import json

alph = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6,
    'g': 7,
    'h': 8,
    'i': 9,
    'j': 10,
    'k': 11,
    'l': 12,
    'm': 13,
    'n': 14,
    'ñ': 15,
    'o': 16,
    'p': 17,
    'q': 18,
    'r': 19,
    's': 29,
    't': 21,
    'u': 22,
    'v': 23,
    'w': 24,
    'x': 25,
    'y': 26,
    'z': 27,
    ' ': -1,
    '?': -2,
    ',': -3,
    'ó': -4,
    'í': -5,
    'é': -6,
    'á': -7,
    'ú': -8,
    '.': -9,
    '-': -10,
    '+': -11,
    '1': -12,
    '2': -13,
    '3': -14,
    '4': -15,
    '5': -16,
    '6': -17,
    '7': -18,
    '8': -19,
    '9': -20,
    '=': -21,
    '_': 22
}

chars = []

result = []

char_result = str()
    

op_a = int()
op_b = int()
op_c = int()

def crypt():
    to_crypt = input(">")
    to_crypt = to_crypt.lower()

    for i in to_crypt:
        try:
            chars.append(list(alph.values())[list(alph).index(i)])

        except ValueError:
            chars.append("?")
            print("Carácter: '", i, "' no soportado.")

    r = int()

    for j in chars:
        while r != j:
            op_a = random.randint(1,1000)
            op_b = random.randint(1,1000)
            op_c = random.randint(1,1000)
            op_d = random.randint(1,1000)
            #print(temporal_input_chars)
            #print(temporal_input_chars[len(temporal_input_chars)-1])   
            r = (op_a-op_b*(op_c/op_d))

        str_result = str(str(op_a)+'-'+str(op_b)+'*'+'('+str(op_c)+'/'+str(op_d)+')')
        result.append(str_result)

    result.append("")
    char_result = '~'.join(str(k) for k in result)
    if platform.system() == 'Linux':
        os.system("clear")
            
    else:
        os.system("cls")

    print(char_result)

dec_chars = []

to_decrypt_chars = []

decrypt_chars = []

def decrypt(to_decrypt):
    temporal_decrypt_char = str()
    temporal_to_decrypt = []
    for m in to_decrypt:
        temporal_to_decrypt.append(m)
    
    while temporal_to_decrypt.count('~') != len(dec_chars):
        for mm in temporal_to_decrypt:
            if mm == '~':
                dec_chars.append(temporal_decrypt_char)
                temporal_decrypt_char = str()
            
            else:
                temporal_decrypt_char = str(temporal_decrypt_char) + str(mm)
        
        
        data_return = {}
        for data_calc in dec_chars:
            exec('temporal_char = float('+data_calc+'); rr = temporal_char;', globals(), data_return)
            temporal_char = int(data_return['temporal_char'])
            #dec_chars.append(float(to_decrypt[0:(to_decrypt.index('~'))]))
            to_decrypt_chars.append(temporal_char)

        for l in to_decrypt_chars:
            decrypt_chars.append(list(alph.keys())[list(alph.values()).index(l)])

    if platform.system() == 'Linux':
        os.system("clear")
    
    else:
        os.system("cls")

    print(''.join(str(b) for b in decrypt_chars))

select = input("1.- Encriptar; 2.- Desencriptar; >")
if select == '1':
    crypt()

elif select == '2':
    char_to = input(">")
    decrypt(str(char_to))

else:
    print("Comando no admitido.")

