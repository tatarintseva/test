__author__ = 'otatarintseva'


def fib(n):
    if n < 1:
        return
    if n <= 2:
        return 1

    pred = 1
    predpred = 1
    current = None

    for _ in range(2, n):
        current = pred + predpred
        predpred, pred = pred, current

    return current

if __name__ == '__main__':
    print fib(10)
