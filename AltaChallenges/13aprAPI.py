#!/usr/bin/python3

import requests

def main():
    quote = requests.get("https://quotes.rest/qod?language=en")
    quote= quote.json()
    print(f"Today\'s quote is from {quote['contents']['quotes'][0]['author']}:")
    print({quote['contents']['quotes'][0]['quote']})
main()
