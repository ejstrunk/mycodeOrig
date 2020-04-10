#!/usr/bin/python3
import urllib.request
import json
import webbrowser

## Define APOD
#apodurl = 'https://api.nasa.gov/planetary/apod?'
#mykey = 'api_key=HIvxKT8AwEYNGOIjkX3intQja6ZmP2FUNwOqhzdH' ## your key goes in place of DEMO_KEY

## Call the webservice
#apodurlobj = urllib.request.urlopen(apodurl + mykey)

## read the file-like object
#apodread = apodurlobj.read()

## decode JSON to Python data structure
#decodeapod = json.loads(apodread.decode('utf-8'))

## display our Pythonic data
#print("\n\nConverted Python data")
#print(decodeapod)

## use Firefox to open the HTTPS URL
#input('\nPress Enter to open NASA Picture of the Day in Firefox')
#webbrowser.open(decodeapod['url'])

#############START OF SECOND SCRIPT FOR LAB PURPOSES################
from pprint import pprint as pp # part of the standard library

## define some constants
NASAAPI = 'https://api.nasa.gov/planetary/apod?' # this is our API to call
MYKEY = 'api_key=HIvxKT8AwEYNGOIjkX3intQja6ZmP2FUNwOqhzdH' ## this is our api key

## pretty print json
def main():
    """Runtime Code"""
    nasaapiobj = urllib.request.urlopen(NASAAPI + MYKEY) # call the webservice
    nasaread = nasaapiobj.read() # parse the JSON blob returned
    convertedjson = json.loads(nasaread.decode('utf-8')) # convert JSON

    # Show converted JSON
    print(convertedjson) # show converted JSON without pprint
    input('\nThis is converted json. Press ENTER to continue.') # pause for ENTER

    # Show Pretty Print JSON
    pp(convertedjson) # this is pretty print in action
    # pprint.pprint(convertedjson) # if you do a simple import pprint, the result is a long usage
    input('\nThis is pretty printed JSON. Press ENTER to continue.') # pause for ENTER

    # Print the description of the photo we are about to view
    print(convertedjson['explanation']) # display the value for the key explanation
    input('\nPress ENTER to view this photo of the day') # pause for ENTER

    webbrowser.open(convertedjson['hdurl']) # open in the webbrowser

main()
