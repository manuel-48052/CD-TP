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
        imagem = Image.open(arquivo)
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
    #print("\nInformação própria:")
    for simbolo, frequencia in contagem.items():
        probabilidade = frequencia / total
        informacao = -math.log2(probabilidade)
      
    # Entropia
    entropia = sum(-freq/total * math.log2(freq/total) for freq in contagem.values())

    # Plot do histograma
    contagem = sorted(contagem.items())
    simbolos, frequencias = zip(*contagem)
    probabilidade = [freq/total for freq in frequencias]
    
    plt.bar(simbolos, frequencias)
    plt.title(arquivo)
    print(f"\nEntropia: {entropia:.4f}")
    plt.show()

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
    symbols = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(symbols) for _ in range(N))
    return password


def makeVernamCypher(plainText, theKey):
    cipherText = ''
    for i in range(len(plainText)):
        # Realiza o XOR bit a bit dos caracteres do texto claro e da chave
        cipherChar = chr(ord(plainText[i]) ^ ord(theKey[i]))
        cipherText += cipherChar
    return cipherText


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
           histograma_entropia("testfiles")  
        elif opcao == "2b":
           """(b) Considere os ficheiros ListaPalavrasEN.txt e ListaPalavrasPT.txt, os quais contêm listagens de palavras em
Língua Inglesa e Língua Portuguesa. Para cada Língua:
(i) Apresente uma estimativa da percentagem de ocorrência de cada símbolo (carater).
(ii) Apresente o valor da entropia de ambos os ficheiros."""
           histograma_entropia("testfiles2")
        elif opcao == "3b":
            probabilities = [0.25, 0.25, 0.25, 0.25]
            save_sequence('sequence.txt', 100, probabilities)

        elif opcao == "3c":
            print(generate_password(12))
        elif opcao == "4a":
            plainText = 'abcabcd'
            theKey = '3333333'

            # Cifra o texto claro
            cipherText = makeVernamCypher(plainText, theKey)
            print('Texto cifrado:', cipherText)

            # Decifra o texto cifrado
            decryptedText = makeVernamCypher(cipherText, theKey)
            print('Texto decifrado:', decryptedText)

        else:
            print("Opção inválida! Por favor, escolha um número.")

