def domain_name(url):
    url = url.replace('http://', '').replace('www.', '').replace('https://', '')
    return url.split('.')[0]


domain_name("google")
