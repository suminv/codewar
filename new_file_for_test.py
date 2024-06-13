import time

import requests




def get_status_code(url):
    r = requests.get(url)
    if r.status_code == 200:
        return r.status_code
    else:
        return 'Error'




if __name__ == '__main__':
    url = 'http://www.google.com'
    for _ in range(100):
        time.sleep(0.1)
        status_code = get_status_code(url)
        print(status_code)



