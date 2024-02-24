#!/usr/bin/python3
"""POST request is sent to a given URL with an email.
 and shows the body of the response.
"""
import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    email = {"email": sys.argv[2]}
    data_encode = urllib.parse.urlencode(value).encode("ascii")

    request = urllib.request.Request(url, data_encode)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode("utf-8"))
