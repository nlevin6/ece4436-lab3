from socket import *
import timeit
import datetime


def main():
    clientSocket = socket(AF_INET, SOCK_DGRAM)
    serverName = 'localhost'
    serverPort = 12000
    seq = 1

    while seq <= 10:
        current_time = datetime.datetime.now().strftime("%H:%M:%S.%f")
        message = f'Ping -- {seq} -- {current_time}'

        sentTime = timeit.default_timer()

        try:
            clientSocket.settimeout(1)
            clientSocket.sendto(message.encode(), (serverName, serverPort))
            modifiedMessage, serverAddress = clientSocket.recvfrom(1024)

            receivedTime = timeit.default_timer()
            rtt = (receivedTime - sentTime) * 1000000
            print(modifiedMessage.decode())
            print('RTT: ' + str(rtt) + ' microseconds')
        except timeout:
            print('Request timed out')

        seq += 1

    clientSocket.close()


if __name__ == '__main__':
    main()
