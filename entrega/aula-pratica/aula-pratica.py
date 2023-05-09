import math

from collections import Counter
import matplotlib.pyplot as plt

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