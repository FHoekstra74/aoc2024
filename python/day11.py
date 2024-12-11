from collections import defaultdict

# aocinput, rocks = "125 17", defaultdict(int)
aocinput, rocks = "30 71441 3784 580926 2 8122942 0 291", defaultdict(int)
for mark in [int(v) for v in aocinput.split()]:
    rocks[mark] = 1
for i in range(75):
    new = defaultdict(int)
    for mark, cnt in rocks.items():
        if mark == 0:
            new[1] += cnt
        elif len(str(mark)) % 2 == 0:
            s = str(mark)
            a, b = s[: len(s) // 2], s[len(s) // 2 :]
            new[int(a)] += cnt
            new[int(b)] += cnt
        else:
            new[mark * 2024] += cnt
    rocks = new
    if i == 24:
        print(sum(rocks.values()))
print(sum(rocks.values()))
