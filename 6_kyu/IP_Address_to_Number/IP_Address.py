from ipaddress import IPv4Address


def ip_num():
    ip = '192.168.1.1'
    num = 167772160
    ip_to_num(ip)
    num_to_ip(num)


def ip_to_num(ip):
    number = IPv4Address(ip)
    return int(number)


def num_to_ip(num):
    addr = IPv4Address(num)
    return str(addr)


ip_num()
