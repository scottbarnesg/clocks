import random

class CardDeck:
    def __init__(self):
      self.suits = ['Hearts','Diamonds','Spades','Clubs']
      self.values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
      self.cards = []
      self.generateDeck()
      self.shuffle()

    def generateDeck(self):
        for suit in self.suits:
            for value in self.values:
                self.cards.append(Card(suit, value))

    def printDeck(self):
        # print("Deck size: ", len(self.cards))
        for card in self.cards:
            print(card.value, " of ", card.suit)

    def shuffle(self):
        newDeck = []
        cardsLeft = len(self.cards)
        while(cardsLeft > 0):
            index = random.randint(0,cardsLeft-1)
            newDeck.append(self.cards[index])
            del self.cards[index]
            cardsLeft = len(self.cards)

        self.cards = newDeck

    def drawCard(self):
        card = self.cards[0]
        del self.cards[0]
        return card


class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def getSuit(self):
        return self.suit

    def getValue(self):
        return self.value
