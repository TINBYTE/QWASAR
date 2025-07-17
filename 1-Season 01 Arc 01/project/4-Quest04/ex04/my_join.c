#include <stdlib.h>
#include <string.h>

#ifndef STRUCT_STRING_ARRAY
#define STRUCT_STRING_ARRAY
typedef struct s_string_array
{
    int size;
    char** array;
} string_array;
#endif

char* my_join(string_array* param_1, char* param_2)
{
    if (param_1->size == 0) {
        return NULL;  // tableau vide → retourne NULL
    }

    int total_length = 0;
    int sep_len = strlen(param_2);

    // 1. Calcul de la taille totale à allouer
    for (int i = 0; i < param_1->size; i++) {
        total_length += strlen(param_1->array[i]);
        if (i < param_1->size - 1) {
            total_length += sep_len;
        }
    }

    // +1 pour le caractère nul final
    char* result = (char*)malloc((total_length + 1) * sizeof(char));
    if (!result) return NULL;

    result[0] = '\0'; // initialise la chaîne

    // 2. Concaténation des mots et séparateurs
    for (int i = 0; i < param_1->size; i++) {
        strcat(result, param_1->array[i]);
        if (i < param_1->size - 1) {
            strcat(result, param_2);
        }
    }

    return result;
}
