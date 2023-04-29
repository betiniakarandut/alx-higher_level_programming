#!/usr/bin/python3
"""Script that takes in a URL, sends a request to the URL"""
import urllib.request
import sys as s

if __name__ == "__main__":
    url = s.argv[1]

    with urllib.request.urlopen(url) as res:
        headers = res.info()
        x_request_id = headers.get("X-Request-Id")
        print(x_request_id)
