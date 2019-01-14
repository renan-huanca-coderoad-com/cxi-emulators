import requests
import json
import uuid
import time
import numpy as np



url = "https://newdev2.vizix.io/supply-chain-api/rest/supply_chain/reference_lists"

headers = {
    "Accept-Encoding": "gzip, deflate",
    "Authorization": "Basic cm9vdDpDb250cm9sMTIzIQ==",
    "Content-Type": "application/json",
    "Accept": "application/json"
}

max_requests = 25
samples = [0] * max_requests ;

sum = 0
for x in range(0, max_requests):
    start = time.time()
    response = requests.get(url, headers=headers)
    end = time.time()
    samples[x] = (end - start)
    print("status: %s time: %0.3f" % (response.status_code, (end - start)))

print("mean: %0.3f" % np.mean(samples))
print("std: %0.3f" % np.std(samples))
