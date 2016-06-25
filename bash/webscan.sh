#!/bin/bash
clear

# Check for Root
function rootcheck() {
if [[ $USER != "root" ]] ; then
echo "Please Note: This script must be run as root!"
exit 1
fi
echo -e " Checking for Root or Sudo: ${g}PASSED!${endc}"
}
rootcheck
HOST=$1
echo "=================================================="
echo "=== Scanning $HOST. Please wait...======="
echo "=================================================="
sleep 2
nmap -sS -p- $HOST -Pn -n --open
sleep 2
echo "   "
echo "$(tput setaf 3)[+]$(tput sgr0) Now scanning port 80 for any web directories"
sleep 2
dirb http://$HOST
echo "     "
echo "$(tput setaf 2)[+]$(tput sgr0) Scan Complete!"
