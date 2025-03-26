# --- PART ONE ---

def load_data(name_of_file):
    """Načtení dat ze souboru. Čtení celého souboru a
    odstranění prázdného řádku"""
    
    with open(name_of_file, "r") as file:
        data = file.read().strip()

    patterns = data.split("\n\n")  # Rozdělení podle prázdných řádků
    return [pattern.split("\n") for pattern in patterns]  # Split na list řádků

# Kontrolní výpis načtených vzorů (grids)
patterns = load_data("day13/input_data.txt")
print(f"Načteno: {len(patterns)} grids.")
print("-------------------")


def horizontal_line(pattern):
    """Hledání horizontální linie. Procházení každé možné
    linie zrcadlení"""
    rows = len(pattern)
    
    for i in range(rows - 1):
        top = pattern[:i+1][::-1] # Zrcadlená část (horní)
        bottom = pattern[i+1:]  # Spodní část
        
        # Kontrola, zda se shodují (top == bottom)
        if top[:len(bottom)] == bottom[:len(top)]:
            return i + 1  # Vrací číslo řádku zrcadlení
        
    return None  # Vrací None pokud nenajde shodu


def vertical_line(pattern):
    """Hledání vertikální línie. Procházení každé možné línie zrcadlení."""
    cols = len(pattern[0])

    for i in range(cols - 1):
        left = [row[:i+1][::-1] for row in pattern]  # Zrcadlená část (levá)
        right = [row[i+1:] for row in pattern]  # Pravá část
        
        # Kontrola, zda se shodují (left == right)
        if all(left[j][:len(right[j])] == right[j][:len(left[j])] for j in range(len(pattern))):
            return i + 1  # Vracíme číslo sloupce, kde je zrcadlení

    return None  # Vrací None pokud nenajde shodu


def calculation(patterns):
    """Finální výpočet skóre dle horizontálních a vertikálních linií."""
    total_score = 0
    
    for pattern in patterns:
        horizontal = horizontal_line(pattern)
        vertical = vertical_line(pattern)
        
        if horizontal:
            total_score += 100 * horizontal  # 100 x číslo řádku
        if vertical:
            total_score += vertical  # Počítá se jako číslo sloupku
            
    return total_score

# Výpočet výsledku
patterns = load_data("day13/input_data.txt")
score = calculation(patterns)
print(f"Celkový výpočet P1: {score}")


# ---PART TWO---


def new_mirror(pattern, original_mirror, is_horizontal=True):
    """
    Změna každého znaku a nalezení nového zrcadlení.
    original_mirror - původní linie, která bude ignorována!
    is_horizontal - "True" hledá horizontální, "False" hledá vertikální
    """
    for i in range(len(pattern)):
        for j in range(len(pattern[0])):
            new_pattern = [list(row) for row in pattern]
            new_pattern[i][j] = "#" if pattern[i][j] == "." else "."  # Přehození znaku
            new_pattern = ["".join(row) for row in new_pattern]  # Převedení zpět do stringu
            
            # Hledání nového zrcadlení
            if is_horizontal:
                new_mirror = horizontal_line(new_pattern)
            else:
                new_mirror = vertical_line(new_pattern)
                
            # Vrácení nové linie (jiné než původní)
            if new_mirror and new_mirror != original_mirror:
                return new_mirror
            
    return None  # Pokud nenajde novou linii


def calculation_part2(patterns):
    """Nový výpočet pro part 2. Po kompetním přeskládání patternů."""
    total_score = 0

    for pattern in patterns:
        original_h = horizontal_line(pattern)
        original_v = vertical_line(pattern)

        new_h = new_mirror(pattern, original_h, is_horizontal=True)
        new_v = new_mirror(pattern, original_v, is_horizontal=False)

        if new_h:
            total_score += 100 * new_h
        if new_v:
            total_score += new_v

    return total_score

# Spočítáme skóre pro Part 2
patterns = load_data("day13/input_data.txt")
score_part2 = calculation_part2(patterns)
print(f"Celkový výpočet P2: {score_part2}")
