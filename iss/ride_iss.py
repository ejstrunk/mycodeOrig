#!/usr/bin/python3
"""Alta3 || Tracking ISS"""

import urllib.request
import json

## Define URL
MAJORTOM = 'http://api.open-notify.org/astros.json'

def main():

    ## Call the webservice
    groundctrl = urllib.request.urlopen(MAJORTOM)

    ## put fileobject into the helmet
    helmet = groundctrl.read()

    ## decode JSON to Python data structure
    helmetson = json.loads(helmet.decode('utf-8'))

    ## display our Pythonic data
    print("\n\nConverted Python data")
    print(helmetson)

    print('\n\nPeople in Space: ', helmetson['number'])
    people = helmetson['people']
    #for x in helmetson:
    #    print("\n" + helmetson['people'] + "on the" + helmetson['craft'] + ".")
    for x in helmetson['people']: # spelled helmetson wrong, bruh
        print(x["name"] + " on the " + x["craft"])

main()
