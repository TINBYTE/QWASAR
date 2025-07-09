#include <stdio.h>

char* my_downcase(char* param_1)
{
    int i = 0;
    while (param_1[i] != '\0') {
        if (param_1[i] >= 'A' && param_1[i] <= 'Z') {
            param_1[i] = param_1[i] + 32;
        }
        i++;
    }
    return param_1;
}