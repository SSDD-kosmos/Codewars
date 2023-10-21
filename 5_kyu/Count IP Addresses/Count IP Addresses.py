# https://www.codewars.com/kata/526989a41034285187000de4/train/python


from ipaddress import IPv4Address


def ips_between(start, end):
    return int(IPv4Address(end)) - int(IPv4Address(start))


ips_between("10.0.0.0", "10.0.0.50")
