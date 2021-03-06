
#!/bin/bash

freespace () {
        mount_point="$1"
        used_space=0
        mount_point=${1:-"/tmp"}
        threshold=${2:-10}
         
        used_space=`df -k $mount_point | grep % | awk {'print $5'} | sed 's/%//g'`
        used_space=`echo "$used_space" | sed -n 2p`
        
        available_space=`df -kH $mount_point | grep % | awk {'print $2'} | sed 's/%//g'`
        available_space=`echo "$available_space" | sed -n 2p`
        
        echo "available_space=$available_space&"
        echo "free_space=`expr 100 - $used_space`%&"
}

gatherdevices () {
	devices=`find -L $1 -maxdepth 2 -name manufacturer -printf '%h;'`
	arrIN=(${devices//;/ })
	declare -a DEVICES
	
	c=0
	for i in "${arrIN[@]}"
	do
	        path=(${i//// })
	        #echo ${path[2]}
		pendingbackup="false"
	        if [ -d "$i/tmp" ]; then pendingbackup="true"; fi
		manufacturer=`cat $i/manufacturer`
	        product=`cat $i/product`
	        model=`cat $i/model`
		deviceId=`cat $i/idProduct`
		size=`du -sch $i 2>/dev/null | sed -n '$p'`
		size=(${size//\t/ })
		size=${size[0]}
		lastbackup=`cd $i/backups > /dev/null && find . -mindepth 4 -maxdepth 4 |sort -nr |head -1`
	        DEVICES["$c"]="serial=${path[2]};deviceId=$deviceId;manufacturer=$manufacturer;product=$product;model=$model;size=$size;lastbackup=$lastbackup;pendingbackup=$pendingbackup"
	        let c=c+1
	done
	
	tLen=${#DEVICES[@]}
	
	echo "numdevices=$tLen&"
	for (( i=0; i<${tLen}; i++ ));
	do
	  echo "device$i=${DEVICES[$i]}&"
	done
}
