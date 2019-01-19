#!/bin/bash

# README FIRST
# ============
#
# 1. Download jmeter form https://jmeter.apache.org/download_jmeter.cgi
# 2. Unpackage it to any folder
# 3. set JMETER_HOME env variable with the path were jmeter was put.
# 4. in this script (run-test.sh) set the server variable to the
#    address of the server you want to test.
#    i.e.:
#         server="dev.vizix.io"
#         server="staging.vizix.io"
#
# 5. execute ./run-test.sh
#

if [[ -z "${JMETER_HOME}" ]]; then
  echo "Please set JMETER_HOME system env variable"
  exit 0
else
  jmeter_path="${JMETER_HOME}"
fi

test_plan="cxi_endpoints.jmx"
server="dev.vizix.io"

echo
echo "test plan: [$test_plan]"
echo "server: [$server]"
echo

echo "cleaning results folder..."
rm -rf results
rm -rf cxiapi.jtl

echo "running jmeter on $jmeter_path"
echo

cmd="$jmeter_path/bin/jmeter.sh -n -JSERVER=$server -t $test_plan -l cxiapi.jtl -e -o results/"
echo "$cmd"
$cmd
