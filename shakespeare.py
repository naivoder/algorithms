import random

def generate():
    charsList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']
    sentence = ''
    while len(sentence) < stringLength:
        guess = random.randint(0,26)
        try:
            sentence += charsList[guess]
        except:
            print("Guess:", guess)
    return sentence

def compare(test, goal):
    match = 0
    for letter in range(stringLength):
        if test[letter] == goal[letter]:
            match += 1
    return match/stringLength

found = False; count = 0
goal = 'methinks it is like a weasel'
stringLength = len(goal)
best_score = 0

while not found:
    count += 1
    test = generate()
    score = compare(test, goal)
    if score > best_score:
        best_score = score
    if count % 1000 == 0:
        print("\nGuess:", test)
        print("Score:", best_score)
    if score == 1:
        print("\n\n******************")
        print("Randomly generated Shakespeare:", test)
        print("Attempts:", count)
        found = True
