#include <stdlib.h>
#include <string.h>
#include <stdio.h>

char* my_spaceship(char* param_1) {
    // Position initiale
    int x = 0;
    int y = 0;
    int dir = 0; // 0=up, 1=right, 2=down, 3=left

    // Directions en texte
    char* directions[] = {"up", "right", "down", "left"};

    // Parcours du plan de vol
    for (int i = 0; param_1[i] != '\0'; i++) {
        if (param_1[i] == 'R') {
            dir = (dir + 1) % 4; // tourner à droite
        } else if (param_1[i] == 'L') {
            dir = (dir + 3) % 4; // tourner à gauche (équivalent à -1 mod 4)
        } else if (param_1[i] == 'A') {
            if (dir == 0) y--;       // up
            else if (dir == 1) x++;  // right
            else if (dir == 2) y++;  // down
            else if (dir == 3) x--;  // left
        }
    }

    // Format final à renvoyer
    char* result = (char*)malloc(100 * sizeof(char));
    snprintf(result, 100, "{x: %d, y: %d, direction: '%s'}", x, y, directions[dir]);
    return result;
}
