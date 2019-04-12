import optparse
import threading
import logging

from socket import \
    (socket,
     AF_INET,
     SOCK_STREAM,
     gethostbyname,
     gethostbyaddr,
     setdefaulttimeout
     )

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def connScan(tgtHost, tgtPort):
    """
    :param tgtHost:
    :param tgtPort:
    :return:
    """
    try:
        connSkt = socket(AF_INET, SOCK_STREAM)
        connSkt.connect((tgtHost, tgtPort))
        connSkt.send(b'ViolentPython\r\n')
        results = connSkt.recv(100)
        logger.info('[+]%d/tcp open'% tgtPort)
        logger.info('[+] ' + str(results))
        connSkt.close()
    except:
        # logger.info('[-]%d/tcp closed'% tgtPort)
        pass

def portScan(tgtHost, tgtPorts):
    """
    :param tgtHost:
    :param tgtPorts:
    :return:
    """

    try:
        tgtIP = gethostbyname(tgtHost)
    except:
        logger.info("[-] Cannot resolve '%s': Unknown host" % tgtHost)
        return
    try:
        tgtName = gethostbyaddr(tgtIP)
        logger.info('\n[+] Scan Results for: ' + tgtName[0])
    except:
        logger.info('\n[+] Scan Results for: ' + tgtIP)
    setdefaulttimeout(1)
    for tgtPort in tgtPorts:
        # logger.info('Scanning port {}'.format(tgtPort))
        thread = threading.Thread(target=connScan, args=(tgtHost, int(tgtPort)))
        thread.start()


def main():
    parser = optparse.OptionParser("usage %prog -H <target host> -p <target port>")
    parser.add_option('-H', dest='tgtHost', type='string', help='specify target host')
    parser.add_option('-p', dest='tgtPort', type='string', help='specify target port[s] separated by comma')
    (options, args) = parser.parse_args()
    tgtHost = options.tgtHost
    tgtPorts = str(options.tgtPort).split(',')
    if (tgtHost == None) | (tgtPorts[0] == None):
        logger.info('[-] You must specify a target host and port[s].')
        exit(0)
    portScan(tgtHost, tgtPorts)


if __name__ == '__main__':
    # main()
    # tgtHost = "192.168.56.20"
    # tgtPorts = [x for x in range(1, 65535)]
    # portScan(tgtHost, tgtPorts)
    print(__name__)
    print(__file__)
    import os
    print(os.path.abspath(__name__))
    print(os.path.abspath(__file__))



