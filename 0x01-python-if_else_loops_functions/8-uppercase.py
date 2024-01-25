def uppercase(str):
    for i in str:
        if (i >= 'a') and (i <= 'z'):
            i = chr(ord(i) - 32)
        print(i, end="")
    print()
