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
print(f"Celkový výpočet je: {score}")