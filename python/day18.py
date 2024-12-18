def bfs(graph, start, goal):
    explored = []
    queue = [[start]]
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node not in explored:
            if node in graph:
                for neighbour in graph[node]:
                    new_path = list(path)
                    new_path.append(neighbour)
                    queue.append(new_path)
                    if neighbour == goal:
                        return new_path
                explored.append(node)
    return


with open("../input/day18.txt", "r", encoding="utf-8") as filehandle:
    aocinput = list(line.rstrip() for line in filehandle)

gridsize, grid = 70, []
for cnt, line in enumerate(aocinput):
    grid.append(tuple(int(i) for i in line.split(",")))
    if (cnt == 1023 or cnt > 2900):  # first tests show no path available after 3000 bytes, 2900 still has a path so start checking at 2900.
        graph = {}
        for y in range(gridsize + 1):
            for x in range(gridsize + 1):
                if (x, y) not in grid:
                    pos = []
                    for v in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                        if (
                            x + v[0] <= gridsize
                            and y + v[1] <= gridsize
                            and (x + v[0], y + v[1]) not in grid
                        ):
                            pos.append((x + v[0], y + v[1]))
                    if len(pos) > 0:
                        graph[(x, y)] = pos
        if cnt == 1023:
            print("a:", len(bfs(graph, (0, 0), (gridsize, gridsize))) - 1)
        elif bfs(graph, (0, 0), (gridsize, gridsize)) == None:
            print("b:", line)
            break
        else:
            print(line, " still oke")
