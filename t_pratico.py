import os
import math
import random

import string

from collections import Counter
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


def geometric_progression(u, r, N):
    """ tp 5)a Função que apresenta os primeiros N termos da progressão
      geométrica de primeiro termo u e razão r. Os valores de N,
u e r são passados como parâmetro.
"""
    for i in range(N):
        print(u * (r ** i))


def mdc_euclides(a, b):
    """ Função que determina o máximo divisor comum entre dois números inteiros a e b, através do algoritmo de Euclides"""
    if b == 0:
        return a
    else:
        return mdc_euclides(b, a % b)
    

def most_least_frequent_symbols(file_path):
    """Função que identifica os símbolos mais frequente e menos frequente de um ficheiro passado como parâmetro, indicando
a frequência de ocorrência desses dois símbolos."""
    with open(file_path, "r") as f:
        text = f.read()
        frequency = {}
        for char in text:
            if char in frequency:
                frequency[char] += 1
            else:
                frequency[char] = 1
        sorted_frequency = sorted(frequency.items(), key=lambda x: x[1])
        least_frequent = sorted_frequency[0]
        most_frequent = sorted_frequency[-1]
        print(f"Least frequent symbol: '{least_frequent[0]}' with frequency {least_frequent[1]}")
        print(f"Most frequent symbol: '{most_frequent[0]}' with frequency {most_frequent[1]}")


def entropy(file_path):
    """função de calculo de entropia simples (não utilizado )"""
    with open(file_path, "r") as f:
        text = f.read()
        frequency = {}
        for char in text:
            if char in frequency:
                frequency[char] += 1
            else:
                frequency[char] = 1
        n = sum(frequency.values())
        entropy = 0
        print("Symbol\tFrequency\tP(x)\tInformation")
        for char, freq in frequency.items():
            p = freq / n
            information = -math.log2(p)
            print(f"{char}\t{freq}\t\t{p:.3f}\t{information:.3f}")
            entropy += p * math.log2(p)
        print(f"Entropy: {-entropy:.3f}")


def histograma_entropia(arquivo):
    """Função que apresenta o histograma de um ficheiro, o valor da informação própria de cada símbolo e a entropia do
ficheiro"""
    if arquivo.endswith('.txt'):
        with open(arquivo, 'r') as f:
            dados = f.read()
        # Process the text data here
    elif arquivo.endswith('.bmp'):
        with open(arquivo, 'rb') as f:
            dados = f.read()
        # imagem = Image.open(arquivo)
        # Process the BMP image data here
    elif arquivo.endswith('.c') or arquivo.endswith('.java') or arquivo.endswith('.htm'):
        with open(arquivo, 'r') as f:
            dados = f.read()
    else:
        print("Formato de arquivo não suportado.")
        print(arquivo)
        return

    contagem = Counter(dados)
    total = sum(contagem.values())

    # Informação própria
    own_info = {k: -math.log2(v/total) for k, v in contagem.items()}

    print("Informação própria:")
    for k, v in own_info.items():
        print(f"{k}: {v:.4f}")
      
    # Entropia
    entropia = sum(-freq/total * math.log2(freq/total) for freq in contagem.values())

    # Plot do histograma
    contagem = sorted(contagem.items())
    simbolos, frequencias = zip(*contagem)
    # probabilidade = [freq/total for freq in frequencias]
    
    plt.bar(simbolos, frequencias)
    plt.title(arquivo)
    print(f"\nEntropia: {entropia:.4f}")
    plt.show()
 

def generic_symbol_source_memory(n: int, m: dict[str, float]) -> str:
    probabilities: list[float] = list(m.values())
    alphabet: list[str] = list(m.keys())
    alphabet_size: int = len(m)
    return [alphabet[np.random.choice(alphabet_size, p=probabilities)] for _ in range(n)]

def generic_symbol_source(n: int, m: dict[str, float], filename: str) -> None:
    """
    Função que gera ficheiros de N simbolos de acordo com a FMP do alfabeto de M símbolos.
    """
    generated_symbols: list[str] = generic_symbol_source_memory(n, m)
    with open(filename, 'w') as f:
        for s in generated_symbols:
            f.write(s)


#-------3-----------
def generate_sequence(N, probabilities):
    """
    Função que gera uma sequência de N símbolos de acordo com as probabilidades
    definidas na FMP.
    """
    symbols = []
    for i in range(N):
        symbol = np.random.choice(len(probabilities), p=probabilities)
        symbols.append(symbol)
    return symbols


def save_sequence(filename, N, probabilities):
    """
    Função que gera e salva em um arquivo uma sequência de N símbolos de acordo com as
    probabilidades definidas na FMP.
    """
    symbols = generate_sequence(N, probabilities)
    with open(filename, 'w') as f:
        for symbol in symbols:
            f.write(str(symbol) + '\n')


