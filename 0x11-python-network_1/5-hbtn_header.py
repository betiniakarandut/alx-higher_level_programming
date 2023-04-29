#!/usr/bin/python3
"""Script that takes in a URL, sends a request to the URL"""
import requests
import sys as s

if __name__ == "__main":
    url = s.argv[1]
    res = requests.get(url)
    print(res.headers.get("X-Request-Id"))
