#!/usr/bin/python3
"""Script that fetches https://alx-intranet.hbtn.io/status"""
import requests

url = 'https://alx-intranet.hbtn.io/status'
res = requests.get(url)

print("Body response:")
print("\t - type: {}".format(type(res.text)))
print("\t - content: {}".format(res.text))
