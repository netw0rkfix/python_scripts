#!/home/serveradmin/Desktop/security/DEV/pyhton/environments/bin/ python3

import socket
import threading
import optparse

def get_arguments():
    ### Set a parser object
    parser = optparse.OptionParser()
    ### Define options and their help message
    parser.add_option("-t", "--target", dest="target", help="Type address to listen on (0.0.0.0, 127.0.0.1, 192.168.1.134")
    parser.add_option("-p", "--port", dest="port", help="Listening port number")
    ### Set options enter by the user to variables
    options = parser.parse_args()[0]
    ### Perform verification on user input
    if not options.target:
        parser.error("[*] - Please specify a target ip, use --help for more info")
    elif not options.port:
        parser.error("[*] - Please specify a port number, use --help for more info")       
    ### If no error found, return user input options
    return options


def main(ip,port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((ip, int(port)))
    server.listen(5)
    print(f'[*] Listening on  {ip}:{port}')

    while True:
        client, address = server.accept()
        print(f'[*] Accepted connection from {address[0]}:{address[1]}')
        client_handler = threading.Thread(target=handle_client,  args=(client,))
        client_handler.start()


def handle_client(client_socket):
    with client_socket as sock:
        request = sock.recv(1024)
        print(f'[*] Received: {request.decode("utf-8")}')
        sock.send(b"ACK")



### Find a way to kill the process holding the port when server go down


if __name__ == '__main__':
    options = get_arguments()
    main(options.target, options.port)

