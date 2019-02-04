#!/bin/bash
count=0; total=0;
for i in {1..20}
do
  t0=`date +%s%3N`

  curl -X POST \
	  'https://dev.red.vizix.io/statemachine-api-status-rest/rest/statuses/location/level/premise/code/CHE041/gtins?format=gtin_loc_count' \
	  -H 'Authorization: Basic cmVkX2RldjppZU03aXU3ZQ==' \
	  -H 'Content-Type: application/json' \
	  -H 'Postman-Token: a161517f-1017-4426-bcd0-f7871c4fac88' \
	  -H 'cache-control: no-cache' \
	  -d '{
    "filters" : [ {
        "filter" : "dispositions",
	    "values" : [ "urn:epcglobal:cbv:disp:sellable_accessible", "urn:epcglobal:cbv:disp:sellable_not_accessible", "urn:epcglobal:cbv:disp:sellable_displayed", "urn:epcglobal:cbv:disp:encoded" ],
	        "excluding" : false
		  } ],
		    "query" : [ "08053672814217" ]
	    }' 2>/dev/null > temp.html

  t1=`date +%s%3N`
  TIMEDIFF=`echo "$t1 - $t0" | bc | awk -F"." '{print $1""substr($2,1,3)}'`
  ((count++));
  echo $TIMEDIFF

done

#echo "count $count"
