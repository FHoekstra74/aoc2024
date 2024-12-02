with open("../input/day2.txt", "r", encoding="utf-8") as filehandle:
    aocinput = [line.rstrip().split() for line in filehandle]


def isok(report):
    report = [int(item) for item in report]
    for i in range(1, len(report)):
        diff = int(report[i]) - int(report[i - 1])
        if (
            abs(diff) not in [1, 2, 3]
            or (diff < 0 and (report[1] - report[0]) > 0)
            or (diff > 0 and (report[1] - report[0]) < 0)
        ):
            return False
    return True


a, b = 0, 0
for line in aocinput:
    if isok(line):
        a += 1
        b += 1
    else:
        for i in range(len(line)):
            newline = line.copy()
            del newline[i]
            if isok(newline):
                b += 1
                break

print("a:", a)
print("b:", b)
