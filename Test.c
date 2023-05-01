#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

#define MAX_SYMBOLS 256

int count_ones(int val) {
    int count = 0;
    while(val != 0) {
        if(val & 1) { 
            count++;
        }
        val >>= 1; 
    }
    return count;
}



int count_zeros(int val) {
    int count = 0;
    while(val != 0) {
        if((val & 1) == 0) { 
            count++;
        }
        val >>= 1;
    }
    return count;
}

char most_frequent_symbol(char *file_name) {
    int count[MAX_SYMBOLS] = {0}; // array para armazenar a frequência de cada símbolo
    char symbol;
    int max_count = 0;
    char most_frequent;
    FILE *fp = fopen(file_name, "r");
    while((symbol = fgetc(fp)) != EOF) { // lê cada caractere do arquivo até o final do arquivo (EOF)
        if(isalpha(symbol)) { // verifica se o caractere é uma letra
            symbol = tolower(symbol); // converte a letra para minúscula
            count[symbol]++; // incrementa a frequência do símbolo no array
            if(count[symbol] > max_count) { // verifica se a frequência do símbolo atual é maior do que a do símbolo mais frequente  
                max_count = count[symbol];
                most_frequent = symbol;
            }
        }
    }
    fclose(fp); // fecha o arquivo
    printf("O simbolo mais frequente no arquivo %s e: %c (%d ocorrencias)\n", file_name, most_frequent, max_count);
    return most_frequent;
}

void print_bits( int val ) {
    int count = 0;
    while(val != 0) {
        if((val & 1) == 0) { 
            printf("0");
        }else{
            printf("1");
        }
        val >>= 1;
    }
    printf("\n");

}

void negative_file(char *input_file_name, char *output_file_name) {
    FILE *input_file = fopen(input_file_name, "rb");
    if(input_file == NULL) { // verifica se houve erro ao abrir o arquivo de entrada
        printf("Erro ao abrir o arquivo de entrada.\n");
        exit(1);
    }
    FILE *output_file = fopen(output_file_name, "wb");
    if(output_file == NULL) { // verifica se houve erro ao abrir o arquivo de saída
        printf("Erro ao abrir o arquivo de saida.\n");
        exit(1);
    }
    int byte;
    while((byte = fgetc(input_file)) != EOF) { // lê cada byte do arquivo até o final do arquivo (EOF)
        byte = ~byte; // nega cada bit do byte
        fputc(byte, output_file); // escreve o byte negado no arquivo de saída
    }
    fclose(input_file); // fecha o arquivo de entrada
    fclose(output_file); // fecha o arquivo de saída
}


int main() {
    int val = 9;
   // printf("Digite um valor inteiro: ");
   // scanf("%d", &val);
   // printf("O valor digitado tem %d bits iguais a 1 e %d bits iguais a 0.\n", count_ones(val), count_zeros(val));

    //print_bits(val);
    char file_name[100] = "text.txt";
    most_frequent_symbol(file_name);

    return 0;
}
