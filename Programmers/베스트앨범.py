# def solution(genres, plays):
#     best = {}
#
#     for g in genres:
#         idx = genres.index(g)
#         play = plays[idx]
#
#         best[g] = {}
#         best[g][idx] = play
#
#     print(f"best: {best}")
#
#     total_plays = {}
#     for gen in best:
#         total_plays[gen] = 0
#         for song in gen:
#             total_plays[gen] += best[gen][song]
#
#
#     print(f"ntotal plays: {total_plays}")

def solution(genres, plays):
    dict_genre = {}
    for i in range(len(genres)):
        if genres[i] not in dict_genre:
            dict_genre[genres[i]] = {}
        dict_genre[genres[i]][i] = plays[i]
    print(dict_genre)

    total_plays = {}
    for genre in dict_genre:
        total_plays[genre] = 0
        for song in dict_genre[genre]:
            total_plays[genre] += dict_genre[genre][song]

    total_plays = sorted(total_plays.items(), key=(lambda x: x[1]), reverse=True)
    print(total_plays)

    best = []
    for p in total_plays:
        sorted_dict = sorted(dict_genre[p[0]].items(), key=lambda x:x[1], reverse=True)
        if len(dict_genre[p[0]]) >= 2:
            sorted_dict = sorted_dict[:2]

        for s in sorted_dict:
            best.append(s[0])

    print(best)


solution(["classic", "pop", "classic", "classic", "pop"],
         [500, 600, 150, 800, 2500])
