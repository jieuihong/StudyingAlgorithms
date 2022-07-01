def solution(lottos, win_nums):
    place = [6, 6, 5, 4, 3, 2, 1]
    cnt_z = lottos.count(0)
    cnt_win = 0

    for n in lottos:
        if n in win_nums:
            cnt_win += 1

    return [place[cnt_win + cnt_z], place[cnt_win]]
