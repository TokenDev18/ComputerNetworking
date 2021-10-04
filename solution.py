from socket import *
import ssl
import base64
import sys

def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
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
    heloCommand = "HELO email-smtp.us-east-2.amazonaws.com\r\n"
    clientSocket.send(heloCommand.encode())
    helo_recv = clientSocket.recv(1024).decode()
    #print(helo_recv)
    if helo_recv[:3] != '250':
        #print('250 reply not received from server.')

    # Send MAIL FROM command and print server response.
    # Fill in start
    mailFrom = "MAIL FROM:<test@test.com>\r\n"
    clientSocket.send(mailFrom.encode())
    mailFrom_recv = clientSocket.recv(1024)
    mailFrom_recv = mailFrom_recv.decode()
    #print(mailFrom_recv)
    # Fill in end

    # Send RCPT TO command and print server response.
    # Fill in start
    rcptTo = "RCPT TO:<test@test.com>\r\n"
    clientSocket.send(mailFrom.encode())
    recptTo_recv = clientSocket.recv(1024)
    recptTo_recv = recptTo_recv.decode()
    #print(recptTo_recv)
    # Fill in end

    # Send DATA command and print server response.
    # Fill in start
    data = "DATA\r\n"
    clientSocket.send(data.encode())
    data_recv = clientSocket.recv(1024)
    data_recv = data_recv.decode()
    #print(data_recv)
    # Fill in end

    # Send message data.
    # Fill in start
    clientSocket.send(msg.encode())
    recv_msg = clientSocket.recv(1024)
    #print("Response after I sent the message to the server: " + recv_msg.decode())
    # Fill in end

    # Message ends with a single period.
    # Fill in start
    clientSocket.send(endmsg.encode())
    end_msg = clientSocket.recv(1024)
    # Fill in end

    # Send QUIT command and get server response.
    # Fill in start
    quit_msg = "QUIT\r\n"
    clientSocket.send(quit_msg.encode())
    quit_recv = clientSocket.recv(1024)
    print(quit_recv.decode())
    clientSocket.close()
    # Fill in end


if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')
