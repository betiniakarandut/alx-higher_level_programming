#!/usr/bin/python3
"""Script that takes in a URL, sends a request to the URL"""
import sys as s
import urllib.request
import urllib.error

if __name__ == "__main__":
    url = s.argv[1]

    try:
        with urllib.request.urlopen(url) as res:
            content = res.read().decode('utf-8')
            print(content)
    except urllib.error.HTTPError as e:
        print('Error code: {}'.format(e.code))
