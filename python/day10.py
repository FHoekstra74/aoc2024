with open("../input/day10.txt", "r", encoding="utf-8") as filehandle:
    aocinput = list(line.rstrip() for line in filehandle)
map, start = {}, []
for y, line in enumerate(aocinput):
    for x, c in enumerate(line):
        map[(x, y)] = int(c)
        if int(c) == 0:
            start.append((x, y))

def cals(distinct):
    result = 0
    for sp in start:
        points, i = [sp], 1
        while i < 10:
            next = []
            for p in points:
                for v in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    n = (p[0] + v[0], p[1] + v[1])
                    if n in map and map[n] == i:
                        if distinct or n not in next:
                            next.append(n)
            points = next
            i += 1
        result += len(next)
    return result

print(cals(False))
print(cals(True))
