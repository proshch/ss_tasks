#!/usr/local/bin/bash
echo "Select what you one"
echo "1) Number of CPU Cores: "
echo "2) Disk Space: " 
echo "3) RAM Size: "
echo "4) The last users which were login on the host: "               
echo "5) Number of active Python and Perl process"
read choice;

case $choice in
    1) sysctl -a | grep 'hw.ncpu' | cut -d ':' -f2;;
    2) df -h;;
    3) sysctl hw.physmem;;
    4) last | head -4;;
    5) ps | awk '{
                for(i=1; i<=NF; i++){
                    if(i == 5 && $i == "python")
                        py_count = py_count + 1;
                    else if (i == 5 && $i == "perl")
                        perl_count = perl_count + 1;
                }
            }; END { printf "Number of active Python process: %s\nNumber of active Perl process: %s\n", py_count, perl_count }';;
    *) echo "Empty args";;
esac

