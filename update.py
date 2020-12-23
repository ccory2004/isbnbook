import requests
import json
import yaml

print("Scan ISBN Barcodes to Add to the Site")
while True:
    isbn = input("Scan ISBN code: ")
    if isbn == "end":
        break
    try:
        response = requests.get("https://openlibrary.org/isbn/"+isbn+".json")
        print("Title: "+response.json()['title'])
        title = response.json()['title']
        try:
            print("ISBN: "+response.json()['isbn_13'][0])
            isbn = response.json()['isbn_13'][0]
        except:
            print("ISBN: "+response.json()['isbn_10'][0])
            isbn = response.json()['isbn_10'][0]
        authors = []
        for author in range(len(response.json()['authors'])):
            authorResp = requests.get("https://openlibrary.org"+response.json()['authors'][author]['key']+".json")
            print("Author: "+authorResp.json()['name'])
            authors.append(authorResp.json()['name'])
        print("")
        with open("_data/booklist.yml", "a+", encoding="utf-8") as f:
            f.write("- title: \""+title+"\"\n")
            f.write("  isbn: \""+isbn+"\"\n")
            f.write("  authors: \""+', '.join(authors)+"\"\n")
            f.write("\n")
    except:
        print("Error with retrieving data")
