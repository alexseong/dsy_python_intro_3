fname = input('Enter a file name:')

try:
    fhand = open(fname)

    keyStr = 'X-DSPAM-Confidence'
    s_confidence = 0
    s_conf_count = 0

    for line in fhand:
        if line.startswith(keyStr):
            s_conf_count = s_conf_count + 1
            confidence = line.split(' ')[1].rstrip()
            confidence = float(confidence)
            s_confidence = s_confidence + confidence

    average = s_confidence / s_conf_count
    print('Average spam confidence:', average)
except:
    print("The file dosen't exist.")
