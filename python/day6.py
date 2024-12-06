with open("../input/day6.txt", "r", encoding="utf-8") as filehandle:
    aocinput = list(line.rstrip() for line in filehandle)
map, b, change = {}, 0, {"U": (0, -1, "R"), "D": (0, 1, "L"), "L": (-1, 0, "U"), "R": (1, 0, "D")}
for y, line in enumerate(aocinput):
    for x, c in enumerate(line):
        map[(x, y)] = c
        if c == "^":
            startpoint = (x, y)

stop, visiteda, pos, direction = False, set(), startpoint, "U"
while not stop:
    visiteda.add(pos)
    newpos = (pos[0] + change[direction][0], pos[1] + change[direction][1])
    if newpos in map:
        if map[newpos] == "#":
            direction = change[direction][2]
        else:
            pos = newpos
    else:
        stop = True
print(len(visiteda))
for x, y in visiteda:
    org, map[x, y] = map[x, y], "#"
    stop, visitedb, pos, direction = False, set(), startpoint, "U"
    while not stop:
        if (pos, direction) in visitedb:
            stop = True
            b += 1
        else:
            visitedb.add((pos, direction))
            newpos = (pos[0] + change[direction][0], pos[1] + change[direction][1])
            if newpos in map:
                if map[newpos] == "#":
                    direction = change[direction][2]
                else:
                    pos = newpos
            else:
                stop = True
    map[x, y] = org
print(b)
