#! /bin/sh

echo "############### Clean Folders ###############"
rm -rf ../test1/ *../test2/* ../compress.tar.gz /tmp/compress.tar.gz /tmp/results.tar.gz /tmp/Latency.csv /tmp/RequestData.xml
sleep 3
echo "############### Run Jmeter ###############"
./jmeter.sh -n -t ${1} -l ../test1/vizix.jtl -e -o ../test2/
sleep 3
cd ..
sleep 1
echo "############### Compres Results ###############"
tar -czvf compress.tar.gz test2/
sleep 3
echo "############### Copy Results in Tmp folder ###############"
cp compress.tar.gz /tmp
sleep 1
echo "###############Compress Results and Data ###############"
cd /tmp
sleep 1
tar -czvf results.tar.gz compress.tar.gz Latency.csv RequestData.xml
echo "####### HTTP Server http://40.76.3.235:9050/compress.tar.gz ######"
sleep 2
python -m SimpleHTTPServer 9050
