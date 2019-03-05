largest = None
smallest = None

while True:
    num = input("Enter a number: ")
    if num == "done" : break

    try:
        inum = int(num)

        # Put your code here

    except:
        print("Invalid input")
        continue

print("Maximum is", largest)
print("Minimum is", smallest)
