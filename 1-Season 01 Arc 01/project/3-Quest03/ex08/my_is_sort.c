#include <stdbool.h>
#ifndef STRUCT_INTEGER_ARRAY
#define STRUCT_INTEGER_ARRAY
typedef struct s_integer_array
{
    int size;
    int* array;
} integer_array;
#endif

bool my_is_sort(integer_array* param_1)
{
    if (param_1->size <= 1) {
        return true;
    }

    bool ascending = true;
    bool descending = true;

    for (int i = 0; i < param_1->size - 1; i++) {
        if (param_1->array[i] > param_1->array[i + 1]) {
            ascending = false;
        }
        if (param_1->array[i] < param_1->array[i + 1]) {
            descending = false;
        }
    }

    return ascending || descending;
}
