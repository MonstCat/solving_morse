data = open('output_all_ver3.txt', 'r')
variants = {'збй'}
for i in data:
    variants.add(i[-4:-1])
print(variants)
