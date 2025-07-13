#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* my_strncpy(char* param_1, char* param_2, int n)
{
    int i = 0;

    while (i < n && param_2[i] != '\0') {
        param_1[i] = param_2[i];
        i++;
    }

    while (i < n) {
        param_1[i] = '\0';
        i++;
    }

    return param_1;
}
