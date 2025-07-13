char* my_strstr(char* param_1, char* param_2)
{
    if (*param_2 == '\0') {
        return param_1;
    }

    while (*param_1 != '\0') {
        char* h = param_1;
        char* n = param_2;

        while (*h == *n && *n != '\0') {
            h++;
            n++;
        }

        if (*n == '\0') {
            return param_1;
        }

        param_1++;
    }

    return 0; 
}
