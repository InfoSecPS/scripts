#!/bin/bash

touch hostlist.txt
echo ">> Please enter IP/range"
   read ip_input
echo $ip_input > hostlist.txt
echo "$(tput setaf 3)[+]$(tpu sgr0) Running ping sweep on $ip_input"
   nmap -sP -iL hostlist.txt -oG pingscan > /dev/null
   grep Up pingscan | awk '{print$2}' > /root/Desktop/SCanResult/uplist
   grep Down pingscan | awk '{print$2}' > /root/Desktop/ScanResult/downlist
   cat /root/Desktop/ScanResult/uplist
echo "$(tput setaf 2)[+]$(tput sgr0)Hosts that are up from '$ip_input'"
  rm hostlist.txt
