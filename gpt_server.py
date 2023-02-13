import socket
import keyboard

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_address = ('169.254.31.87', 5000)
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

# Accept a connection from the client
connection, client_address = sock.accept()
x=15
y=88
n_x_u=0
n_x_d=0
n_y_u=0
n_y_d=0
n_y=0
#data_to_send = str(x)+'*'+str(y)+'#'

while True:
    # Send data to the client
    #data_to_send = input("Enter data to send: ")
    #print(type(data_to_send))
    #data_to_send = str(12,23,34)
    # used try so that if user pressed other than the given key error will not be shown
    
    if not keyboard.is_pressed('q'):
        #print(2)
        n_x_u=1
    elif keyboard.is_pressed('q'):
        if(n_x_u==1):
            x=x+10
            n_x_u=0
            
    if not keyboard.is_pressed('a'):
        #print(2)
        n_x_d=1
    elif keyboard.is_pressed('a'):
        if(n_x_d==1):
            x=x-10
            n_x_d=0

    if not keyboard.is_pressed('w'):
        #print(2)
        n_y_u=1
    elif keyboard.is_pressed('w'):
        if(n_y_u==1):
            y=y+10
            n_y_u=0
            
    if not keyboard.is_pressed('s'):
        #print(2)
        n_y_d=1
    elif keyboard.is_pressed('s'):
        if(n_y_d==1):
            y=y-10
            n_y_d=0

    
    
    data_to_send = str(x)+'*'+str(y)+'#'
    connection.sendall(data_to_send.encode())

# Close the connection
    #connection.close()