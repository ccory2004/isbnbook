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
        try:
            for author in range(len(response.json()['authors'])):
                authorResp = requests.get("https://openlibrary.org"+response.json()['authors'][author]['key']+".json")
                print("Author: "+authorResp.json()['name'])
                authors.append(authorResp.json()['name'])
        except:
            try:
                for author in range(len(response.json()['authors'])):
                    authorResp = requests.get("https://openlibrary.org"+response.json()['authors'][author]['key']+".json")
                    authorResp = requests.get("https://openlibrary.org"+authorResp.json()['location']+".json")
                    print("Author: "+authorResp.json()['name'])
                    authors.append(authorResp.json()['name'])
            except:
                try:
                    for contributor in range(len(response.json()['contributors'])):
                        if response.json()['contributors'][contributor]['role'] == "Author":
                            authors.append(response.json()['contributors'][contributor]['name'])
                            print("Author: "+response.json()['contributors'][contributor]['name'])
                except:
                    print("Author not found")
                    authors.append("N/A")
        print("")
        with open("_data/booklist.yml", "a+", encoding="utf-8") as f:
            f.write("- title: \""+title+"\"\n")
            f.write("  isbn: \""+isbn+"\"\n")
            f.write("  authors: \""+', '.join(authors)+"\"\n")
            f.write("\n")
    except:
        print("Error with retrieving data")
        print("")
