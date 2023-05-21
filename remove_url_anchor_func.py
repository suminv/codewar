def remove_url_anchor(url):
    """7 kyu Remove anchor from URL"""
    return url.split('#')[0]


assert remove_url_anchor("www.codewars.com/katas/?page=1#about") == "www.codewars.com/katas/?page=1"
