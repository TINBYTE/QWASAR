#include <stdio.h>


void my_swap(int* param_1, int* param_2)
{
    int param_3 = *param_1;
    *param_1 = *param_2;
    *param_2 = param_3;

}