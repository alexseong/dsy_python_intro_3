largest_so_far = None
smallest_so_far = None

while True:
    number = input('Enter a number: ')

    if number == 'done':
        break

    try:
        number = int(number)

        if smallest_so_far is None:
            smallest_so_far = number
        elif number < smallest_so_far:
            smallest_so_far = number

        if largest_so_far is None:
            largest_so_far = number
        elif number > largest_so_far:
            largest_so_far = number

    except:
        print('Invalid Number')

print('The maximum number: ', largest_so_far)
print('The minimum number: ', smallest_so_far)
