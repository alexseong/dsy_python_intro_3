fname = input('Enter a file name:')

if fname == "na na boo boo":
    print(fname.upper(), "TO YOU - You have been punk'd!")
else:
    try:
        fhand = open(fname)

        keyStr = 'Subject: '
        s_count = 0

        for line in fhand:
            if line.startswith(keyStr):
                s_count = s_count + 1

        print('There were %d subject lines in %s' % (s_count, fname))
    except:
        print("File cannot be opened: ", fname)
