data = open('output_all_ver4.txt', 'r')
output = open('output_all_ver5.txt', 'x')
for i in data:
    if not i[:-1].startswith(('межет', 'мифт', 'мифмж', 'мифзй')):
        print(i[:-1], file=output)
data.close()
output.close()
