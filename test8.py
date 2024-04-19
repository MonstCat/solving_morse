data = open('output_all_ver2.txt', 'r')
output = open('output_all_ver3.txt', 'x')
for i in data:
    if i.startswith(('мест', 'меже', 'межа', 'межв', 'межп', 'мифт', 'мифм', 'мифг', 'мифз', 'гиен')):
        print(i[:-1], file=output)
