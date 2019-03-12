def compute_count(str, char):
    count = 0

    for letter in str:
        if letter == char:
            count = count + 1

    print(count)

str = input('Enter a string: ').strip()
char = input('Enter a character: ').strip()

compute_count(str, char)
