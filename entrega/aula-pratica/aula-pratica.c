#include <stdio.h>

#define ASCII_TABLE_SIZE 128
#define TRUE 1

// Exercicio 1
int count_ones(int val) {
	int count = 0;
	while (val) {
		count += val & 0x1;
		val >>= 1;
	}
	return count;
}

int count_zeros(int val) {
	int count = 0;
	while (val) {
		count += !(val & 0x1);
		val >>= 1;
	}
	return count;
}

// Exercicio 2
void print_bits(int val) {
	int vals[32];
	int count = 0;

	while (val) {
		vals[count++] = val & 0x1;
		val >>= 1;
	}

	for (int i = count - 1; i >= 0; i--)
		printf("%d", vals[i]);

	printf("\n");
}

// Exercicio 3
int find_max_pos(int arr[], int size) {
	int curr_max_pos = 0;
	for (int i = 0; i < size; i++) {
		if (arr[i] > arr[curr_max_pos])
			curr_max_pos = i;
	}
	return curr_max_pos;
}

char most_frequent_symbol(char *file_name) {
	int occurrences[ASCII_TABLE_SIZE] = {0};
	int c;

	FILE *fp;

	fp = fopen(file_name, "r");

	if(fp == NULL) {
		printf("No file '%s' found.\n", file_name);
		return EOF;
	}

	while (TRUE) {
		c = fgetc(fp);
		if (c == EOF)
			break;
		occurrences[c]++;
	}

	fclose(fp);

	int pos = find_max_pos(occurrences, ASCII_TABLE_SIZE);

	printf("%d", occurrences[pos]);

	return pos;
}

// Exercicio 4
void negative_file(char *input_file_name, char *output_file_name) {
	int c;
	FILE *ifp, *ofp;

	ifp = fopen(input_file_name,"r");

	if(ifp == NULL)
		printf("No file '%s' found.\n", input_file_name);

	ofp = fopen(output_file_name,"a+");

	while(TRUE) {
		c = fgetc(ifp);
		fputc(~c, ofp);
		if (c == EOF)
			break;
	}

	fclose(ofp);
	fclose(ifp);
}

// void main() {
// 	//print_bits(10); //1010
// 	//printf("%d\n", res);
// 	char input_file_name[] = "file_name";
// 	char output_file_name[] = "file_out_name";
// 	//char res = most_frequent_symbol(file_name);
// //	char c= 'a';
// //	printf("%c",~c);

// 	negative_file(input_file_name, output_file_name);

// 	//printf("%c\n", res);
// }
