#!/usr/bin/env python
import requests, argparse, re

def convert_url(url):
    if "w" in url:
        return url.replace("w", "https://w", 1)
    else:
        return url.replace(url[0], "https://www.{}".format(url[0]))

# Give the user the option to choose its target
parser = argparse.ArgumentParser(description="This program will catch all the headers of the specified url")
parser.add_argument("-u", "--url", help="The URL from which the headers will be extracted")
args = parser.parse_args()

# Analyze the url of the user to check if the url is valid
def check_url(url):
    if re.match(r'https://www\.\w*[^.].com', url) or re.match(r'www\.\w*.com', url) or re.match('http://www\.\w*[^.].com', url) or re.match(r'\w*.com', url):
        return True
    else:
        return False

# Convert the url
if args.url:
    if check_url(args.url):
        url = ""
        response = ""
        if "https" not in args.url:
            url = convert_url(args.url)
        else:
            url = args.url

        try:
            response = requests.get(url)
            print("\n[+] Headers of The Webpage {} : ".format(url))
            for item in response.headers:
                print("{} -> {}\n".format(item, response.headers[item]))
            print("[+] Amount of Headers : {}".format(str(len(response.headers))))
        except requests.exceptions.ConnectionError:
            print("[-] No such webpage")
    else:
        print("[-] Invalid URL")
else:
    print("[-] No URL specified")