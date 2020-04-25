"""
this file simulates a deck of playing cards

"""
import random

class CardDeck:

    def __init__(self):
        self.cards = '123456789JQKA'
        self.suits = ['Clubs', 'Spades', 'Hearts', 'Diamonds']


    def drawACard(self):
        randomCard = random.randint(0, 12)
        randomSuit = random.randint(0, 3)
        draw = (self.cards[randomCard], self.suits[randomSuit])
        print(draw)
        return draw

class Hand:

    def __init__(self):
        self.hand = []

    def __str__(self):
        for card in self.hand:
            print(card)

    def discard(self, item):
        try:
            self.hand.remove(item)
        except:
            print("You don't have that card...")

    def showHand(self):
        for card in self.hand:
            print(card[0] + ' of ' + card[1])

    def keepCard(self, item):
        self.hand.append(item)

if __name__=="__main__":
    cards = CardDeck()
    myHand = Hand()
    startGame = input("Draw a card? (y/n) ")
    while startGame is 'y':
        myTurn = cards.drawACard()
        myHand.keepCard(myTurn)
        myHand.showHand()
        myHand.discard(myTurn)
        startGame = input("Draw another? (y/n) ")
