str = input('Enter a string: ')
str = str.strip()

idx = len(str)

while True:
    idx = idx - 1
    if idx < 0:
        break

    print(str[idx])