def generate_password(N):
    """generate random word with N number ofcharacters wit leters digits and puntuation"""
    symbols = string.ascii_letters + string.digits
    password = ''.join(random.choice(symbols) for _ in range(N))
    return password


def makeVernamCypher(plainText, theKey):
    cipherText = ""
    for i in range(len(plainText)):
        # Realiza o XOR bit a bit dos caracteres do texto claro e da chave
        cipherChar = chr(ord(plainText[i]) ^ ord(theKey[i]))
        cipherText += cipherChar
    return cipherText


def bsc(seq, p):
    output_s = ""
    for leter in seq:
        leter_bin = format(ord(leter), 'b')    
        bits = []
        for bit in leter_bin:
            # Extract the i-th bit using bitwise operations
           # bit = (leter_bin >> i) & 1
            if random.random() < p:
                bits.append(int(bit) ^ 1)
            else:
                bits.append(int(bit))

        bit_str = ''.join(str(bit) for bit in bits)
        output_int = int(bit_str, 2)
        output_s += chr(output_int)

    return output_s



def ber(seq1, seq2):
    def tobits(s):
        result = []
        for c in s:
            bits = bin(ord(c))[2:]
            bits = '00000000'[len(bits):] + bits
            result.extend([int(b) for b in bits])
        return result
    
    a = tobits(seq1)
    b = tobits(seq2)

    diff_bits = 0

    for i in range(len(a)):
        diff_bits += a[i] ^ b[i]

    return diff_bits / len(a)


# Função de entrelaçamento
def interleave(msg, rows, cols,length):
    interleaved = np.zeros((rows, cols), dtype=str)
    idx = 0
    for j in range(cols):
        for i in range(rows):
            if(idx==length):
                break
            interleaved[i, j] = msg[idx]
            idx += 1
        if(idx==length):
                break
    
    return interleaved


# Função de desentrelaçamento
def deinterleave(interleaved,rows,cols):
    msg = ""
    for j in range(cols):
        for i in range(rows):
            #if  interleaved[i, j] == -1:
             #   break
            msg += interleaved[i, j]   

    return msg


def create_strong_password_memory(size: int, symbols: str = None) -> str:
    possible_symbols: str = symbols if symbols else string.ascii_letters + string.digits + string.punctuation
    symbol_probability: float = 1.0 / len(possible_symbols)
    alphabet: dict[str, float] = {s: symbol_probability for s in possible_symbols}
    return generic_symbol_source_memory(size, alphabet)


def create_strong_password(size: int, filename: str, symbols: str = None) -> None:
    possible_symbols: str = symbols if symbols else string.ascii_letters + string.digits + string.punctuation
    symbol_probability: float = 1.0 / len(possible_symbols)
    alphabet: dict[str, float] = {s: symbol_probability for s in possible_symbols}
    generic_symbol_source(size, alphabet, filename)

