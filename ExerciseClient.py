from socket import *
import time

# Vi angiver en server host og en server port
serverName = "127.0.0.1"
serverPort = 12000

# Vi opretter en TCP client socket og connecter denne
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))


while True:
    print("Choose three operations. Random, Add or Subtract. Choose two numbers.")
    print("Format as: <Operation num1 num2>. Type Over to quit.")

    # Vi tager et brugerindput og sender dette til serversocketen.
    calculation = input("Input calculation:")

    if(calculation == "Over"):
        break

    clientSocket.send(calculation.encode())

    answer = clientSocket.recv(1024)

    print("The answer is:", answer.decode())
    time.sleep(1)




