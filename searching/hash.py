"""
this file contains various hashing functions. it is often very useful that the hash table contain a prime number of slots so that collision resolution can be efficiently handled via open addressing with linear (or quadratic) probing. an alternate solution to collision resolution is 'chaining' multiple values to single slots (this can be efficiently done with a dictionary)

"""
def stringHash(word, slots):
    sum = 0
    for index in range(len(word)):
        sum += ord(word[index])
    return sum % slots

def weightedStringHash(word, slots):
    sum = 0
    for index in range(len(word)):
        sum += ord(word[index]) * index
    return sum % slots

def moduloHash(number, slots):
    return number % slots

def foldingHash(number, slots):
    split = str(number)
    split = [int(char) for char in split]
    right = sum(split[:len(split) // 2])
    left = sum(split[len(split) // 2 + 1:])
    return (right + left) % slots

def midSquareHash(number, slots):
    square = str(pow(number, 2))
    square = int(square[1:-1])
    return square % slots

if __name__=="__main__":
    print("###---String Hash---###")
    print("String hash of 'cameron':", stringHash('cameron', 11))
    print("String hash of 'carolina':", stringHash('carolina', 11))
    print("###---Weighted String Hash---###")
    print("String hash of 'cameron':", weightedStringHash('cameron', 11))
    print("String hash of 'carolina':", weightedStringHash('carolina', 11))
    print("###---Modulo Hash---###")
    print("Modulo hash of '5869043':", moduloHash(5869043, 11))
    print("Modulo hash of '9856425':", moduloHash(9856425, 11))
    print("###---Folding Hash---###")
    print("Folding hash of '97845638':", foldingHash(97845638, 11))
    print("Folding hash of '16458513':", foldingHash(16458513, 11))
    print("###---Mid-Square Hash---###")
    print("Mid-Square hash of '62':", midSquareHash(62, 11))
    print("Mid-Square hash of '91':", midSquareHash(91, 11))
