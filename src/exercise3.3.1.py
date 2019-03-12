fname = input('Enter a file name:')

try:
    fhand = open(fname)

    for line in fhand:
        print(line)
except:
    print("The file dosen't exist.")
