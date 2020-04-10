import socket

class Client:
    def __init__(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.playerNum = None


    def connect(self):
        TCP_IP = '192.168.1.218'
        TCP_PORT = 60001
        BUFFER_SIZE = 1024
        MESSAGE = "Connection Request"
        self.s.connect((TCP_IP, TCP_PORT))
        self.s.send(MESSAGE.encode())
        data = self.s.recv(BUFFER_SIZE)
        self.playerNum = int(data)
        print("Connected to server")
        print("You are player: ", self.playerNum)

    def run(self):
        BUFFER_SIZE = 1024
        while True:
            data = self.s.recv(BUFFER_SIZE)

            if (data.decode() == "Shutdown"):
                print("Server closed connection... stopping.")
                self.s.close()

            state = data.decode().split(",")
            print("Your hand: ")
            print("--------------------")
            for value in state:
                if value[0:2] == "h:":
                    print(value[2:])
                if value[0:2] == "c:":
                    break
            print("")
            print("Clock: ")
            print("--------------------")
            for value in state:
                if value[0:2] == "c:":
                    print(value[2:])



        self.s.close()

if __name__ == "__main__":
    client = Client()
    client.connect()
    client.run()
