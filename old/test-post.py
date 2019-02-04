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
print("### Test Post ###")
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

data1 = {
           "filters":[
                     {
                                  "property":"type",
                                           "operator":"EQ",
                                                    "values":[
                                                                    "ObjectEvent"
                                                                             ]
                                                          },
                           {
                                        "property":"bizStep",
                                                 "operator":"EQ",
                                                          "values":[
                                                                          "urn:epcglobal:cbv:bizstep:cycle_counting"
                                                                                   ]
                                                                }
                              ],
              "order":{
                        "property":"eventTime",
                              "direction":"DESC"
                                 },
                 "pagination":{
                           "documents":20,
                                 "page":0
                                    }
                 }

data2 = {
           "query":[
                        "urn:epcglobal:cbv:disp:sellable_not_accessible"
                           ],
              "filters":[
                        {
                                     "filter":"bizSteps",
                                              "excluding":True,
                                                       "values":[
                                                                       "urn:epcglobal:cbv:bizstep:cycle_counting"

                                                                                ]
                                                             }
                           ]
              }


data3 = {
           "query":[
                        "urn:epcglobal:cbv:disp:encoded"
                           ],
              "filters":[
                        {
                                     "filter":"bizSteps",
                                              "excluding":False,
                                                       "values":[
                                                                       "urn:epcglobal:cbv:bizstep:encoding"

                                                                                ]
                                                             }
                           ]
              }

data =  {
            "order": {
                      "property": "creationTime",
                            "direction": "ASC"
                                },
                "filters": [{
                          "property": "bizStep",
                                "operator": "EQ",
                                "values": ["urn:epcglobal:cbv:bizstep:packing"]
                                          },{
                                                    "property": "status",
                                                          "operator": "EQ",
                                                                "values": ["available"]
                                                                    }]
                                          }

data = {}


sum = 0
for x in range(0, max_requests):
    start = time.time()
    response = requests.post(url, headers=headers, data=json.dumps(data))
    end = time.time()
    samples[x] = (end - start)
    print("status: %s time: %0.3f" % (response.status_code, (end - start)))
    print("bytes: %s" % len(response.text))
    print(response.text)

print("mean: %0.3f" % np.mean(samples))
print("std: %0.3f" % np.std(samples))
