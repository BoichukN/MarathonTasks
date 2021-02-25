# Given number n and two permutations p and q of length n.
# Find a permutation r, such that for every 1 <= i <= n, q[i] = p[r[i]].
# Permutation of length n is an array consisting of distinct numbers from 1 to n in some order.
# Example
#
# Input:
# n = 3, p = [3, 1, 2],  q = [2, 1, 3]
#
# Output:
# r = [3, 2, 1]

def find_permutation(n, p, q):
    r = []
    for i in range(n):
        r.append((p.index(q[i])) + 1)
    return r
