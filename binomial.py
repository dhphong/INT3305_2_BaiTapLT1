import operator as op
from functools import reduce
import math


def nCk(n, k):
    k = min(k, n - k)
    numer = reduce(op.mul, range(n, n - k, -1), 1)
    denom = reduce(op.mul, range(1, k + 1), 1)
    return numer // denom


def prob(n, p, N):
    return nCk(N, n) * (p ** n) * ((1 - p) ** (N - n))


def infoMeasure(n, p, N):
    return -math.log2(prob(n, p, N))


def sumProb(N, p):
    res = 0
    for i in range(0, N + 1):
        res += prob(i, p, N)
    return res


def approxEntropy(N, p):
    res = 0
    for i in range(0, N + 1):
        res += prob(i, p, N) * infoMeasure(i, p, N)
    return res
