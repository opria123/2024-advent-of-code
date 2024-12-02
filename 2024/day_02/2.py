def is_safe(levels):
    differs = [a - b for a, b in zip(levels, levels[1:])]
    is_monotonic = all(i > 0 for i in differs) or all(i < 0 for i in differs)
    is_in_range = all(0 < abs(i) <= 3 for i in differs)
    if is_monotonic and is_in_range:
        return True
    return False

f = open("2024/day_02/input.txt", "r")
lines = f.read().splitlines()

safeCount = 0

for report in lines:
    levels = [*map(int, report.split())]
    if is_safe(levels):
        safeCount += 1
    else:
        for i in range(len(levels)):
            tolerated_levels = levels[:i] + levels[i + 1 :]
            if is_safe(tolerated_levels):
                safeCount += 1
                break;

print(safeCount)