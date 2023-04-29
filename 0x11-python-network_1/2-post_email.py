#!/usr/bin/python3
"""Script that takes in a URL and an email, sends a POST request"""
import urllib.request
import urllib.parse
import sys as s

if __name__ == "__main__":

    url = s.argv[1]
    email = s.argv[2]
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')
    with urllib.request.urlopen(url, data) as res:
        body_res = res.read().decode('utf-8')
        print('Your email is:', body_res)
