#!/bin/bash

if [[ -z "${JMETER_HOME}" ]]; then
  echo "Please set JMETER_HOME system env variable"
  exit 0
else
  jmeter_path="${JMETER_HOME}"
fi

test_plan="cxi_endpoints.jmx"
server="staging.vizix.io"

echo
echo "test plan: $test_plan"
echo "server: $server"
echo

echo "cleaning results folder..."
rm -rf results

echo "running jmeter on $jmeter_path"
echo
#                   ./jmeter.sh -n -t ${1} -l ../test1/vizix.jtl -e -o ../test2/
cmd="$jmeter_path/bin/jmeter.sh -n -Jpage=$server -t $test_plan -l vizix.jtl -e -o results/"
echo "$cmd"
$cmd
