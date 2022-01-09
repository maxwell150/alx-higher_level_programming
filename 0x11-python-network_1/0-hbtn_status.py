#!/usr/bin/python3
"""
script that fetches https://intranet.hbtn.io/status
"""
import urllib.request

if __name__ == '__main__':
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as file:
        content = file.read()
        print("Body response:")
        print("\t- type:", type(content))
        print("\t- content:", content)
        print("\t- utf8 content:", content.decode("utf-8"))
