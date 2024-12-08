import itertools

with open("../input/day8.txt", "r", encoding="utf-8") as filehandle:
    aocinput = list(line.rstrip() for line in filehandle)
map, antennas, a, b = {}, {}, set(), set()
for y, line in enumerate(aocinput):
    for x, c in enumerate(line):
        map[(x, y)] = c
        if c != ".":
            b.add((x,y))
            if c not in antennas:
                antennas[c] = set()
            antennas[c].add((x, y))
for antenna in antennas.values():
    for combination in list(itertools.combinations(antenna, 2)):
        x1, y1 = combination[0]
        x2, y2 = combination[1]
        p0, p1, i = combination[0], combination[1], 1
        while p0 in map or p1 in map:
            p0 = (x1 + ((x1 - x2) * i), y1 + ((y1 - y2) * i))
            if p0 in map:
                if i == 1:
                    a.add(p0)
                b.add(p0)
            p1 = (x2 + ((x2 - x1) * i), y2 + ((y2 - y1) * i))
            if p1 in map:
                if i == 1:
                    a.add(p1)
                b.add(p1)
            i += 1
print(len(a))
print(len(b))
