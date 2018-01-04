# This python script will ping the ip address and record the failed ping package.
# Tested on RHEL6.3  python 2.7.11
# How to use : 'python ping.py' and a log ping.log will be created in the same directory

import subprocess
import time
import logging





# Main function starts here

logging.basicConfig(filename='ping.log', level=logging.INFO)
target_ip = "1.1.1.1"
# set the how long the loop runs 60 * 1 is 60 seconds
time_end = time.time() + 60 * 1

while time.time() < time_end:

    p1 = subprocess.Popen (['ping', '-c 1', target_ip], stdout = subprocess.PIPE)
    output = p1.communicate()[0]
    str = "100% packet loss"

    # if ping failed, log it
    if (output.find(str)!=-1):
        localtime = time.asctime( time.localtime(time.time()) )
        print "Local current time :", localtime    
        print output
        logging.info(localtime)
        logging.info(output)

