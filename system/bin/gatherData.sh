#!/bin/bash

PINGFILE=/tmp/ping.txt
BIN_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Load helper functions for getting system data
source $BIN_DIR/pinghelper.sh

# Load the public IP of the memorybox
pip=$(curl -Ls http://ping.backupbox.se/public_ip.php)
echo "public_ip=$pip&" > $PINGFILE

# Load the local IP on the router
lip=$(ifconfig eth0 | grep 'inet addr:' | cut -d: -f2 | awk '{ print $1}')
echo "local_ip=$lip&" >> $PINGFILE

#Load Unique ID of backup hard drive
uuid=`blkid -s UUID -o value /dev/sda1`
echo "uuid=$uuid&" >> $PINGFILE

# Calculate free and total space of the backup drive
freespace /HDD >> $PINGFILE

# Load information of all backed up devices
gatherdevices $1>> $PINGFILE
