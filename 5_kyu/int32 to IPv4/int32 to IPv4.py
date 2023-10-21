# https://www.codewars.com/kata/52e88b39ffb6ac53a400022e


from ipaddress import IPv4Address


def int32_to_ip(int32):
    return str(IPv4Address(int32))


int32_to_ip(2154959208)
