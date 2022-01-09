import sys

word = sys.stdin.readline().rstrip()
croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in croatia:
    word = word.replace(i, '_')

print(len(word))
# c_len = len(word)
#
# i = 0
# while i < len(word):
#     if word[i] == 'c':
#         if word[i+1] == '-' or word[i+1] == '=':
#             c_len -= 1
#             i += 2
#         else:
#             i += 1
#     elif word[i] == 'd':
#         if word[i+1] == '-':
#             c_len -= 1
#             i += 2
#         elif word[i+1] == 'z' and word[i+2] == '=':
#             c_len -= 2
#             i += 3
#         else:
#             i += 1
#     elif word[i] == 'l' and word[i+1] == 'j':
#         c_len -= 1
#         i += 2
#     elif word[i] == 'n' and word[i+1] == 'j':
#         c_len -= 1
#         i += 2
#     elif word[i] == 's' and word[i+1] == '=':
#         c_len -= 1
#         i += 2
#     elif word[i] == 'z' and word[i+1] == '=':
#         c_len -= 1
#         i += 2
#     else:
#         i += 1
#
# print(c_len)
