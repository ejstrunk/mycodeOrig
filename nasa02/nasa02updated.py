#!/usr/bin/python3
import requests ## 3rd party URL lookup

## define the main function
def main():
    neourl = 'https://api.nasa.gov/neo/rest/v1/feed?'  # API URL
    year = input("Please enter the start date of the data you would like to view, beginning with 4-digit year: ")
    month = input("2-digit month: ")
    day = input("2-digit day: ")
    startdate = 'start_date' + year + '-' + month + '-' + day ## start date for data
    enddate = '&end_date=END_DATE' ## create a mechanism to utilize enddate
    mykey = '&api_key=HIvxKT8AwEYNGOIjkX3intQja6ZmP2FUNwOqhzdH'

    neourl = neourl + startdate + mykey

    neojson = (requests.get(neourl)).json()

    print(neojson)

main()
