#!/usr/bin/python3
"""cript that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter."""
import requests
import sys as s

if len(s.argv) == 1:
    q = ""
else:
    q = sys.argv[1]

url = "http://0.0.0.0:5000/search_user"
data = {'q': q}
res = requests.post(url, data=data)

try:
    json_res = res.json()
    if json_res:
        print("[{}] {}".format(json_res['id'], json_res['name']))
    else:
        print("No result")
except ValueError:
    print("Not a valid JSON")
