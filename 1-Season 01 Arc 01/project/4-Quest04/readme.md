# Bienvenue dans Quest04
***

## Tâche
Résoudre 6 exercices en langage C autour de la manipulation de chaînes de caractères, de tableaux dynamiques, et de logique de déplacement :
- ex00 : Découper une chaîne en mots
- ex01 : Compter les mots dans une chaîne
- ex02 : Afficher un tableau de chaînes
- ex03 : Compter la taille de chaque mot
- ex04 : Fusionner des mots avec un séparateur
- ex05 : Simuler les mouvements d’un vaisseau spatial

## Description

### ex00 - `my_split`
Découpe une chaîne de caractères en mots (séparés par des espaces ou des tabulations). Le défi est de détecter correctement les mots et d’allouer dynamiquement un tableau de chaînes.

### ex01 - `my_count_words`
Compte le nombre de mots dans une chaîne. Une fonction utilitaire qui prépare aux traitements plus complexes de chaînes.

### ex02 - `my_print_words_array`
Affiche les éléments d’un tableau de chaînes, un mot par ligne, en utilisant votre propre fonction `my_putstr`. Cela renforce l’usage des boucles et de l’affichage personnalisé.

### ex03 - `my_count_on_it`
Reçoit un tableau de chaînes et retourne un tableau d’entiers contenant la longueur de chaque chaîne. Vous devez gérer une structure contenant un tableau alloué dynamiquement.

### ex04 - `my_join`
Fusionne un tableau de chaînes avec un séparateur (comme `join()` en Python). Vous devez calculer la mémoire totale nécessaire et construire soigneusement le résultat.

### ex05 - `my_spaceship`
Simule le déplacement d’un vaisseau spatial dans une grille infinie, selon des commandes (`R`, `L`, `A`). Il faut gérer l’orientation et retourner une chaîne formatée avec les coordonnées finales.

## Installation
Pour compiler tous les fichiers :
```bash
make
```

Ou pour compiler chaque fichier séparément :
```bash
gcc -Wall -Wextra -Werror mon_fichier.c -o mon_executable
```

## Utilisation

Chaque exécutable peut être lancé indépendamment. Exemples :
```
./my_spaceship RAALALL
./my_print_words_array
```

Vous pouvez créer des fichiers `main()` pour tester chaque fonction.

### L’équipe principale

<span><i>Réalisé chez <a href='https://qwasar.io'>Qwasar SV -- École d'ingénierie logicielle</a></i></span>  
<span><img alt='Logo de Qwasar SV' src='https://storage.googleapis.com/qwasar-public/qwasar-logo_50x50.png' width='20px' /></span>