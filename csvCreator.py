import requests
import csv
import json

weight = 0
isbn = ""

while True:
    isbn = input("Scan ISBN code: ")
    if isbn == "end":
        break
    response = requests.get("https://openlibrary.org/isbn/"+isbn+".json")
    print(response.text)
    print(response.json()['contributors'][0]['name'])
    authorResp = requests.get("https://openlibrary.org"+response.json()['authors'][0]['key']+".json")
    print(authorResp.text)
    authorResp = requests.get("https://openlibrary.org"+authorResp.json()['location']+".json")
    print(authorResp.json()['name'])
