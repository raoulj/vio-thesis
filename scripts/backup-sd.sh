#!/bin/bash
BACKUP_BASE_PATH="/Users/raoulrodriguez/Developer/vio-thesis/images"
BACKUP_CHUNK_SIZE="64m"
echo "Consider the following drives:"
diskutil list

echo "Which one do you want to back up?  Enter the number and press ENTER:"
echo -n "/dev/disk"
read disk_number

echo "What name do you want for the backup?  Enter the full name (followed by .img) and press ENTER:"
read file_name

sudo dd if="/dev/disk$disk_number" of="$BACKUP_BASE_PATH/$file_name" bs="$BACKUP_CHUNK_SIZE"