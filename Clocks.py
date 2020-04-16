from Card import CardDeck, Card
from Player import Player
from Server import Server
import time
import _thread as thread

class Clocks:
    def __init__(self, player_names, cards_per_player):
        self.server = Server()
        self.shownClock = [Card('Hidden','Hidden') for i in range(12)]
        self.createPlayers(player_names)
        self.setup(cards_per_player)
        self.currentTime = 0

    def setup(self, cards_per_player):
        self.deck = CardDeck()
        self.deck.shuffle()
        self.createClock()
        self.dealHands(cards_per_player)
        self.server.setGameState(self.shownClock)
        self.server.setPlayers(self.players)
        # self.server.run() # TODO: Put in its own thread
        thread.start_new_thread(self.server.run,())

    def createPlayers(self, player_names):
        self.players = []
        counter = 0
        for name in player_names:
            player = Player(counter, name)
            self.players.append(player)

    def createClock(self):
        self.clock = []
        for i in range(12):
            card = self.deck.drawCard()
            self.clock.append(card)

    def revealNextClock(self):
        self.shownClock[self.currentTime] = self.clock[self.currentTime]
        self.currentTime += 1

    def printShownClock(self):
        print("Current clock")
        for card in self.shownClock:
            print(card.getValue(), " of ", card.getSuit())

    def getShownClock(self):
        return self.shownClock

    def dealHands(self, cards_per_player):
        for player in self.players:
            for i in range(cards_per_player):
                card = self.deck.drawCard()
                player.giveCard(card)
            print("Player Name: ", player.getName())
            player.printHand()


if __name__ == '__main__':
    player_names = ['Scott', 'Tyler', 'Zamin', 'Tom', 'Sam', 'Tylers Brother']
    cards_per_player = 5
    clocks = Clocks(player_names, cards_per_player)
    print("Waiting for clients to connect...")
    preGameDuration = 180
    counter = 0
    while(counter < preGameDuration):
        counter += 1
        clocks.server.setTimer(preGameDuration-counter)
        time.sleep(1)

    clocks.server.showPlayerHands(False)
    interCardDelay = 60
    for i in range(12):
        clocks.revealNextClock()
        counter = 0
        userInput = "no"
        while(userInput != "next"):
            print("Type 'next' to go to the next card: ")
            userInput = Input()


    # Everyone says their cards:
    print("Everyone says their cards")
    time.sleep(120)
    clocks.server.showPlayerHands(True)
    time.sleep(30)
    # Shut down clients
    print("Ending game...")
    clocks.server.sendShutdown()
    time.sleep(10)
    print("Done.")
