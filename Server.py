import socket
import _thread as thread
import time

BUFFER_SIZE=1024
gameState = None
gamePlayers = None
connectedPlayers = 0

def on_new_client(self, clientsocket, addr):
    # Assign player number to thread
    msg_recv = clientsocket.recv(BUFFER_SIZE)
    if msg_recv == "Connection Request":
        playerNumber = connectedPlayers
        msg_out = raw_input(playerNumber)
        connectedPlayers += 1
    # Run Game Loop
    while True:
        # msg_recv = clientsocket.recv(BUFFER_SIZE)
        playerHand = gamePlayers[playerNumber]
        playerState = [playerHand, gameState]
        msg_out = raw_input(playerState)
        clientsocket.send(msg)
        time.sleep(1)
    clientsocket.close()

class Server:
    def __init__(self):
        TCP_IP = '0.0.0.0'
        TCP_PORT = 60001
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind((TCP_IP, TCP_PORT))
        self.s.listen(5)

    def run(self):
        while True:
            conn, addr = self.s.accept()
            print ('Got new connection from address:', addr)
            thread.start_new_thread(on_new_client,(conn,addr))
        conn.close()

    def setGameState(self, state):
        gameState = state

    def setPlayers(self, players):
        gamePlayers = players
