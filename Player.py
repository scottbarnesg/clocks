class Player:
    def __init__(self, number, name):
        self.number = number
        self.name = name
        self.cards = []

    def giveCard(self, card):
        self.cards.append(card)

    def printHand(self):
        for card in self.cards:
            print(card.getValue(), " of ", card.getSuit())

    def getName(self):
        return self.name

    def getNumber(self):
        return self.number

    
