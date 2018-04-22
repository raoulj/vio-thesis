echo -n "The pi ip you want to identity: 192.168.0."
read ip

echo "Connecting to pi@192.168.0.$ip"
sshpass -p 'raspberry' ssh -T pi@192.168.0.$ip << EOF > /dev/null
    echo 1 | sudo tee /sys/class/leds/led0/brightness
    sleep 1
    echo 0 | sudo tee /sys/class/leds/led0/brightness
EOF