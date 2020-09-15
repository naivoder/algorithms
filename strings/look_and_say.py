"""
this file implements the 'look and say' algorithm in which the nth digit of a sequence is the verbal description of the number preceding it
if x[n - 1] = 211, then x[n] = 1221 ('one 2 and two 1s' -> 1 2 2 1)

"""

from itertools import groupby

def look_and_say(n):
    def next_number(s):
        result, i = [], 0
        while i < len(s):
            # count repeated digits
            count = 1
            while i + 1 < len(s) and s[i] == s[i + 1]:
                count += 1
                i += 1
            # 'four 1s' -> '4' + '1'
            result.append(str(count) + s[i])
            i += 1
        return ''.join(result)

    s = '1'
    for _ in range(1, n):
        s = next_number(s)
    return s

# pythonic solution
def lns(n):
    s = '1'
    for _ in range(n - 1):
        s = ''.join(str(len(list(group))) + key for key, group in groupby(s))
    return s

if __name__=="__main__":
    print("###---Look and Say---###")
    for i in range(5):
        print('N=%s:   %s' % (i, lns(i + 1)))
    print('N=15: ', look_and_say(15))