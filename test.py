def convert_base(num, to_base=10, from_base=10):
    if isinstance(num, str):
        n = int(num, from_base)
    else:
        n = int(num)
    alphabet = "0123456789"
    if n < to_base:
        return alphabet[n]
    else:
        return convert_base(n // to_base, to_base) + alphabet[n % to_base]


output = open('output_variants.txt', 'w')
for i in range(390624, 5820766091346740722657):
    number = list(convert_base(i, to_base=5, from_base=10))
    if '0' in number:
        continue
    number = [int(digit) for digit in number]
    if sum(number) == 32:
        print(number, file=output)
output.close()
