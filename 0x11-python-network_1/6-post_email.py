#!/usr/bin/python3
"""Script that takes in a URL and an email address, sends a POST request"""
import requests
import sys as s

if __name__ == "__main__":
    url = s.argv[1]
    email = s.argv[2]

    payload = {'email': email}
    res = requests.post(url, data=payload)
    print(response.text)
