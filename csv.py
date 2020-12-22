import requests
import csv
import json

weight = 0
isbn = ""
with open(, "a+") as lol:
    pass

while True:
    isbn = input("Scan ISBN code: ")
    if isbn == "end":
        break
    try:
        response = requests.get("https://openlibrary.org/isbn/"+isbn+".json")
        print(json.dumps(response, indent=4))

        arr = []
        arr.append(response.json()['title'])
        for name in response.json()['authors']:
            print(name)
            arr.append(name)
            try:
                arr.append(response.json()['isbn_13'])
            except:
                arr.append(response.json()['isbn_10'])
                with open(filename, "a+") as f:
                    writer = csv.writer(f, delimiter=",")
                    writer.writerow(arr)
    except:
        print("ISBN Code incorrect, try again")
