"""
this file implements an algorithm to reverse the words in a given sentence
to accomplish this in one pass the entire phrase is first reversed, and then each individual word is reversed

"""

# my implementation
def word_reverse(phrase):
    esahp = phrase[::-1]
    reversed_words = ''.join(esahp)
    reversed_words = reversed_words.split(' ')
    corrected_words = [word[::-1] for word in reversed_words]
    sentence = ' '.join(corrected_words)
    return sentence

# EPI algorithm
def reverse_words(phrase):
    def reverse_range(phrase, start, finish):
        while start < finish:
            phrase[start], phrase[finish] = phrase[finish], phrase[start]
            start, finish = start + 1, finish - 1
    # reverse the whole string
    reverse_range(phrase, 0, len(phrase) - 1)
    start = 0
    while True:
        finish = start
        while finish < len(phrase) and phrase[finish] != ' ':
            finish += 1
        if finish == len(phrase):
            break
        # reverse each word
        reverse_range(phrase, start, finish - 1)
        start = finish + 1
    # reverse last word
    reverse_range(phrase, start, len(phrase) - 1)
    return ''.join(phrase)

if __name__=='__main__':
    phrase = ['r', 'a', 'm', ' ', 'i', 's', ' ', 'c', 'o', 's', 't', 'l', 'y']
    print(reverse_words(phrase))
    print(word_reverse(phrase))