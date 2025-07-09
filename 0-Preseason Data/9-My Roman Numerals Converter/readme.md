# My Roman Numerals Converter

## Task

Create a function that converts an integer into its equivalent Roman numeral.
The function must return a string representation of the number using Roman numeral symbols.
You only need to support numbers up to around 3000.

---

## Description

The function works by mapping known Roman numeral values to their respective integers, from largest to smallest.
It subtracts from the input number while appending the corresponding Roman symbol until the number reaches zero.
For example:

* 14 → `XIV`
* 79 → `LXXIX`
* 845 → `DCCCXLV`
* 2022 → `MMXXII`

---

## Installation

No installation is required. This is a simple Python script.
Just make sure you have Python 3 installed.

---

## Usage

```python
from my_roman_numerals_converter import my_roman_numerals_converter

print(my_roman_numerals_converter(2022))  # Output: MMXXII
```

---

## Qwasar Reference

Abdelfattah Bouhlali


