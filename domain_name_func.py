def domain_name(url):
    """Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:"""
    return url.split('//')[-1].split('www.')[-1].split('.')[0]


assert domain_name("http://google.com") == "google"
assert domain_name("http://google.co.jp") == "google"
assert domain_name("www.xakep.ru") == "xakep"
assert domain_name("https://youtube.com") == "youtube"
