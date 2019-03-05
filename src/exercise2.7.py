# Enter your code here. Read input from STDIN. Print output to STDOUT
n = 0
S = raw_input().strip()
SS = raw_input().strip()

for i in range(0, len(S)):
    if S[i:i+len(SS)] == SS:
        n += 1

print (n) 
