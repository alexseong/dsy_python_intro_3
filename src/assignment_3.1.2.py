# This 8 lines are provided for you

#largest = None
#smallest = None
numbers = list()

def compute_min_max(numbers):
    largest = None
    smallest = None

    for num in numbers:
        if largest is None or inum > largest:
            largest = inum

        if smallest is None or inum < smallest:
            smallest = inum

    print("Maximum is", largest)
    print("Minimum is", smallest)


while True:
    num = input("Enter a number: ")
    if num == "done" : break

    try:
        number = int(number)
        numbers.append(num)

    except:
        print('Invalid Number')

compute_min_max(numbers)
