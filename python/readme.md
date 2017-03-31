### portscan.py

Taken from the Violent Python book with modifications. I wasn't too happy with just retyping existing code. I don't learn well that way. Anywho, it was an exercise on how to space things out, how it worked and how I could modify something. 

****

### httpgrab.py

I've created this script from scratch. It'll be a working progress I'm sure. Just grabs the HEADER, OPTIONS and sends a GET request to the desired webserver on port 80. Excuse the messy functions. I'm sure there's a way of grouping them together, but for now it works at least.

#### Changes
* Original IP address input was to alter the code for the IP. 
* Changed to raw_input but that annoyed me.
* Now it takes the IP Address as an argument passed to the script. So far, the way I've been used to running python scripts. 

****
### argparse.py

In search of some sort of experience in validation I was directed to using argparse. This is just an exercise in implementing argparse to make sure the data you need has been entered. If not, you get told about it. Next step is to validate that it is indeed an IP address that is being entered. 

****
### md5.py

I was bored. I wanted a quick way to md5 a string to play around with password cracking without leaving the terminal. Seeing I'm working on Python just now it was a good idea. Takes a string, and outputs the MD5 hash. Simples. 
