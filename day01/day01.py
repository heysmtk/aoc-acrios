# PART 1 of Day 01
import re

# Otevírá a čte ze souboru, kde jsou data a ty ukládá do listu po řádku
with open("day01/large_data.txt", "r") as file:
    content = file.readlines()

# # For cykl, který vytáhne položku po položce z listu a pracuje s ní dál
total = 0  
for item in content:
    # List comprehension - Vyfiltrování čísel z jednotlivých položek dat
    numbers = [char for char in item if char.isdigit()]
    total += int(numbers[0] + numbers[-1])  # Sečtění první a poslední číslice z položky dat a uložení do proměnné "total"

print(f"Result of PART 1: {total}")  # 55172

# PART 2 of Day 02
# Později se k tomu vrátím...