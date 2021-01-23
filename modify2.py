import socket
import math

ClientSocket = socket.socket()
host = '192.168.0.161'
port = 8888

print('Waiting for connection')
try:
    ClientSocket.connect((host, port))
    print('Connected!!')
except socket.error as ex:
    print(str(ex))

Response = ClientSocket.recv(1024).decode()
print(Response)

while True:
    print (' NL - Nasi Lemak \n S - Sate \n NA - Nasi Ayam \n Q - Quit')
    table = input('\nEnter table number : ')
    Input = input('\nOrder your food : ')
    
    if Input == 'NL' :
        option = "NL"
        table = table
        quantity = input('Quantity : ')
        quantity = int(quantity)
        totprice = 5*quantity
        l = option + '.' + str(table) + '.' + str(quantity) + '.' + str(totprice)
        ClientSocket.send(str.encode(l))
    elif Input == 'S':
        option = "S"
        table = table
        quantity = input('Quantity : ')
        quantity = int(quantity)
        totprice = 1*quantity
        s = option + '.' + str(table) + '.' + str(quantity) + '.' + str(totprice)
        ClientSocket.send(str.encode(s))
    elif Input == 'NA':
        option = "NA"
        table = table
        quantity = input('Quantity : ')
        quantity = int(quantity)
        totprice = 6*quantity
        e = option + '.' + str(table) + '.' + str(quantity) + '.' + str(totprice)
        ClientSocket.send(str.encode(e))
    elif Input == "Q":
        option = "Q"
        table = "0"
        quantity = "0"
        totprice = "0"
        f = option + '.' + str(table) + '.' + str(quantity) + '.' + str(totprice)
        ClientSocket.send(str.encode(f))
        print ('Goodbye!! \n')
        ClientSocket.close()
    else :
        print ('Invalid funtion! Try Again \n')
        
    Response = ClientSocket.recv(1024)
    print(Response.decode())

ClientSocket.close()
