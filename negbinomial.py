import operator as op
from functools import reduce
import math


def nCk(n, k):
    k = min(k, n - k)
    numer = reduce(op.mul, range(n, n - k, -1), 1)
    denom = reduce(op.mul, range(1, k + 1), 1)
    return numer // denom


def prob(n, p, r):
    return nCk(n + r - 1, n) * (p ** r) * ((1 - p) ** n)


def infoMeasure(n, p, r):
    return -math.log2(prob(n, p, r))


def sumProb(N, p, r):
    res = 0
    for i in range(r, N + 1):
        res += prob(i, p, r)
    return res


def approxEntropy(N, p, r):
    res = 0
    for i in range(r, N + 1):
        res += prob(i, p, r) * infoMeasure(i, p, r)
    return res
