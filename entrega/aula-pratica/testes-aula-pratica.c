#include "aula-pratica.h"
#include <stdio.h>

void main() {
    printf("Exercicio 1:\n");

    int ex_bits_1 = 263;

    int ex_bits_2 = 15;

    printf("%d tem %d ums.\n", ex_bits_1, count_ones(ex_bits_1));
    printf("%d tem %d zeros.\n", ex_bits_1, count_zeros(ex_bits_1));

    printf("%d tem %d ums.\n", ex_bits_2, count_ones(ex_bits_2));
    printf("%d tem %d zeros.\n", ex_bits_2, count_zeros(ex_bits_2));

    printf("\nExercicio 2:\n");

    printf("Vamos ler %d com recurso ao print_bits: ", ex_bits_1);
    print_bits(ex_bits_1);
    printf("Vamos ler %d com recurso ao print_bits: ", ex_bits_2);
    print_bits(ex_bits_2);
    printf("\n");

    printf("\nExercicio 3:\n");
    char input_file_name_1[] = "a.txt";
    // char solucao_1 = 'a';
    char input_file_name_2[] = "ListaPalavrasPT.txt";
    // char solucao_2 = 'a';
    printf(
        "Vamos saber o caracter mais frequente no ficheiro %s. Ocurrencias tem ",
        input_file_name_1
        );
    char result_1 = most_frequent_symbol(input_file_name_1);
    printf(" ... o caracter '%c'!\n", result_1);

    printf(
        "Vamos saber o caracter mais frequente no ficheiro %s. Ocurrencias tem ",
        input_file_name_2
        );
    char result_2 = most_frequent_symbol(input_file_name_2);
    printf(" ... o caracter '%c'!\n", result_2);

    printf("\nExercicio 4:\n");
    char input_file_name_orig[] = "a.txt";
    char input_file_name_neg[] = "a_negative.txt";
    char input_file_name_rec[] = "a_recovered.txt";

    negative_file(input_file_name_orig, input_file_name_neg);
    negative_file(input_file_name_neg, input_file_name_rec);

    printf(
        "O ficheiro %s é o negativo de %s. Portanto, como %s é o negativo de %s, %s tem de ser igual a %s.\n",
        input_file_name_neg, input_file_name_orig,
        input_file_name_rec, input_file_name_neg,
        input_file_name_rec, input_file_name_orig
        );
}