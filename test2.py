def convert_base(num, to_base=10, from_base=10):
    # first convert to decimal number
    n = int(num, from_base) if isinstance(num, str) else num
    # now convert decimal to 'to_base' base
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    res = ""
    while n > 0:
        n,m = divmod(n, to_base)
        res += alphabet[m]
    return res[::-1]


print(convert_base(11111111111111111111111111111112, from_base=6, to_base=10))


# 1591732221989280176878388