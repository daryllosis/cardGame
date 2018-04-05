import random

class Card:
    def __init__(self, num, suit):
        self.num = num
        self.suit = suit

    def __repr__(self):
        return "{} of {}".format(self.num, self.suit)

class Deck:
    def __init__(self):
        self.deck = []
        for suite in ['Hearts', 'Diamonds', 'Spades', 'Clubs']:
            for num in ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']:
                self.deck.append(Card(num, suite))

        # #shuffles the deck    
        # random.shuffle(deck)
        random.shuffle(self.deck)
        self.displayDeck()

    def displayDeck(self):
        for card in self.deck:
            print(card)
    
    def dealCard(self, player):
        for x in range(0,5):
            player.hand.append(self.deck.pop())

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def printPlayerCard(self):
        print("name: ", self.name)
        
deck1 = Deck()
player1 = Player("Daryll")
player1.printPlayerCard()
deck1.dealCard(player1)
print("daryll's hand", player1.hand)