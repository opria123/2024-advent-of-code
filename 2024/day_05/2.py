f = open("2024/day_05/input.txt", "r")
lines = f.read().splitlines()

rules = []
changes = []

for line in lines:
    if '|' in line:
        rules.append([int(line.split('|')[0]), int(line.split('|')[1])])
    elif ',' in line:
        changes.append(list(map(int, line.split(','))))

invalidChanges = []

for change in changes:
    isValid = True
    for rule in rules:
        try:
            if change.index(rule[0]) > change.index(rule[1]):
                isValid = False
        except:
            notFound=True;
    if not isValid:
        invalidChanges.append(change)

total = 0

for change in invalidChanges:
    isValid = False
    while not isValid:
        for rule in rules:
            try:
                if change.index(rule[0]) > change.index(rule[1]):
                    change[change.index(rule[0])], change[change.index(rule[1])] = change[change.index(rule[1])], change[change.index(rule[0])]
            except:
                notFound=True;
        tmpIsValid = True

        for rule in rules:
            try:
                if change.index(rule[0]) > change.index(rule[1]):
                    tmpIsValid = False
            except:
                notFound=True;
        isValid = tmpIsValid
    if isValid:
        total += change[int((len(change) - 1) / 2)]

print(total)