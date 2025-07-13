#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int my_strcmp(char* param_1, char* param_2)
{
    while (*param_1 && *param_2) {
        if (*param_1 != *param_2) {
            return (*param_1 > *param_2) ? 1 : -1;
        }
        param_1++;
        param_2++;
    }

    if (*param_1 == *param_2) {
        return 0;
    }

    return (*param_1 > *param_2) ? 1 : -1;
}
