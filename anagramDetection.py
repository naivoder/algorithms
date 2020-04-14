"""
Author: Cameron Redovian

This file contains various solutions to a simple anagram detection problem with various time/space requirements.
The three solutions defined initially are from "Problem Solving with Algorithms and Data Structures" by Miller and Ranum.
The fourth solution is my revision of the O(n) solution to include an initial length comparison which would produce an O(1) runtime for many False inputs.
The revised solution also accounts for any possible Unicode entries, rather than only lowercase english alphabet characters.

The solutions are benchmarked so that runtime comparisons can be easily seen.
It is particularly interesting to note that for average word sizes the naive solutions outperform the linear checks (logically consistent with xy graph of runtimes).

"""
import time

#O (n2) solution - "Checking Off"
def anagram_solution1(s1, s2):
    start = time.time()
    a_list = list(s2)
    pos1 = 0
    still_ok = True

    while pos1 < len(s1) and still_ok:
        pos2 = 0
        found = False
        while pos2 < len(a_list) and not found:
            if s1[pos1] == a_list[pos2]:
                found = True
            else:
                pos2 = pos2 + 1

        if found:
            a_list[pos2] = None
        else:
            still_ok = False

        pos1 = pos1 + 1

    runtime = time.time() - start
    return still_ok, runtime

print(anagram_solution1('abcdefghijklmnopqrstuvwxyz', 'zyxwvutsrqponmlkjihgfedcba'))

# O(nlogn) solution - "Sort and Compare"
def anagram_solution2(s1, s2):
    start = time.time()
    a_list1 = list(s1)
    a_list2 = list(s2)

    a_list1.sort()
    a_list2.sort()

    pos = 0
    matches = True

    while pos < len(s1) and matches:
        if a_list1[pos] == a_list2[pos]:
            pos = pos + 1
        else:
            matches = False

    runtime = time.time() - start
    return matches, runtime

print(anagram_solution2('abcdefghijklmnopqrstuvwxyz', 'zyxwvutsrqponmlkjihgfedcba'))

# O(n) solution - "Count and Compare"
def anagram_solution3(s1, s2):
    start = time.time()
    c1 = [0] * 26
    c2 = [0] * 26

    for i in range(len(s1)):
        pos = ord(s1[i]) - ord('a')
        c1[pos] = c1[pos] + 1

    for i in range(len(s2)):
        pos = ord(s2[i]) - ord('a')
        c2[pos] = c2[pos] + 1

    j = 0
    still_ok = True

    while j < 26 and still_ok:
        if c1[j] == c2[j]:
            j = j + 1
        else:
            still_ok = False

    runtime = time.time() - start
    return still_ok, runtime

print(anagram_solution3('abcdefghijklmnopqrstuvwxyz', 'zyxwvutsrqponmlkjihgfedcba'))

# O(n) solution with O(1) pre-check and
def hashCompare(string1, string2):
    start = time.time()
    try:
        len(string2) == len(string1)
    except:
        runtime = time.time() - start
        return False, runtime

    hash1 = [0 for i in range(128)]
    hash2 = [0 for i in range(128)]

    for char in string1:
        value = ord(char)
        hash1[value] += 1
    for char in string2:
        value = ord(char)
        hash2[value] += 1

    if hash1 != hash2:
        runtime = time.time() - start
        return False, runtime

    runtime = time.time() - start
    return True, runtime

print(hashCompare('abcde', 'abcd'))
print(hashCompare('super', 'purse'))
print(hashCompare('house', 'mouse'))
print(hashCompare('lose!', '!sole'))
print(hashCompare('abcdefghijklmnopqrstuvwxyz', 'zyxwvutsrqponmlkjihgfedcba'))
