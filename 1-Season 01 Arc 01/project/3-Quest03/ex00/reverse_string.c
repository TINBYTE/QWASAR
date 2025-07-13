#include <stdio.h>
#include <string.h>
#include <stdlib.h>

char* reverse_string(char* chaine1)
{
    //taille de param_1
    int len_chaine1 = strlen(chaine1);

    char *chaine2 = (char *) malloc (len_chaine1 + 1);

    // inverser les elements
    for(int i=0 ; i < len_chaine1 ; i++){
        chaine2[i] = chaine1[len_chaine1 - i - 1];
    }

    return chaine2;
}