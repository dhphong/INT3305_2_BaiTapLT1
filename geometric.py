import math

def prob(n, p):
    return p * ((1 - p) ** (n - 1))


def infoMeasure(n, p):
    return -math.log2(prob(n, p))


def sumProb(N, p):
    """
    Tổng xác suất trong phân bố geometric là tổng xác suất của tất cả các sysbols từ 1 đến vô cùng.
    Khi ta tăng giá trị của tham số N dần, ta thấy hàm trả về giá trị dần tiến tới 1.
    Khi N đủ lớn thì, giá trị hàm trả về sẽ xấp xỉ bằng giá trị của Tổng xác suất trong phân bố geometric.
    """
    res = 0
    for i in range(1, N + 1):
        res += prob(i, p)
    return res


def approxEntropy(N, p):
    """
    Entropy trong phân bố geometric được tính bằng tổng giá trị (xác suất * lượng tin) của tất cả các symbols
    từ 1 đến vô cùng. Vì vậy, khi ta tăng giá trị của N lên đủ lớn thì giá trị hàm trả về sẽ xấp xỉ giá trị entropy.
    Qua thực nghiệm, entropy của nguồn geometric với p = 0.5 bằng 2. Cụ thể:
    - Khi N = 1000 => approxEntropy(N, p) = 1.9999999999999998
    """
    res = 0
    for i in range(1, N + 1):
        res += prob(i,p) * infoMeasure(i, p)
    return res

