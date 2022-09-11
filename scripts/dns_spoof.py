# pip install https://github.com/johnteslade/python-netfilterqueue/archive/refs/heads/update-cython-code.zip

# import needed library
import netfilterqueue


def process_packet(packet):
    print(packet)


queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()
