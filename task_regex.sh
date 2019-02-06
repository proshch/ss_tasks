#!/usr/local/bin/bash

choice=$1
file=$2

TIME_REGEX="\b([0-9]|0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]\b"
IP_REGEX="([^[:punct:]]|^)\b([0-9]{1,2}|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]{1,2}|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]{1,2}|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]{1,2}|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\b([^[:punct:]]|$)"

if [ $choice = "ip" ]; then
    echo "You have choosen: $choice"
    egrep -o "$IP_REGEX" "$file" | sort -n -t . -k 1,1 -k 2,2 -k 3,3 -k 4,4 | uniq -c | less
elif [ $choice = "time" ]; then
    echo "You have choosen: $choice"
    egrep -o "$TIME_REGEX" "$file" | sort -u
else
    echo "Try again!"
fi
