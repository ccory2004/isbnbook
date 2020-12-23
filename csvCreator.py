import requests
import csv
import json

weight = 0
isbn = ""

while True:
    isbn = input("Scan ISBN code: ")
    if isbn == "end":
        break
    response = requests.get("http://bms.bowker.com/rest/books/isbn/"+isbn)
    print(response.text)
