with open("../input/day4.txt", "r", encoding="utf-8") as filehandle:
    aocinput = list(line.rstrip() for line in filehandle)
map, a, b = {}, 0, 0
aocinput.append("." * (len(aocinput[0]) + 2))
aocinput.insert(0, "." * (len(aocinput[0]) + 2))
for y, line in enumerate(aocinput):
    for x, c in enumerate("." + line + "."):
        map[(x, y)] = c

for x, y in [p for p, c in map.items() if c == "X"]:
    for vx, vy in [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]:
        ok = True
        for i, c in enumerate(["M", "A", "S"]):
            if map[(x + (vx * (i + 1)), y + (vy * (i + 1)))] != c:
                ok = False
                break
        if ok:
            a += 1
print(a)

for x, y in [p for p, c in map.items() if c == "A"] :
    ok = True
    for p1, p2 in [((x + 1, y + 1), (x - 1, y - 1)), ((x - 1, y + 1), (x + 1, y - 1))]:
        if not (map[p1] in ["M", "S"] and map[p2] in ["M", "S"] and map[p1] != map[p2]):
            ok = False
            break
    if ok:
        b += 1
print(b)

