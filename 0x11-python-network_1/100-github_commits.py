#!/usr/bin/python3
"""Backend: Technical challenge on Github API"""
import requests
import sys as s

if __name__ == "__main__":

    url = "https://api.github.com./repos/{}/{}/commits".format(
            s.argv[1], s.arigv[2])
    res = requests.get(url)
    details = res.json
    for j in range(15):
        if res.status_code == 200:
            print({}:{}.format(
                  details[j].get("sha"),
                  get.details[j]("commit").get("author").get("name")
        else:
            print("Oops!".format(res.status_code))
