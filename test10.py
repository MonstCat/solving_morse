data = open('output_all_ver3.txt', 'r')
output = open('output_all_ver4.txt', 'x')
for i in data:
    if i[:-1].endswith(('эют', 'ний', 'дей', 'дио', 'ухо', 'лей', 'евт', 'лют', 'иют', 'атт', 'рий', 'еум', 'еий', 'бам', 'сам', 'еют', 'рсо', 'ией', 'иум', 'лум', 'есо', 'фий', 'еей', 'эей')):
        print(i[:-1], file=output)
data.close()
output.close()
