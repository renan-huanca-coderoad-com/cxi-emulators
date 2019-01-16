#!/bin/bash
count=0; total=0;
for i in {1..20}
do
  t0=`date +%s%3N`
  curl -X GET \
	    https://dev.red.vizix.io/product-api/rest/products/03572642333695 \
	    -H 'Authorization: Basic cmVkX2RldjppZU03aXU3ZQ==' \
	    -H 'Content-Type: application/json' \
	    -H 'Postman-Token: d7dc77fb-284a-4432-9f22-192cd937e070' \
	    -H 'cache-control: no-cache' 2>/dev/null > temp.html
  t1=`date +%s%3N`
  TIMEDIFF=`echo "$t1 - $t0" | bc | awk -F"." '{print $1""substr($2,1,3)}'`
  ((count++));
  echo $TIMEDIFF

done

#echo "count $count"
