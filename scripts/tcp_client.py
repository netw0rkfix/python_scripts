#!/home/serveradmin/Desktop/security/DEV/pyhton/environments/bin/ python3
import socket
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

### Setting variable to store arguments
options = get_arguments()


if __name__ == '__main__':
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((options.target, int(options.port)))
        client.send(b"THIS IS SOME TEST DATA")
        response = client.recv(4096)
        print(response)
    except :
        print("[*] Cannot establish connection to th supplied socket")        











