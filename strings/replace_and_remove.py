"""
this file implements an algorithm that computes the resulting array given a set of rules in O(n) time and space
in this example the rules will be:
  1) replace all 'a' with 'dd'
  2) delete all 'b'

"""

def replace_and_remove(word, size):
    write_id, a_count = 0, 0
    # forward pass: count 'a', delete 'b'
    for i in range(size):
        if word[i] != 'b':
            word[write_id] = word[i]
            write_id += 1
        if word[i] == 'a':
            a_count += 1
    #backwards pass: replace 'a' with 'dd' from end
    current = write_id - 1
    write_id += a_count - 1
    final_size = write_id + 1
    while current >= 0:
        if word[current] == 'a':
            word[write_id - 1:write_id + 1] = 'dd'
            write_id -= 2
        else:
            word[write_id] = word[current]
            write_id -= 1
        current -= 1
    return ''.join(word), final_size

if __name__=="__main__":
    test_word = list('acaa   ')
    print('Test word:', test_word)
    print(replace_and_remove(test_word, size=4))