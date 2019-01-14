import requests
import json
import uuid
import time
import sys

url = 'http://10.100.1.79:8081/supply-chain-api/rest/supply_chain/reference_lists'

headers = {
    "Accept-Encoding": "gzip, deflate",
    "Authorization": "Basic cm9vdDpDb250cm9sMTIzIQ==",
    "Content-Type": "application/json",
    "Accept": "application/json"
}


with open(sys.argv[1]) as json_file:
    data = json.load(json_file)
    for x in range(1, 2):
        data["transactionId"] = "searchnpick-%s" % uuid.uuid4()
        start = time.time()

        response = requests.put(url, data=json.dumps(data), headers=headers)
        end = time.time()

        print("status: %s time: %0.3f" % (response.status_code, (end - start)))
        print("refrence id: %s" % response.text)
