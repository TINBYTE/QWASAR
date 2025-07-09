#include <stdio.h>


int my_strlen(char* param_1)
{
    int length = 0;
    while (param_1[length] != '\0') {
        length++;
    }
    return length;
}