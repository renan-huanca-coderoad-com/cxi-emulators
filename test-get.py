import requests
import json
import uuid
import time
import numpy as np
import sys
import argparse


parser = argparse.ArgumentParser(description='Test Get')
parser.add_argument('--server', dest='server', required=True,
                help='server')
parser.add_argument('--endpoint', dest='endpoint', required=True,
                help='server')
parser.add_argument('--nreqs', dest='number_of_requests', required=False,
                default=10, help='number of requests')


args = parser.parse_args()

print("")
print("### Test Get ###")
print("")

print("> server: %s" % args.server)
print("> endpoint: %s" % args.endpoint)
print("> #requests: %s" % args.number_of_requests)
print("")

url = "%s/%s" % (args.server, args.endpoint)

# url = "https://newdev2.vizix.io/product-api/rest/products/00014671041095/picture"

headers = {
    "Accept-Encoding": "gzip, deflate",
    "Authorization": "Basic cm9vdDpDb250cm9sMTIzIQ==",
    "Content-Type": "application/json",
    "Accept": "application/json"
}

max_requests = int(args.number_of_requests);
samples = [0] * max_requests ;

sum = 0
for x in range(0, max_requests):
    start = time.time()
    response = requests.get(url, headers=headers)
    end = time.time()
    samples[x] = (end - start)
    print("status: %s time: %0.3f" % (response.status_code, (end - start)))
    print(response.text)

print("mean: %0.3f" % np.mean(samples))
print("std: %0.3f" % np.std(samples))
