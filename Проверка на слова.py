output = open('output.txt', 'r')
all = []
point = input()
while point != '/':
    all.append(point)
    point = input()
print(all)
for line in output:
    lenq = line
lenq = lenq.split('\t')
for i in all:
    for q in lenq:
        if q.startswith(i.lower()):
            print(i)
            break
output.close()
