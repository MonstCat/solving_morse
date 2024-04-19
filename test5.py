import math
output = open('output_variants_test_5.txt', 'x')
start = []
for i in range(33):
    for q in range(17):
        for p in range(11):
            for m in range(9):
                if i + 2 * q + 3 * p + 4 * m == 27:
                    start.append([i, q, p, m])
for i in start:
    numbers = [0 for numb in range(sum(i))]
    positions = [k + 1 for k in range(sum(i))]
    if i[0] != 0:
        ones = [number for number in range(1, i[0] + 1)]
        for q in range(math.factorial(sum(i)) // math.factorial(sum(i) - i[0]) // math.factorial(i[0])):
            numbers_one = []
            positions_one = []
            if q != 0:
                if ones[-1] != sum(i):
                    ones[-1] += 1
                else:
                    transfer = False
                    for x in range(1, i[0] + 1):
                        if ones[-1 * x] != sum(i) - x + 1:
                            ones[-1 * x] += 1
                            for t in range(1, x):
                                ones[-1 * t] = ones[-1 * x] + x - t
                                transfer = True
                            if transfer:
                                break
            for p in numbers:
                numbers_one.append(p)
            for p in positions:
                positions_one.append(p)
            for p in ones:
                numbers_one[positions_one[p - 1] - 1] = 1
            for p in ones:
                positions_one[p - 1] = 0
            while 0 in positions_one:
                positions_one.remove(0)
            if i[1] != 0:
                twos = [number for number in range(1, i[1] + 1)]
                for e in range(math.factorial(sum(i[1:])) // math.factorial(sum(i[1:]) - i[1]) // math.factorial(i[1])):
                    numbers_two = []
                    positions_two = []
                    if e != 0:
                        if twos[-1] != sum(i[1:]):
                            twos[-1] += 1
                        else:
                            transfer = False
                            for x in range(1, i[1] + 1):
                                if twos[-1 * x] != sum(i[1:]) - x + 1:
                                    twos[-1 * x] += 1
                                    for t in range(1, x):
                                        twos[-1 * t] = twos[-1 * x] + x - t
                                        transfer = True
                                    if transfer:
                                        break
                    for r in numbers_one:
                        numbers_two.append(r)
                    for r in positions_one:
                        positions_two.append(r)
                    for r in twos:
                        numbers_two[positions_two[r - 1] - 1] = 2
                    for r in twos:
                        positions_two[r - 1] = 0
                    while 0 in positions_two:
                        positions_two.remove(0)
                    if i[2] != 0:
                        threes = [number for number in range(1, i[2] + 1)]
                        for v in range(
                                math.factorial(sum(i[2:])) // math.factorial(sum(i[2:]) - i[2]) // math.factorial(i[2])):
                            numbers_three = []
                            positions_three = []
                            if v != 0:
                                if threes[-1] != sum(i[2:]):
                                    threes[-1] += 1
                                else:
                                    transfer = False
                                    for x in range(1, i[2] + 1):
                                        if threes[-1 * x] != sum(i[2:]) - x + 1:
                                            threes[-1 * x] += 1
                                            for t in range(1, x):
                                                threes[-1 * t] = threes[-1 * x] + x - t
                                                transfer = True
                                            if transfer:
                                                break
                            for g in numbers_two:
                                numbers_three.append(g)
                            for g in positions_two:
                                positions_three.append(g)
                            for g in threes:
                                numbers_three[positions_three[g - 1] - 1] = 3
                            for g in threes:
                                positions_three[g - 1] = 0
                            while 0 in positions_three:
                                positions_three.remove(0)
                            if i[3] != 0:
                                numbers_four = []
                                positions_four = []
                                fours = [number for number in range(1, i[3] + 1)]
                                for h in numbers_three:
                                    numbers_four.append(h)
                                for h in positions_three:
                                    positions_four.append(h)
                                for h in fours:
                                    numbers_four[positions_four[h - 1] - 1] = 4
                                print(numbers_four, file=output)
                            else:
                                print(numbers_three, file=output)
                    else:
                        if i[3] != 0:
                            numbers_four = []
                            positions_four = []
                            fours = [number for number in range(1, i[3] + 1)]
                            for h in numbers_two:
                                numbers_four.append(h)
                            for h in positions_two:
                                positions_four.append(h)
                            for h in fours:
                                numbers_four[positions_four[h - 1] - 1] = 4
                            print(numbers_four, file=output)
                        else:
                            print(numbers_two, file=output)
            else:
                if i[2] != 0:
                    threes = [number for number in range(1, i[2] + 1)]
                    for v in range(math.factorial(sum(i[2:])) // math.factorial(sum(i[2:]) - i[2]) // math.factorial(i[2])):
                        numbers_three = []
                        positions_three = []
                        if v != 0:
                            if threes[-1] != sum(i[2:]):
                                threes[-1] += 1
                            else:
                                transfer = False
                                for x in range(1, i[2] + 1):
                                    if threes[-1 * x] != sum(i[2:]) - x + 1:
                                        threes[-1 * x] += 1
                                        for t in range(1, x):
                                            threes[-1 * t] = threes[-1 * x] + x - t
                                            transfer = True
                                        if transfer:
                                            break
                        for g in numbers_one:
                            numbers_three.append(g)
                        for g in positions_one:
                            positions_three.append(g)
                        for g in threes:
                            numbers_three[positions_three[g - 1] - 1] = 3
                        for g in threes:
                            positions_three[g - 1] = 0
                        while 0 in positions_three:
                            positions_three.remove(0)
                        if i[3] != 0:
                            numbers_four = []
                            positions_four = []
                            fours = [number for number in range(1, i[3] + 1)]
                            for h in numbers_three:
                                numbers_four.append(h)
                            for h in positions_three:
                                positions_four.append(h)
                            for h in fours:
                                numbers_four[positions_four[h - 1] - 1] = 4
                            print(numbers_four, file=output)
                        else:
                            print(numbers_three, file=output)
                else:
                    if i[3] != 0:
                        numbers_four = []
                        positions_four = []
                        fours = [number for number in range(1, i[3] + 1)]
                        for h in numbers_one:
                            numbers_four.append(h)
                        for h in positions_one:
                            positions_four.append(h)
                        for h in fours:
                            numbers_four[positions_four[h - 1] - 1] = 4
                        print(numbers_four, file=output)
                    else:
                        print(numbers_one, file=output)
    else:
        if i[1] != 0:
            twos = [number for number in range(1, i[1] + 1)]
            for e in range(math.factorial(sum(i[1:])) // math.factorial(sum(i[1:]) - i[1]) // math.factorial(i[1])):
                numbers_two = []
                positions_two = []
                if e != 0:
                    if twos[-1] != sum(i[1:]):
                        twos[-1] += 1
                    else:
                        transfer = False
                        for x in range(1, i[1] + 1):
                            if twos[-1 * x] != sum(i[1:]) - x + 1:
                                twos[-1 * x] += 1
                                for t in range(1, x):
                                    twos[-1 * t] = twos[-1 * x] + x - t
                                    transfer = True
                                if transfer:
                                    break
                for r in numbers:
                    numbers_two.append(r)
                for r in positions:
                    positions_two.append(r)
                for r in twos:
                    numbers_two[positions_two[r - 1] - 1] = 2
                for r in twos:
                    positions_two[r - 1] = 0
                while 0 in positions_two:
                    positions_two.remove(0)
                if i[2] != 0:
                    threes = [number for number in range(1, i[2] + 1)]
                    for v in range(math.factorial(sum(i[2:])) // math.factorial(sum(i[2:]) - i[2]) // math.factorial(i[2])):
                        numbers_three = []
                        positions_three = []
                        if v != 0:
                            if threes[-1] != sum(i[2:]):
                                threes[-1] += 1
                            else:
                                transfer = False
                                for x in range(1, i[2] + 1):
                                    if threes[-1 * x] != sum(i[2:]) - x + 1:
                                        threes[-1 * x] += 1
                                        for t in range(1, x):
                                            threes[-1 * t] = threes[-1 * x] + x - t
                                            transfer = True
                                        if transfer:
                                            break
                        for g in numbers_two:
                            numbers_three.append(g)
                        for g in positions_two:
                            positions_three.append(g)
                        for g in threes:
                            numbers_three[positions_three[g - 1] - 1] = 3
                        for g in threes:
                            positions_three[g - 1] = 0
                        while 0 in positions_three:
                            positions_three.remove(0)
                        if i[3] != 0:
                            numbers_four = []
                            positions_four = []
                            fours = [number for number in range(1, i[3] + 1)]
                            for h in numbers_three:
                                numbers_four.append(h)
                            for h in positions_three:
                                positions_four.append(h)
                            for h in fours:
                                numbers_four[positions_four[h - 1] - 1] = 4
                            print(numbers_four, file=output)
                        else:
                            print(numbers_three, file=output)
                else:
                    if i[3] != 0:
                        numbers_four = []
                        positions_four = []
                        fours = [number for number in range(1, i[3] + 1)]
                        for h in numbers_two:
                            numbers_four.append(h)
                        for h in positions_two:
                            positions_four.append(h)
                        for h in fours:
                            numbers_four[positions_four[h - 1] - 1] = 4
                        print(numbers_four, file=output)
                    else:
                        print(numbers_two, file=output)
        else:
            if i[2] != 0:
                threes = [number for number in range(1, i[2] + 1)]
                for v in range(math.factorial(sum(i[2:])) // math.factorial(sum(i[2:]) - i[2]) // math.factorial(i[2])):
                    numbers_three = []
                    positions_three = []
                    if v != 0:
                        if threes[-1] != sum(i[2:]):
                            threes[-1] += 1
                        else:
                            transfer = False
                            for x in range(1, i[2] + 1):
                                if threes[-1 * x] != sum(i[2:]) - x + 1:
                                    threes[-1 * x] += 1
                                    for t in range(1, x):
                                        threes[-1 * t] = threes[-1 * x] + x - t
                                        transfer = True
                                    if transfer:
                                        break
                    for g in numbers:
                        numbers_three.append(g)
                    for g in positions:
                        positions_three.append(g)
                    for g in threes:
                        numbers_three[positions_three[g - 1] - 1] = 3
                    for g in threes:
                        positions_three[g - 1] = 0
                    while 0 in positions_three:
                        positions_three.remove(0)
                    if i[3] != 0:
                        numbers_four = []
                        positions_four = []
                        fours = [number for number in range(1, i[3] + 1)]
                        for h in numbers_three:
                            numbers_four.append(h)
                        for h in positions_three:
                            positions_four.append(h)
                        for h in fours:
                            numbers_four[positions_four[h - 1] - 1] = 4
                        print(numbers_four, file=output)
                    else:
                        print(numbers_three, file=output)
            else:
                if i[3] != 0:
                    numbers_four = []
                    positions_four = []
                    fours = [number for number in range(1, i[3] + 1)]
                    for h in numbers:
                        numbers_four.append(h)
                    for h in positions:
                        positions_four.append(h)
                    for h in fours:
                        numbers_four[positions_four[h - 1] - 1] = 4
                    print(numbers_four, file=output)
                else:
                    print(numbers, file=output)
    print(i)
output.close()