if __name__ == "__main__":
    while True:
        # Exibe um menu de opções para o usuário
        print("Escolha uma opção:")
        print("1a1: - 5a")
        print("1a2: - 5b")
        print("1a3: - 5c")
        print("2a:  1a4 e 2a")
        print("2b")
        print("3b")
        print("3c")
        print("4a")
        print("4b")
        print("5a")
        # Recebe a entrada do usuário
        opcao = input("Digite o número da opção desejada: ")

        # Executa a opção escolhida pelo usuário
        if opcao == "1a1":           
            geometric_progression(2,5,16)
        elif opcao == "1a2":
            mdc_euclides(45,66)
        elif opcao == "1a3":
            most_least_frequent_symbols("fox.txt")
        elif opcao == "2a":
            pasta = "testfiles"
            arquivos = os.listdir(pasta)
            for arquivo in arquivos:
                histograma_entropia(pasta+"/"+arquivo)
        elif opcao == "2b":
            """(b) Considere os ficheiros ListaPalavrasEN.txt e ListaPalavrasPT.txt, os quais contêm listagens de palavras em
Língua Inglesa e Língua Portuguesa. Para cada Língua:
(i) Apresente uma estimativa da percentagem de ocorrência de cada símbolo (carater).
(ii) Apresente o valor da entropia de ambos os ficheiros."""
            pasta = "testfiles2"
            arquivos = os.listdir(pasta)
            for arquivo in arquivos:
                histograma_entropia(pasta+"/"+arquivo)
        elif opcao == "3b":
            alphabet: dict[str, float] = {
                "a": 0.50,
                "b": 0.25,
                "c": 0.125,
                "d": 0.125
            }
            generic_symbol_source(100, alphabet, 'seq_100.txt')
            generic_symbol_source(1000, alphabet, 'seq_1000.txt')
            generic_symbol_source(10000, alphabet, 'seq_10000.txt')
            generic_symbol_source(100000, alphabet, 'seq_100000.txt')

            print(f"Entropia para N=100:")
            entropy('seq_100.txt')
            print(f"Entropia para N=1000:")
            entropy('seq_1000.txt')
            print(f"Entropia para N=10000:")
            entropy('seq_10000.txt')
            print(f"Entropia para N=100000:")
            entropy('seq_100000.txt')

            # probabilities = [0.25, 0.25, 0.25, 0.25]
            # save_sequence('sequence.txt', 100, probabilities)
        elif opcao == "3c":
            create_strong_password(8, 'password8.txt')
            create_strong_password(9, 'password9.txt')
            create_strong_password(10, 'password10.txt')
            create_strong_password(11, 'password11.txt')
            create_strong_password(12, 'password12.txt')

            # print(generate_password(12))
        elif opcao == "4a":
            plainText = 'abcabcd'
            theKey = '3333333'

            # Cifra o texto claro
            cipherText = makeVernamCypher(plainText, theKey)
            print('Texto cifrado:', cipherText)

            # Decifra o texto cifrado
            decryptedText = makeVernamCypher(cipherText, theKey)
            print('Texto decifrado:', decryptedText)
        elif opcao == "4b":            
            with open("testfiles/alice29.txt", 'r') as file:
                
                alice = file.read()
            length = len(alice)      
            theKey = "A"*length
            #chave constante
            cipherText = makeVernamCypher(alice, theKey)
            with open("alice_cipherd.txt", 'w') as f:
                for symbol in cipherText:
                    f.write(str(symbol))

            histograma_entropia("alice_cipherd.txt")

            #chave aleatoria
            the_key_random = create_strong_password_memory(length)
            cipher_text_random = makeVernamCypher(alice, the_key_random)
            with open("alice_cipherd_random.txt", 'w') as f:
                for symbol in cipher_text_random:
                    f.write(str(symbol))

            histograma_entropia("alice_cipherd_random.txt")
        elif opcao == "5a":
            with open("testfiles/alice29.txt", 'r') as file:                
                alice = file.read()
            length = len(alice)      
            the_key_random = generate_password(length)
            
            #chave constante
            cipherText = makeVernamCypher(alice, the_key_random)
            output_bits = bsc(cipherText, 0.001)
            plain_text = makeVernamCypher(output_bits, the_key_random) 

            with open("alice29_with_ber.txt", 'wb') as f:
                f.write(bytes(plain_text, 'ASCII'))

            print(f"BER: {ber(alice,plain_text)}")

        elif opcao == "5b":
            with open("testfiles/alice29.txt", 'r') as file:                
                alice = file.read()
            length = len(alice)      

            cols = 7
            rows =math.ceil(length/cols)
            
            intervaled_text = interleave(alice,rows,cols)

            to_deintel = np.zeros((rows, cols), dtype=str)           

            for i in range(rows): 
                len_c = len(intervaled_text[i])

                the_key_random = generate_password(len_c)    
                joined = "".join(intervaled_text[i])

                cipherText = makeVernamCypher(joined, the_key_random)     
                output_bits = bsc(cipherText, 0.001)  
                plain_text = makeVernamCypher(output_bits, the_key_random)

                for j in range(len(plain_text)):
                    to_deintel[i][j] = plain_text[j]
                
           
            de_inter_text = deinterleave(to_deintel,rows,cols)
            
            with open("alice_cipherd_random_ber_intervel.txt", 'wb') as f:
                f.write(bytes(de_inter_text, 'ASCII'))
            print(f"BER: {ber(de_inter_text, alice)}") 

        elif opcao == "6":
            with open("testfiles/U.txt", 'r') as file:                
                alice = file.read()
            length = len(alice)      

            cols = 3
            rows =math.ceil(length/cols)
            
            intervaled_text = interleave(alice,rows,cols,length)
            

            to_deintel = np.zeros((rows, cols), dtype=str)           

            for i in range(rows): 
                len_c = len(intervaled_text[i])

                the_key_random = generate_password(len_c)    
                joined = "".join(intervaled_text[i])

                cipherText = makeVernamCypher(joined, the_key_random)     
                output_bits = bsc(cipherText, 0.1)  
                plain_text = makeVernamCypher(output_bits, the_key_random)

                for j in range(len(plain_text)):
                    to_deintel[i][j] = plain_text[j]
                
           
            de_inter_text = deinterleave(to_deintel,rows,cols)
            
            with open("alice_cipherd_random_ber_intervel.txt", 'wb') as f:
                f.write(bytes(de_inter_text, 'ASCII'))
            print(f"BER: {ber(de_inter_text, alice)}") 
      
        else:
            print("Opção inválida! Por favor, escolha um número.")

