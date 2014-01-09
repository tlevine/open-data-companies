#!/usr/bin/env python3
import os

import requests
from lxml.html import fromstring

def download_roster(l, email, password):
    '''
        <FORM Method=POST ACTION="../roster/r-sig-geo">
        <INPUT name="language" type="HIDDEN" value="en" >(<i>The subscribers list is only available to the list
                members.</i>) <p>Enter your address and password to visit  the subscribers list: <p><center> Address: <INPUT type="Text" name="roster-email" size="20" value="">Password: <INPUT type="Password" name="roster-pw" size="15">&nbsp;&nbsp;<INPUT name="SubscriberRoster" type="SUBMIT" value="Visit Subscriber List" ></center>
            </FORM>
    '''
    data = {
        'language': 'en',
        'roster-email': email,
        'roster-pw': password,
        'SubscriberRoster': 'Visit Subscriber List',
    }
    r = requests.post('https://stat.ethz.ch/mailman/roster/r-sig-geo',
        data = data, stream = True)

    fp = open(fn(l), 'xb')
    for c in r.iter_content():
        fp.write(c)

def companies(raw):
    html = fromstring(raw)

def fn(l):
    return os.path.join('downloads',l.split('/')[-1] + '.html')

if __name__ == '__main__':
    l = 'https://stat.ethz.ch/mailman/roster/r-sig-geo'
    if not os.path.exists(fn(l)):
        download_roster(l,'_@thomaslevine.com', os.environ['PASSWORD'])
    raw = open(fn(l), 'r').read()
    companies(raw)
