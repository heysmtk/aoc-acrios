# ---PART ONE---
# Input data
times = [54, 81, 70, 88]
distances = [446, 1292, 1035, 1007]

# Prázdný list pro budoucí data výsledků
race_results = []

# For cyklus, který mi "zipuje" times a distance hodnoty
for time, distance in zip(times, distances):
    chance_of_wins = 0  # Připravená prázdná hodnota

    # Výpočet času a vzádelnosti pro každý závod 
    for active_time in range(1, time):
        speed = active_time
        post_distance = speed * (time - active_time)

        # Porovnání ujeté vzdálenosti vs. dané vzdálenosti
        if post_distance > distance:
            chance_of_wins += 1  # Pokud je větší než požadovaná, navýší se o jednu jednotku
    
    # Uložení iterace (závodu) do listu
    race_results.append(chance_of_wins)

print(race_results)