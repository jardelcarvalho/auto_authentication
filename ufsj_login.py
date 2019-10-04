import urllib.request
import urllib.parse
import re

if __name__ == '__main__':
    url_gen_login = 'http://www.gstatic.com/generate_204'
    url_post_login = 'https://fwctan.ufsj.edu.br:1003/'

    res = urllib.request.urlopen(url_gen_login)
    ct = res.read().decode('utf-8')
    _, s = re.search('fgtauth?', ct).span()
    e, _ = re.search('";</script>', ct).span()
    mgc = ct[s + 1:e]

    print(mgc)