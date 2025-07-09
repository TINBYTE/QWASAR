#!/bin/bash

# Create main folders
mkdir -p project exercices

# Define and sort project names
projects=(
  "Quest01"
  "Quest02"
  "Quest03"
  "Quest04"
  "My Square"
  "Quest05"
  "My Cat"
  "My Ngram"
  "My Mastermind"
  "My Printf"
)

exercises=(
  "Alpha Mirror"
  "Last Word"
  "My Array Uniq"
  "My First Script"
  "My Initializer"
  "My Isdigit"
  "My Iterative Pow"
  "My Mult"
  "My Range"
  "My Strcmp"
  "My Strcpy"
  "My Strrchr"
  "My Sub"
)

# Create numbered project folders and files
index=1
for name in "${projects[@]}"; do
  folder="project/${index}-${name}"
  mkdir -p "$folder"
  touch "$folder/code.py" "$folder/readme.md"
  ((index++))
done

# Create numbered exercise folders and files
index=1
for name in "${exercises[@]}"; do
  folder="exercices/${index}-${name}"
  mkdir -p "$folder"
  touch "$folder/code.py" "$folder/readme.md"
  ((index++))
done

echo "Ordered folder structure created successfully!"
