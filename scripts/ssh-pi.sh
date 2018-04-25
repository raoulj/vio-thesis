echo -n "The pi ip you want to ssh into: 192.168.0."
read ip

sshpass -p raspberry ssh pi@192.168.0.$ip
