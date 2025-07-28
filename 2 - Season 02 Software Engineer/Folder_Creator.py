import os

# Define folder structure
folders = {
    "Projects": [
        "My Bsq",
        "Ruby Quest01",
        "My Levenshtein",
        "Ruby Quest02",
        "Ruby Quest03",
        "Ruby Quest04",
        "Ruby Quest05",
        "Ruby Quest06",
        "My Hamming Dna",
        "My Roman Numerals Converter",
        "My Bc",
        "My Mouse",
        "My Allocine",
        "My Zsh",
        "My Css Is Easy I",
        "My Sqlite",
        "My Curl",
        "My Libasm",
        "My Malloc"
    ],
    "Exercises": [
        "Add Prime Sum",
        "Average Of Levels In Binary Tree",
        "Binary Prefix Divisible By 5",
        "Brackets",
        "Capitalize",
        "Count Letter",
        "Find Words That Can Be Formed By Characters",
        "Frog Jump",
        "Is Anagram",
        "Is Power Of 2",
        "Jewels And Stones",
        "Last Word",
        "Longest Arithmetic Subsequence Of Given Difference",
        "Maximum Gap",
        "My Abs",
        "My Array Uniq",
        "My Atoi",
        "My Capitalize",
        "My Cat",
        "My Christmas Tree",
        "My Data Process",
        "My Initializer",
        "My Is Negative",
        "My Is Sort",
        "My Isspace",
        "My Iterative Pow",
        "My Join",
        "My Mult",
        "My Range",
        "My Recursive Factorial",
        "My Robot Simulator",
        "My Roman Numerals Converter",
        "My Sort",
        "My Square",
        "My Strchr",
        "My Strip",
        "My Strstr",
        "My Swap",
        "My Union",
        "Number Of Atoms",
        "Ord Alphlong",
        "Pascals Triangle Ii",
        "Print Duplicates",
        "Remove Duplicate Letters",
        "Rev Wstr",
        "Rostring",
        "Rotone",
        "Satisfiability Of Equality Equations",
        "Str Maxlenoc",
        "Valid Anagram"
    ]
}

# Create the directories with numbering
for main_folder, subfolders in folders.items():
    os.makedirs(main_folder, exist_ok=True)
    for i, subfolder in enumerate(subfolders, start=1):
        # Format with leading zeroes if desired (e.g., 01, 02, ...)
        numbered_name = f"{i:02d} - {subfolder}"
        path = os.path.join(main_folder, numbered_name)
        os.makedirs(path, exist_ok=True)

print("All numbered folders created successfully.")
