"""
this file implements a deck of Uno cards, and is an ongoing project. the intention is to eventually automate the entire game including a production system for the AI 

"""
import random

class Stack:

    def __init__(self):
        self.content = []

    def __str__(self):
        return str(self.content)

    def __len__(self):
        return len(self.content)

    def __contains__(self, item):
        return True if item in self.content else False

    def isEmpty(self):
        return len(self.content) == 0

    def push(self, item):
        self.content.append(item)

    def pull(self):
        return self.content.pop()

    def peek(self):
        return self.content[-1]

    def count(self):
        return len(self.content)

    def show(self):
        copy = self.content[:]
        reverse = ''
        while copy:
            reverse += str(copy.pop())
        return reverse

class UnoDeck:

    def __init__(self):
        self.numbers = '0112233445566778899'
        self.specials = ['skip', 'skip', 'reverse', 'reverse', 'draw 2', 'draw 2']
        self.colors = ['Red', 'Blue', 'Green', 'Yellow']
        self.wilds = ['Wild', 'Wild', 'Wild', 'Wild', 'Wild Draw 4', 'Wild Draw 4','Wild Draw 4', 'Wild Draw 4']
        self.deck = []
        for color in self.colors:
            for number in self.numbers:
                self.deck.append((color, number))
            for special in self.specials:
                self.deck.append((color, special))
        for wild in self.wilds:
            self.deck.append((wild, 0))

    def count(self):
        return len(self.deck)

    def deal(self, playerList, number=7):
        loop = 1
        while loop <= number:
            for player in playerList:
                draw = random.choice(self.deck)
                self.deck.remove(draw)
                player.keepCard(draw)
            loop += 1
        return playerList

    def drawACard(self):
        draw = random.choice(self.deck)
        self.deck.remove(draw)
        return draw

class Hand:

    def __init__(self):
        self.hand = []

    def __str__(self):
        for card in self.hand:
            print(card)

    def count(self):
        return len(self.hand)

    def discard(self, item):
        try:
            self.hand.remove(item)
            discard.push(item)
        except:
            print("You don't have that card...")

    def showHand(self):
        for card in self.hand:
            if not card[1] == 0:
                print(card[0] + " " + card[1])
            else:
                print(card[0])

    def keepCard(self, item):
        self.hand.append(item)

if __name__=="__main__":
    discard = Stack()
    cards = UnoDeck()
    me = Hand()
    ai = Hand()
    [me, ai] = cards.deal([me, ai])
    print("Dealing...")
    print("\nMy hand:")
    print("--------")
    me.showHand()
    print("\nA.I.'s hand:")
    print("------------")
    ai.showHand()
    first_card = cards.drawACard()
    discard.push(first_card)
    print("Top card:", discard.peek())
    while cards.count() > 0:
        draw = input("\nDraw card? (y/n) ")
        if draw == 'y':
            card = cards.drawACard()
            print("You drew:", card)
