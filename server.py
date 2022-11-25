#!/usr/bin/python3

import socket #importing socet module from python standard library

serversocketobject = socket.socket(socket.AF_INET, socket.soc_STREAM) #created an (serversocketobject) object which is calling the socket function and we specified the socket family and socket type

host = socket.gethostbyname() #giving this value to host
port = 444 #specifying this value to port

serversocketobject.bind((host, port)) #using the server socket object and binding the address (host and port) to the socket 

serversocketobject.listen(3) #setting up a TCP listener which would listn to connections up to a maximum of three

while True: #while all of this is true
    clientsocket, address = serversocketobject.accept() #we've created two more, we're saying that the clientsocket(another object) and the address are equal to the serversocket.accept, that's going to be the information that we accepted from the client 

    print("receive connection from " % str(address)) #we're gonna print received connection from and we specify that we want to convert tje address into a string

    message = 'Hello! Thank you for connecting to the server' + "\r\n" #specifying what out message is going to be
    clientsocket.send(message) #using the send function to send our message so that the client knows he's successfully connected to the server

    clientsocket.close() #closing the socket