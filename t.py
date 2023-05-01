import os
import math
import random

import string

from collections import Counter
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def geometric_progression(u, r, N):
    for i in range(N):
        print(u * (r ** i))


def mdc_euclides(a, b):
    if b == 0:
        return a
    else:
        return mdc_euclides(b, a % b)


def most_least_frequent_symbols(file_path):
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








"""5. Escreva as seguintes funções em linguagem ‘Python’. Para cada função, apresente os resultados obtidos no seu funcionamento.
(a) Função que apresenta os primeiros N termos da progressão geométrica de primeiro termo u e razão r. Os valores de N,
u e r são passados como parâmetro.

(b) Função que determina o máximo divisor comum entre dois números inteiros a e b, através do algoritmo de Euclides.

(c) Função que identifica os símbolos mais frequente e menos frequente de um ficheiro passado como parâmetro, indicando
a frequência de ocorrência desses dois símbolos.

(d) Função que apresenta o histograma de um ficheiro, o valor da informação própria de cada símbolo e a entropia do
ficheiro."""


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


def empirical_entropy(symbols):
    """
    Função que calcula a entropia empírica de uma sequência de símbolos.
    """
    frequencies = np.zeros(len(set(symbols)))
    for symbol in symbols:
        frequencies[symbol] += 1
    probabilities = frequencies / len(symbols)
    entropy = -np.sum(probabilities * np.log2(probabilities))
    return entropy


def ex_3b():
    probabilities = [0.25, 0.25, 0.25, 0.25]

    # gerar sequências
    save_sequence('sequence_10.txt', 10, probabilities)
    save_sequence('sequence_100.txt', 100, probabilities)
    save_sequence('sequence_1000.txt', 1000, probabilities)
    save_sequence('sequence_10000.txt', 10000, probabilities)

    # calcular entropias empíricas
    with open('sequence_10.txt') as f:
        symbols = [int(line.strip()) for line in f]
        emp_entropy_10 = empirical_entropy(symbols)
        true_entropy = -np.sum(probabilities * np.log2(probabilities))
        print(f"Entropia empírica para sequência de tamanho 10: {emp_entropy_10}")
        print(f"Entropia verdadeira: {true_entropy}")

    with open('sequence_100.txt') as f:
        symbols = [int(line.strip()) for line in f]
        emp_entropy_100 = empirical_entropy(symbols)
        print(f"Entropia empírica para sequência de tamanho 100: {emp_entropy_100}")

    with open('sequence_1000.txt') as f:
        symbols = [int(line.strip()) for line in f]
        emp_entropy_1000 = empirical_entropy(symbols)
        print(f"Entropia empírica para sequência de tamanho 1000: {emp_entropy_1000}")

    with open('sequence_10000.txt') as f:
        symbols = [int(line.strip()) for line in f]
        emp_entropy_10000 = empirical_entropy(symbols)
        print(f"Entropia empírica para sequência de tamanho 100000: {emp_entropy_10000}")


def generate_password(N):
    symbols = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(symbols) for _ in range(N))
    return password




if __name__ == "__main__":
    while True:
        # Exibe um menu de opções para o usuário
        print("Escolha uma opção:")
        print("1. Opção um")
        print("2. Opção dois")
        print("3. Opção três")

        
        # Recebe a entrada do usuário
        opcao = input("Digite o número da opção desejada: ")

        # Executa a opção escolhida pelo usuário
        if opcao == "1":
            #a)
            print("alinia a)") 
            geometric_progression(5, 2, 3)
            print("alinia b)")        
            a = 84
            b = 18
            mdc = mdc_euclides(a, b)
            print("O MDC de", a, "e", b, "é", mdc)

        elif opcao == "2":
            #f = "fox.txt"
            #entropy(f)
            #most_least_frequent_symbols(f)
            #histograma_entropia(f)

            pasta = "testfiles"
            arquivos = os.listdir(pasta)
            for arquivo in arquivos:
                histograma_entropia(pasta+"/"+arquivo) 
        elif opcao == "3":
            #-------------ex 3  a)------------

            #probabilities = [0.25, 0.25, 0.25, 0.25]
            #save_sequence('sequence.txt', 100, probabilities)

            #-------------ex 3  b)------------
            #ex_3b()
            #Recorra à implementação da fonte de símbolos, 
            # para realizar um gerador de palavras-passe robustas, com dimensão entre
            # 8 e 12 caracteres. Apresente cinco exemplos de palavras-passe geradas
            pas = generate_password(7)
            print(pas)

        else:
            print("Opção inválida! Por favor, escolha um número.")

