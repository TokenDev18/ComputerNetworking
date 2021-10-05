from socket import *
import ssl
import base64
import sys

def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My Message"
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope

    # Create socket called clientSocket and establish a TCP connection with mailserver and port
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((mailserver,port))
    recv = clientSocket.recv(1024).decode()
    #print(recv)

    if recv[:3] != '220':
        #print('220 reply not received from server.')

    # Send HELO command and print server response.
    heloCommand = "HELO 127.0.0.1\r\n"
    clientSocket.send(heloCommand.encode())
    helo_recv = clientSocket.recv(1024).decode()
    #print(helo_recv)
    if helo_recv[:3] != '250':
        print('250 reply not received from server.')

    # Send MAIL FROM command and print server response.
    # Fill in start
    mailFrom = "MAIL FROM: at5201@nyu.edu\r\n"
    clientSocket.send(mailFrom.encode())
    mailFrom_recv = clientSocket.recv(1024)
    mailFrom_recv = mailFrom_recv.decode()
    #print(mailFrom_recv)
    # Fill in end

    # Send RCPT TO command and print server response.
    # Fill in start
    rcptTo = "RCPT TO: athealthylife14@gmail.com\r\n"
    clientSocket.send(rcptTo.encode())
    recptTo_recv = clientSocket.recv(1024)
    recptTo_recv = recptTo_recv.decode()
    #print(recptTo_recv)
    # Fill in end

    # Send DATA command and print server response.
    # Fill in start
    data = "DATA\r\n"
    clientSocket.send(data.encode())
    clientSocket.send(msg.encode())
    clientSocket.send(endmsg.encode())
    data_recv = clientSocket.recv(1024)
    data_recv = data_recv.decode()
    #print(data_recv)
    # Fill in end

    # Send QUIT command and get server response.
    # Fill in start
    quit_msg = "QUIT\r\n"
    clientSocket.send(quit_msg.encode())
    quit_recv = clientSocket.recv(1024)
    #print("Quit Response: " + quit_recv.decode())
    clientSocket.close()
    # Fill in end


if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')
