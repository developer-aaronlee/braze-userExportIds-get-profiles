import csv
import json
import requests

url = 'https://rest.iad-06.braze.com/users/export/ids'
API_KEY = 'Bearer 2c324fa9-7629-4b0a-9527-7ac6e8b1e0d5'
headers = {
    'Content-Type': 'application/json',
    'Authorization': API_KEY
}

alldata = []
with open('batch_test_9_result.csv', 'w') as file:
    # str1 = ""
    with open('batch_test_9.csv') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            if len(row) == 0:
                continue
            temp = row[0].split(",")
            if temp[0] == "external_id":
                continue
            body = json.dumps({"email_address": temp[0]
                             })
            response = requests.post(url, data=body, headers=headers)
            a = response.json()
            all = []

            if len(a['users']) == 0:
                continue
            if len(a['users']) != 0:
                all.append([a['users'][0]['email']])
            for x in a['users']:
                if 'external_id' in x:
                    all.append([x['external_id']])
                else:
                    all.append([''])

            alldata.append(all)
            print(all)

with open("batch_test_9_result.csv", "w") as csvfile:
    writer = csv.writer(csvfile)
    for x in alldata:
        writer.writerow(x)
