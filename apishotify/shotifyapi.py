import requests
import csv

res = requests.get("https://2c3f163172dd38319f642d33707ce0ac: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@1quocanh.myshopify.com/admin/api/2020-10/orders.json",
                   'Authorization: Basic 2c3f163172dd38319f642d33707ce0ac')
res1 = requests.get("https://2c3f163172dd38319f642d33707ce0ac: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@1quocanh.myshopify.com/admin/api/2020-10/customers.json")
print(res1.text)
f = open('data.csv','w')
with f:
    writer = csv.writer(f)
    for column in res1.text:
        for row in column:
            writer.writerow(row)