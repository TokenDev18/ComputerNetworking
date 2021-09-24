# import socket module
from socket import *
import http.server
# In order to terminate the program
import sys


def webServer(port=13331):
  serverSocket = socket(AF_INET, SOCK_STREAM)
  #Prepare a server socket
  serverSocket.bind(("", port))
  serverSocket.listen()

  while True:
    #Establish the connection
    connectionSocket, addr = serverSocket.accept()
    try:

      try:
        message = connectionSocket.recv(2048)
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()

        #Send one HTTP header line into socket.
        #Fill in start
        #http_message = "HTTP/1.1 200 OK GET /helloworld.html"
        connectionSocket.sendall(b"HEAD / HTTP/1.1 \r\nGET /helloworld.htlm \r\nAccept: text/html\r\n\r\n")
        connectionSocket.recv(1024)
        #connectionSocket.sendall(file_message.encode())
        #connectionSocket.send('HTTP/1.1 200 OK\r\n'.encode())
        #Fill in end

        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
          connectionSocket.send(outputdata[i].encode())

        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
      except IOError:
        # Send response message for file not found (404)
        connectionSocket.send("404 File Not Found".encode())

        #Close client socket
        connectionSocket.close()

    except (ConnectionResetError, BrokenPipeError):
      pass

  serverSocket.close()
  sys.exit()  # Terminate the program after sending the corresponding data

if __name__ == "__main__":

  webServer(13331)
