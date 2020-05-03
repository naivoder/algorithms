"""
this file simulates a deck of playing cards

"""
import random

class CardDeck:

    def __init__(self):
        self.numbers = '123456789JQKA'
        self.suits = ['Clubs', 'Spades', 'Hearts', 'Diamonds']
        self.deck = []
        for suit in self.suits:
            for number in self.numbers:
                self.deck.append((number, suit))

    def count(self):
        return len(self.deck)

    def deal(self, playerList, number):
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
        #draw = (self.cards[randomCard], self.suits[randomSuit])
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
    theirHand = Hand()
    [myHand, theirHand] = cards.deal([myHand, theirHand], 3)
    print("Dealing...")
    print("My hand:"); myHand.showHand()
    print("Their hand:"); theirHand.showHand()
    startGame = input("Draw a card? (y/n) ")
    while startGame is 'y':
        myTurn = cards.drawACard()
        myHand.keepCard(myTurn)
        myHand.showHand()
        myHand.discard(myTurn)
        print(cards.count())
        startGame = input("Draw another? (y/n) ")
