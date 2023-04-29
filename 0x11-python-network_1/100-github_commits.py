#!/usr/bin/python3
"""Backend: Technical challenge on Github API"""
import requests
import sys as s

if __name__ == "__main__":

    url = "https://api.github.com./repos/{}/{}/commits".format(
            s.argv[1], s.argv[2])
    res = requests.get(url)
    details = res.json()
    for j in range(15):
        if res.status_code == 200:
            print("{}:{}".format(
                  details[j].get("sha"),
                  details[j].get("commit").get("author").get("name")))
        else:
            print("Error code {}".format(details.status_code))
