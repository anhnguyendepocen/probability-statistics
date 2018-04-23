from math import factorial as fac
from math import pow


'''
Calculate probabilities of a random variable with binomial distribution
'''


def bineq(k, n, p):
    '''
    input
        k - the number of successes in trials
        n - the number of trials
        p - the probability of a success
    returns
        P(X = k)
    '''
    fail_count = n - k
    success_count = fac(n)/(fac(k)*fac(fail_count))
    success_prob = pow(p, k)
    fail_prob = pow(1 - p, fail_count)
    return success_count * success_prob * fail_prob


def binlt(k, n, p):
    # P(X < k)
    return sum(bineq(x, n, p) for x in range(0, k))


def binle(k, n, p):
    # P(X <= k)
    return sum(bineq(x, n, p) for x in range(0, k+1))


def bingt(k, n, p):
    # P(X > k)
    return 1 - binle(k, n, p)


def binge(k, n, p):
    # P(X >= k)
    return 1 - binlt(k, n, p)
