import IN, socket


def mtu_finder(node, port=9999, packet_size=9100):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    s.connect((node, port))
    s.setsockopt(socket.IPPROTO_IP, IN.IP_MTU_DISCOVER, IN.IP_PMTUDISC_DO)
    mtu = None
    try:
        s.send('#'.encode() * packet_size)
    except socket.error:
        option = getattr(IN, 'IP_MTU', 14)
        mtu = s.getsockopt(socket.IPPROTO_IP, option)
    else:
        #mtu = 'MTU => {}!'.format(packet_size + 28)
        mtu = None
    return mtu

print(mtu_finder('216.58.193.142'))

