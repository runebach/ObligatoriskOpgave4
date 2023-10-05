from socket import *

serverName = "localhost"
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
print("use format [operand] [operation] [operand] including spaces. "
      + "Example: 2 + 2")

calculation = input("Input calculation:")
clientSocket.send(calculation.encode())
