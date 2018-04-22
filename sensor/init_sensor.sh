touch /Volumes/boot/ssh
cp -f resources/config.txt /Volumes/boot/config.txt
cp -f resources/cmdline.txt /Volumes/boot/cmdline.txt
cp -f resources/wpa_supplicant.conf /Volumes/boot/wpa_supplicant.conf
echo "Need to provide the computer password"
sudo umount /dev/disk1s1
