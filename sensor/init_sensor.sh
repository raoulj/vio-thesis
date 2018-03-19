source config.sh
touch /Volumes/boot/ssh
echo "dtoverlay=dwc2" >> /Volumes/boot/config.txt
echo "dwc_otg.lpm_enable=0 console=serial0,115200 console=tty1 root=PARTUUID=37665771-02 rootfstype=ext4 elevator=deadline fsck.repair=yes rootwait modules-load=dwc2,g_ether quiet init=/usr/lib/raspi-config/init_resize.sh" > /Volumes/boot/cmdline.txt
cp ~/Developer/vio-thesis/sensor/wpa_supplicant.conf /Volumes/boot/wpa_supplicant.conf
sudo umount /dev/disk1s1