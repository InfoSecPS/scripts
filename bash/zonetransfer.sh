#! /bin/bash
clear

echo "Enter the domain name/URL"
read domain

dig NS $domain +short | sed -e "s/\.$//g" | while read nameserver; do echo "Testing $domain @ $nameserver"; dig AXFR $domain "@$nameserver"; done
