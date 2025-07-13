#include <stdio.h>
#include <stdlib.h>
#include <string.h>


char* my_strchr(char* param_1, char param_2)
{
    while (*param_1 != '\0') {
        if (*param_1 == param_2) {
            return param_1;
        }
        param_1++;
    }

    // Vérifie aussi si on cherche '\0'
    if (param_2 == '\0') {
        return param_1;
    }

    return 0;  // NULL si pas trouvé
}
