# # # # # # # # # # # # # # # # # # # # # # # # # # SONIYA NITIN KADAM EECE7374 # # # # # # # # # # # # # # # # # # # # # # # 

# According to the assignment we have to create a client that will connect to the server which will give our client mathematical equations.
# After receiving these mathematical equations, our client is supposed to answer a few. After this the server will send a secret key, 
# which will display as output in the terminal. To start this, first we need to establish connection between our client and the server, for
# this we have used the information of the ip address and the port number. We will make the TCP connection using the command SOCK_STREAM and
# for IPv4 F_INET. Once the connection is established, the client will send a message to the server saying "EECE7374 INTR 002818960" which 
# includes the charecters that will be recognized by the server , once thee server identifies that the client message contents it will start 
# sending math equations, these equations will be identified by the client by splitting the message received into parts & if that message 
# includes "EECE7374 EXPR 'equation'" which will be solved by the client and the client will send back "EECE7374 RSLT 'result'". 
# This message will again be decoded by the server, the server will send multiple such equations till the server is satisfied and will send
# the secret key. If the server is not able to identify the message or if the answer of the equation is wrong the server will reply "EECE7374 fail"
# After the process is completed the SECRET KEY WILL BE VISIBLE IN THE OUTPUT .
# SECRET KEY RECEIVED AS : EECE7374 SUCC 3723963d252be94010f1c16f01f0fdb05772de22d62d0c8bd1d50b472838cd4b

from operator import truediv #Here we are importing the module called opertor , which comtaines mathametical operations 
import socket # Socket module provides functions for creating and managing network sockets 

server_hostname = '129.10.132.64' #Using the server IP Address for later use
default_server_port = 5206 #Cummunicationg with port number 5208 of the server for later use
NU_ID = 'ADD YOUR ID HERE'# Assigning NEU ID to variable name NU_ID for later use (PLEASE ADD YOUR OWN ID)
list_of_operations = [ '+' , '-' , '*' , '/' ] #Assigning multiple operations to be done in a List

clientSocket = socket.socket( socket.AF_INET , socket.SOCK_STREAM ) # Here AF_INET is to connect with a IPv4 address & SOCK_STREAM to for a TCP connection
clientSocket.connect((server_hostname, default_server_port)) # Defining the host name and port number to establish the connection


message = "EECE7374 INTR - YOUR ID HERE" #First message that the client will send to the server (PLEASE ADD YOUR OWN ID)
clientSocket.send(message.encode( 'utf-8')) #Sending the message to the server & to the proper port number

while True:
    expression = clientSocket.recv(2046).decode()# While receiving message from the server , if it is an expression 
    list_of_tokens = expression.split() # split the expression
    if list_of_tokens[0] == "EECE7374" and list_of_tokens[1] == "EXPR": #check if the 0 indexed part has EECE7374 & 1 indexed part has EXPR
        Exp1 = int(list_of_tokens[2]) # if yes , the 2 indexed number will be an integer saved in variable EXP1
        operand = list_of_tokens[3] # the 3 indexed is a operand which will be selected from the list of operations
        Exp2 = int(list_of_tokens[4]) # the 4 indexed number will be an integer saved in variable EXP2
        if operand == '+': # if the peration is '+'  
            expected_solution = Exp1 + Exp2 # then add Exp1 & Exp2
        elif operand == '-': # if the peration is '-' 
            expected_solution = Exp1 - Exp2 # then subtract Exp1 & Exp2
        elif operand == '*': # if the peration is '*' 
            expected_solution = Exp1 * Exp2 # then multiply Exp1 & Exp2
        elif operand == '/': # if the peration is '/' 
            expected_solution = Exp1 / Exp2 # then divide Exp1 & Exp2
        second_message = "EECE7374 RSLT " + str(expected_solution) # Message to be sent in th eformat EECE7374 RSLT 'solution'
        clientSocket.send(second_message.encode('utf-8')) # Sending the message to the server
    elif list_of_tokens[0] == "EECE7374" and list_of_tokens[1] == "SUCC": #if the received message has EECE7374 in index 0 and SUCC in index 1
        print(expression) #Print the message with the secreate key
        break # breake

clientSocket.close() # close the established connection


       

    



        

         

    
    

    







               
        
               
            

               

               
    

