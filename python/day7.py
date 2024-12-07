from itertools import product

with open("../input/day7.txt", "r", encoding="utf-8") as filehandle:
    aocinput = list(line.rstrip() for line in filehandle)
a, b = set(), set()
for line in aocinput:
    test = line.split(":")
    testvalue = int(test[0])
    values = [int(i) for i in test[1].split()]
    for calc in [list(i) for i in product(["+", "*", "||"], repeat=len(values) - 1)]:
        res = values[0]
        for i in range(len(values) - 1):
            if calc[i] == "+":
                res = res + values[i + 1]
            elif calc[i] == "||":
                res = int(str(res) + str(values[i + 1]))
            else:
                res = res * values[i + 1]
        if res == testvalue:
            b.add(testvalue)
            if not ("||" in calc):
                a.add(testvalue)

print(sum(a))
print(sum(b))
