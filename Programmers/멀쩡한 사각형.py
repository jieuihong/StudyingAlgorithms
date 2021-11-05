from math import gcd


def solution(w,h):
    g = gcd(w, h)
    return  w * h - (w + h - g)
