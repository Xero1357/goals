total_multiplier = 0

with open("data.txt", "r") as file:
    for dataset in file:
        group1, group2 = dataset.strip().split("|")
        overlapping_data = set(group1.split()) & set(group2.split())
        count_items = len(overlapping_data)
        multiplier = 1 * (2 ** (count_items - 1)) if count_items > 0 else 0 
        total_multiplier += multiplier

print(total_multiplier)
