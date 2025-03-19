# PART 1

# Otevírá a čte ze souboru, kde jsou data a ty ukládá do listu
with open("day01/large_data.txt", "r") as file:
    content = file.readlines()
  
total = 0  
for item in content:
    numbers = [char for char in item if char.isdigit()]  # Listová komprehenze, která mi vyfiltruje čísla do listů
    total += int(numbers[0] + numbers[-1])

print(total)