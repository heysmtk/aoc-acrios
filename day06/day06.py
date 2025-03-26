# ---PART ONE---

# Input data
times = [54, 81, 70, 88]
distances = [446, 1292, 1035, 1007]

# Funkce, která vypočítá čas a vzálenost k závodům (pro part 1 i 2)
def race_calc(times, distances):
    results = []  # Připravený list pro výsledky
    
    for time, distance in zip(times, distances):
        chance_of_wins = 0  # Připravená prázdná proměnná pro přičítání možností na "výhru"

        # Výpočet času a vzádelnosti pro každý závod 
        for active_time in range(1, time):
            speed = active_time
            post_distance = speed * (time - active_time)

            # Porovnání ujeté vzdálenosti vs. dané vzdálenosti
            if post_distance > distance:
                chance_of_wins += 1 
                
        # Uložení iterace (závodu) do listu
        results.append(chance_of_wins)
    return results

# Uložení funkce s argumenty do proměnné k vypsání
race_results = race_calc(times, distances)
print(f"Part One Results: {race_results}")


# ---PART TWO---

# Převedení původních listů s daty na stringy a spojení dohromady v listu (čili výstup je opět list)
times_full = [int("".join(map(str, times)))]
distances_full = [int("".join(map(str, distances)))]

# Změna parametrů pro již existující funkci pro výpočet partu 2
full_race_result = race_calc(times_full, distances_full)
print(f"Part Two Results: {full_race_result}")