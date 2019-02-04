#!/bin/bash
count=0; total=0;
for i in {1..20}
do
  t0=`date +%s%3N`
  curl -X POST \
	  https://dev.red.vizix.io/statemachine-api-status-rest/rest/statuses/epcs \
	    -H 'Authorization: Basic cmVkX2RldjppZU03aXU3ZQ==' \
            -H 'Content-Type: application/json' \
	    -H 'Postman-Token: f0d3dedd-da45-44c7-ac4b-0e5d38c346d0' \
	    -H 'cache-control: no-cache' \
	    -d '{"query" : [ "urn:epc:id:sgtin:357264.0233369.1" ]}' 2>/dev/null > temp.html
  t1=`date +%s%3N`
  TIMEDIFF=`echo "$t1 - $t0" | bc | awk -F"." '{print $1""substr($2,1,3)}'`
  ((count++));
  echo $TIMEDIFF

done

#echo "count $count"
