import socket
import _thread as thread
import time

BUFFER_SIZE=1024
gameState = None
gamePlayers = None
connectedPlayers = 0
shutdown = False
showPlayerHands = True

def getPlayerState(playerNumber): # comma separated state in string
    global gameState
    global gamePlayers
    global showPlaerHands
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
        TCP_PORT = 60001
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind((TCP_IP, TCP_PORT))
        self.s.listen(5)
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
