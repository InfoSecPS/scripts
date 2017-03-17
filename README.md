# Scripts

A centralised place for anything I knock up in BASH or whatever else I feel useful. 

## Ping Sweeper
A ping sweeper that takes an IP or IP Range as an input, passes it to Nmap and outputs 'Up' hosts to the screen.
[hostscan.sh](https://github.com/InfoSecPS/scripts/blob/master/bash/hostscan.sh)

## Zone Transfer
Takes input of domain/URL and runs a dig command and outputs to screen.
[zonetransfer.sh](https://github.com/InfoSecPS/scripts/blob/master/bash/zonetransfer.sh)


## Pentest Scans
A working project that incorporates both of the above scans into one BASH script.
It takes an input of 'Company name' and creates a directory and sub folders. 
A menu displays with options. On selection, you are passed to the function of each option. A DNS 'ANY' scan or an Nmap Ping Sweep and an MSSQL Emuneration scan on target IP. User input needed on all scans.
All files saved within the respective folders inside the Company Directory that was created. 
[pentest.sh](https://github.com/InfoSecPS/scripts/blob/master/bash/pentest.sh)
