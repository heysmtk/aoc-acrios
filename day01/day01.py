# PART 1

# Otevírá a čte ze souboru, kde jsou data a ty ukládá do listu
with open("day01/large_data.txt", "r") as file:
    content = file.readlines()

# For cykl, který vytáhne položku po položce z listu a pracuje s ní dál
total = 0  
for item in content:
    # List comprehension - Vyfiltrování čísel z jednotlivých položek dat
    numbers = [char for char in item if char.isdigit()]
    total += int(numbers[0] + numbers[-1])  # Sečtění první a poslední číslice z položky dat a uložení do proměnné "total"

print(total)

# PART 2
