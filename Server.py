import socket
import _thread as thread
import time
from flask import Flask, Response, request, send_from_directory, render_template

BUFFER_SIZE=1024
gameState = None
gamePlayers = None
connectedPlayers = 0
shutdown = False
showPlayerHands = True

links = {
    "2 Clubs": "2C.png",
    "2 Diamonds": "2D.png",
    "2 Hearts": "2H.png",
    "2 Spades": "2S.png",
    "3 Clubs": "3C.png",
    "3 Diamonds": "3D.png",
    "3 Hearts": "3H.png",
    "3 Spades": "3S.png",
    "4 Clubs": "4C.png",
    "4 Diamonds": "4D.png",
    "4 Hearts": "4H.png",
    "4 Spades": "4S.png",
    "5 Clubs": "5C.png",
    "5 Diamonds": "5D.png",
    "5 Hearts": "5H.png",
    "5 Spades": "5S.png",
    "6 Clubs": "6C.png",
    "6 Diamonds": "6D.png",
    "6 Hearts": "6H.png",
    "6 Spades": "6S.png",
    "7 Clubs": "7C.png",
    "7 Diamonds": "7D.png",
    "7 Hearts": "7H.png",
    "7 Spades": "7S.png",
    "8 Clubs": "8C.png",
    "8 Diamonds": "8D.png",
    "8 Hearts": "8H.png",
    "8 Spades": "8S.png",
    "9 Clubs": "9C.png",
    "9 Diamonds": "9D.png",
    "9 Hearts": "9H.png",
    "9 Spades": "9S.png",
    "10 Clubs": "0C.png",
    "10 Diamonds": "0D.png",
    "10 Hearts": "0H.png",
    "10 Spades": "0S.png",
    "Jack Clubs": "JC.png",
    "Jack Diamonds": "JD.png",
    "Jack Hearts": "JH.png",
    "Jack Spades": "JS.png",
    "Queen Clubs": "QC.png",
    "Queen Diamonds": "QD.png",
    "Queen Hearts": "QH.png",
    "Queen Spades": "QS.png",
    "King Clubs": "KC.png",
    "King Diamonds": "KD.png",
    "King Hearts": "KH.png",
    "King Spades": "KS.png",
    "Ace Clubs": "AC.png",
    "Ace Diamonds": "AD.png",
    "Ace Hearts": "AH.png",
    "Ace Spades": "AS.png",
}

def getImageLink(card):
    global links
    lookup = str(card.value) + " " + str(card.suit)
    print(lookup)
    if lookup in links:
        return "/static/img/" + links[lookup]
    return None

def cardsToImages(cards):
    images = []
    for card in cards:
        images.append(getImageLink(card))
    return images

def getPlayerState(playerNumber): # comma separated state in string
    global gameState
    global gamePlayers
    global showPlayerHands
    str_state = ""
    playerHand = gamePlayers[playerNumber].cards
    if showPlayerHands:
        for card in playerHand:
            str_state = str_state + "h:" + str(card.getValue()) + " of " + str(card.getSuit()) + ","
    else:
        for card in playerHand:
            str_state = str_state + "h:Hidden of Hidden,"

    for card in gameState:
        str_state = str_state + "c:" + str(card.getValue()) + " of " + str(card.getSuit()) + ","
    return str_state

def on_new_client(clientsocket, addr):
    global connectedPlayers
    global shutdown
    # Assign player number to thread
    msg_recv = clientsocket.recv(BUFFER_SIZE)
    if msg_recv.decode() == "Connection Request":
        playerNumber = connectedPlayers
        msg_out = str(playerNumber).encode()
        clientsocket.send(msg_out)
        connectedPlayers += 1
    else:
        return 1
    # Run Game Loop
    while True:
        playerState = getPlayerState(playerNumber)
        msg_out = str(playerState).encode()
        clientsocket.send(msg_out)
        time.sleep(1)
        if(shutdown):
            msg = "Shutdown"
            msg_out = str(msg).encode()
            clientsocket.send(msg_out)
            time.sleep(1)
            break
    clientsocket.close()

class Server:
    def __init__(self):
        TCP_IP = '0.0.0.0'
        TCP_PORT = 60003
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind((TCP_IP, TCP_PORT))
        self.s.listen(5)
        # Start web server
        self.t = thread.start_new_thread(run_flask, ())
        print("Started server")

    def run(self):
        while True:
            conn, addr = self.s.accept()
            print ('Got new connection from address:', addr)
            thread.start_new_thread(on_new_client,(conn,addr))
        conn.close()

    def setGameState(self, state):
        global gameState
        gameState = state

    def setPlayers(self, players):
        global gamePlayers
        gamePlayers = players

    def sendShutdown(self):
        global shutdown
        shutdown = True

    def showPlayerHands(self, show):
        global showPlayerHands
        showPlayerHands = show


app = Flask(__name__, static_url_path='/static')
@app.route('/Player1', methods=['GET'])
def serve_player1():
    # hand = gamePlayers[0].cards
    hand = cardsToImages(gamePlayers[0].cards)
    print(hand)
    clock = gameState
    if showPlayerHands:
        return render_template('hand.html', hand=hand, )
    else:
        return render_template('clock.html', clock=clock)

@app.route('/Player2', methods=['GET'])
def serve_player2():
    hand = gamePlayers[1].cards
    clock = gameState
    if showPlayerHands:
        return render_template('hand.html', hand=hand, )
    else:
        return render_template('clock.html', clock=clock)

@app.route('/Player3', methods=['GET'])
def serve_player3():
    hand = gamePlayers[2].cards
    clock = gameState
    if showPlayerHands:
        return render_template('hand.html', hand=hand, )
    else:
        return render_template('clock.html', clock=clock)

@app.route('/Player4', methods=['GET'])
def serve_player4():
    hand = gamePlayers[3].cards
    clock = gameState
    if showPlayerHands:
        return render_template('hand.html', hand=hand, )
    else:
        return render_template('clock.html', clock=clock)

@app.route('/Player5', methods=['GET'])
def serve_player5():
    hand = gamePlayers[4].cards
    clock = gameState
    if showPlayerHands:
        return render_template('hand.html', hand=hand, )
    else:
        return render_template('clock.html', clock=clock)

@app.route('/Player6', methods=['GET'])
def serve_player6():
    hand = gamePlayers[5].cards
    clock = gameState
    if showPlayerHands:
        return render_template('hand.html', hand=hand, )
    else:
        return render_template('clock.html', clock=clock)

@app.route('/', methods=['GET'])
def serve_player():
    hand = gamePlayers[0].cards
    clock = gameState
    if showPlayerHands:
        return render_template('hand.html', hand=hand, )
    else:
        return render_template('clock.html', clock=clock)

def run_flask():
    addr = '0.0.0.0'
    app.run(host=addr, port=60000, debug=False, threaded=True)
