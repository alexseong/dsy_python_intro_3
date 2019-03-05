total = 0
count = 0
numbers = list()

while True:
    number = input('Enter a number: ')

    if number == 'done':
        break

    try:
        number = int(number)
        numbers.append(number)
    except:
        print('Invalid Number')

for number in numbers:
    #write your code here
    count += 1 ## count = count + 1
    total += number ## total = total + number

average = total / count

print(total, count, average)
