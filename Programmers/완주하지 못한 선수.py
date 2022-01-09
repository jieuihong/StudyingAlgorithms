# # 효율성 통과 X
# def solution(participant, completion):
#     i = -1
#     while len(participant) > 1:
#         if participant[i] in completion:
#             p = participant.pop(i)
#             print(completion.pop(completion.index(p)))
#             print(participant)
#         else:
#             i -= 1
#     return participant[0]

# # solve using hash
# def solution(participant, completion):
#     d = {}
#     c, p  = 0, 0
#
#     for i in participant:
#         p += hash(i)
#         d[hash(i)] = i
#
#     for j in completion:
#         c  += hash(j)
#
#     return d[p-c]

# solve using Collection
from collections import Counter


def solution(participant, completion):
    answer = Counter(participant) - Counter(completion)
    print(list(answer.keys())[0])


if __name__ == '__main__':
    solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["marina", "josipa", "nikola", "filipa"])