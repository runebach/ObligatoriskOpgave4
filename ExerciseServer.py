from socket import *
import threading

def HandleClient(connectionSocket, address):
    print(address[0])
    communicate = True

    while communicate == True:
        calculation = connectionSocket.recv(1024).decode().strip()
        
        print(calculation)
        response = "Sorry. Please input a proper message"
        if calculation == "close":
            communicate = False
            response = "You have quit the calculator."

        calculation_list = calculation.split()
        operand_1 = calculation_list[0]
        operator = calculation_list[1]
        operand_2 = calculation_list[2]

        num_1 = float(operand_1)
        num_2 = float(operand_2)

        if operator == "+":
            result = num_1 + num_2
        if operator == "-":
            result = num_1 - num_2
        if operator == "*":
            result = num_1 * num_2
        if operator == "/":
            if num_2 == 0:
                result = "Sorry. You cannot divide by 0"
            if num_2 != 0:
                result = num_1 / num_2
        else:
            result = "Invalid input"

        print("Sending result to client")

        output = str(result)
        connectionSocket.send(output.encode())
    connectionSocket.close()

serverPort = 12000
serverHost = "127.0.0.2"
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind((serverHost, serverPort))
serverSocket.listen(1)
print("Server is ready")
while True:
    connectionSocket, addr = serverSocket.accept()
    threading.Thread(target=HandleClient, args=(connectionSocket, addr)).start()

        



