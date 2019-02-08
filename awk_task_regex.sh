#! /usr/local/bin/bash

choice="$1"
file="$2"
TIME_REGEX="([0-9]|0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]$"
IP_REGEX="^([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])"

if [ $choice = "ip" ]; then
    awk -v IP="${IP_REGEX}" '{
        for(i=1;i<=NF;i++){
            if($i~IP){
                print $i
            }
        }
    }' "$file" | sort -n | uniq -c
elif [ $choice = "time" ]; then
    awk -v TIME="$TIME_REGEX" '{
        for(i=1;i<=NF;i++){
            m=match($i, TIME)
            if($i~TIME){
                print substr($i, RSTART, RSTART + RLENGTH)
            }
        }
    }' $file
else
    echo "Try again!"
fi
