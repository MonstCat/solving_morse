output = open('output_variants_2.txt', 'w')
for i in range(2, 32):
    number = [1 for l in range(i)]
    for q in range(1, 4 ** i):
        reached = False
        while not reached:
            for p in range(-1, i * -1 - 1, -1):
                if number[p] != 4:
                    number[p] += 1
                    reached = True
                    break
                else:
                    number[p] = 1
        if sum(number) == 32:
            print(number, file=output)
    print(i)
output.close()
