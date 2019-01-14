import requests
import json
import uuid
import time
import sys

url = "%s/supply-chain-api/rest/supply_chain/reference_lists" % sys.argv[1]

print("url: %s" % url)

headers = {
    "Accept-Encoding": "gzip, deflate",
    "Authorization": "Basic cm9vdDpDb250cm9sMTIzIQ==",
    "Content-Type": "application/json",
    "Accept": "application/json"
}


data = {
  "contentFormat": "quantity",
  "transactionId": "searchnpick-%s" % uuid.uuid4(),
  "bizStep": "urn:epcglobal:cbv:bizstep:packing",
  "bizLocation": "FRA082"
}

max_elements = int(sys.argv[2])

elements = json.loads('[]'); # [max_elements]

for x in range(0, max_elements):
     elements.append({
       "format": "quantity",
       "gtin": "%014d" % (x + 1),
       "quantity": 1
     })

content = {
    "content": elements
}

data["containers"] = [content]

for x in range(1, 2):
    data["transactionId"] = "searchnpick-%s" % uuid.uuid4()
    start = time.time()

    print(data)

    response = requests.put(url, data=json.dumps(data), headers=headers)
    end = time.time()

    print("status: %s time: %0.3f" % (response.status_code, (end - start)))
    print("refrence id: %s" % response.text)
