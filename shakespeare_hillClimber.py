"""
Author: Cameron Redovian

'Given enough time, a monkey pressing random keys on a typewriter could reproduce the works of Shakespeare'

This program modifies the naive shakespeare.py solution to find a solution quickly. In this imaginary scenario any character in the correct position is kept.
"""

import random

def generate():
    for letter in range(len(sentence)):
        if not sticky[letter]:
            guess = random.randint(0,26)
            sentence[letter] = charsList[guess]
    return sentence

def compare(test, goal):
    match = 0
    for letter in range(length):
        if test[letter] == goal[letter]:
            match += 1
            sticky[letter] = True
    return match/length


found = False; count = 0; best_score = 0
goal = 'methinks it is like a weasel'
length = len(goal)

charsList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']
sticky = [False for char in range(length)]
sentence = ['' for char in range(length)]

while not found:
    count += 1
    test = generate()
    score = compare(test, goal)
    answer = ""
    for char in test:
        answer += char
    if score > best_score:
        best_score = score
    if count % 5 == 0:
        print("\nGuess:", answer)
        print("Score:", best_score)
    if score == 1:
        print("\n\n******************")
        print("Randomly generated Shakespeare: '%s'" % str(answer))
        print("Attempts:", count)
        found = True
