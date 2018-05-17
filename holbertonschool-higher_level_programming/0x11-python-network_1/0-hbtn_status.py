#!/usr/bin/python3
# Script fetches URL
import urllib.request
import urllib.error
if __name__ == "__main__":
    url = 'https://intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        data = response.read()
        print('Body response:')
        print('\t- type:', type(data))
        print('\t- content:', data)
        print('\t- utf8 content:', data.decode('utf-8'))
