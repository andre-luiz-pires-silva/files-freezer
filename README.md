# files-freezer

# create auto-backup service
- Connect the media
- Get media label with: systemctl list-units -t mount
- Create the file /etc/systemd/system/freezer-media-bkp.service with
`
[Unit]
Description=Files Freezer Backup
Requires=media-usb0.mount
After=media-usb0.mount

[Service]
ExecStart=python3 /home/pi/files-freezer/media_bkp.py --media /media/usb --storage-path /home/pi/Public

[Install]
WantedBy=media-usb0.mount
`
- Enable the service with: sudo systemctl enable freezer-media-bkp.service