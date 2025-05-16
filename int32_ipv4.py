def int32_to_ip(int32):
    bin = format(int32, 'b')
    n = 32 - len(bin)
    bin = '0' * n + bin
    first, second, third, fourth = bin[0:8], bin[8:16], bin[16:24],bin[24:]
    octs = [first,second,third,fourth]
    res = []
    for oct in octs:
        if oct != '':
            res.append(int(oct,2))
        else:
            res.append(0)
    return f'{res[0]}.{res[1]}.{res[2]}.{res[3]}' 



def main():
    num = 1365783016
    print(int32_to_ip(num))

if __name__ == "__main__":
    main()
