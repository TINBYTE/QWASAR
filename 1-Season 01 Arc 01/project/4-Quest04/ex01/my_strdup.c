#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* my_strdup(char* inchar) {
    int taille = strlen(inchar);
    
    char* outchar = (char*)malloc((taille + 1) * sizeof(char));
    if (!outchar) {
        return NULL;
    }

    for (int i = 0; i < taille; i++) {
        outchar[i] = inchar[i];
    }

    outchar[taille] = '\0';

    return outchar;
}
