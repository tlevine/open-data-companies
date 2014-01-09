#!/usr/bin/env python3
import requests
from lxml.html import fromstring

def download_roster(l, username, password):
    r = requests.post(
        'https://stat.ethz.ch/mailman/roster/r-sig-geo',
        auth = (username,password))
    return r.text

def companies(raw):
    html = fromstring(raw)


if __name__ == '__main__':
    fn = os.path.join('downloads','r-sig-geo')
    if os.path.exists(fn):
        raw = open(fn, 'r').read()
    else:
        raw = download_roster(
            'https://stat.ethz.ch/mailman/roster/r-sig-geo',
            '_@thomaslevine.com', input())
        open(fn, 'x').write(raw)
    companies(raw)
