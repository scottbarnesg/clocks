import socket

class Client:
    def __init__(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.playerNum = None


    def connect(self):
        TCP_IP = '127.0.0.1'
        TCP_PORT = 60001
        BUFFER_SIZE = 1024
        MESSAGE = input("Connection Request")
        self.s.connect((TCP_IP, TCP_PORT))
        self.s.send(MESSAGE)
        data = self.s.recv(BUFFER_SIZE)
        self.playerNum = int(data)
        print("Connected to server")
        print("You are player: ", self.playerNum)

    def run(self):
        BUFFER_SIZE = 1024
        while True:
            data = self.s.revc(BUFFER_SIZE)
            print(data)


        self.s.close()

if __name__ == "__main__":
    client = Client()
    client.connect()
    client.run()