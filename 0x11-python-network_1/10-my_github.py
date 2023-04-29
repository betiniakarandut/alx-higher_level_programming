#!/usr/bin/python3
"""Script that takes my Github credentials and display my id"""
import sys as s
import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":

    check = HTTPBasicAuth(s.argv[1], s.argv[2])
    res = requests.get("https://api.github.com/user", auth=check)
    print(res.json().get("id"))
