import sys

word = sys.stdin.readline().rstrip()
c_len = len(word)

for i in range(len(word)):
    if word[i] == '=':
        c_len -= 1
    elif word[i] == '-':
        c_len -= 1


    if i < (len(word) - 2):
        if word[i] == 'l' and word[i+1] == 'j':
        c_len -= 1
        elif word[i] == 'n' and word[i+1] == 'j':
            c_len -= 1
            
    if i < (len(word) - 3):
        if word[i] == 'd' and word[i+1] == 'z' and word[i+2] == '=':
            c_len -= 1

print(c_len)
