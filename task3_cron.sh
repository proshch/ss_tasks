#!/usr/local/bin/bash

if [ $1 == "CPU" ]; then
    echo "Number of CPU Cores: "
    sysctl -a | grep 'hw.ncpu' | cut -d ':' -f2
elif [ $1 == "RAM" ]; then
   echo "RAM Size: "..
   sysctl hw.physmem
elif [ $1 == "DiskSpace" ]; then
    echo "Disk Space: "
    df -h
elif [ $1 == "users" ]; then
    echo "The last users which were login on the host: "
    last | head -4
elif [ $1 == "process" ]; then
    echo "Number of active Python and Perl process"
    ps | awk '{
                for(i=1; i<=NF; i++){
                    if(i == 5 && $i == "python")
                        py_count = py_count + 1;
                    else if (i == 5 && $i == "perl")
                        perl_count = perl_count + 1;
                }
            }; END { printf "Number of active Python process: %s\nNumber of active Perl process: %s\n", py_count, perl_count }'
else
    echo "Nice try!"
fi

