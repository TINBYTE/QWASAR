#include <stdio.h>

int my_string_index(char* param_1, char param_2)
{
    int index = 0;
    while(param_1[index] != '\0'){
        if(param_1[index] == param_2){
            return index;
        }
        index++;
    }
    return -1;
}