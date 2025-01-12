f = open("2024/day_07/input.txt", "r")
lines = f.read().splitlines()

def is_valid(val: int, nums: list[int]) -> bool:
    if len(nums) == 1:
        return val == nums[0]

    if val % nums[-1] == 0 and is_valid(val // nums[-1], nums[:-1]):
        return True
    if val - nums[-1] >= 0 and is_valid(val - nums[-1], nums[:-1]):
        return True

    return False



calibrations = []

for line in lines:
    calibrations.append(
        {
            "total": int(line.split(":")[0]),
            "values": list(map(int, line.split(":")[1].split(" ")[1:]))
        }
    )

total = 0
for calibration in calibrations:
    if is_valid(calibration["total"], calibration["values"]):
        total += calibration["total"]

print(total)