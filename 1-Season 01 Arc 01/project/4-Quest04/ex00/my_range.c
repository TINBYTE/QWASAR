#include <stdio.h>
#include <stdlib.h>

int* my_range(int min, int max) {
    if (min >= max) {
        return NULL;
    }

    int size = max - min;
    int* my_array = (int*) malloc(size * sizeof(int));
    if (!my_array) {
        return NULL; 
    }

    for (int i = 0; i < size; i++) {
        my_array[i] = min + i;
    }

    return my_array;
}