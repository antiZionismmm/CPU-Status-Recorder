# CPU-Status-Recorder
CPU Status Recorder for Linux SBCs

Step 1: Set Time Zone to GMT+3:30

    Open a terminal on your NanoPi.

    Check the available time zones using the timedatectl command:

    bash

timedatectl list-timezones

This will display a list of time zones. Find the GMT+3:30 time zone in the list.

Set the time zone to GMT+3:30 using the timedatectl command. Replace your_time_zone with the appropriate time zone from the list:

bash

sudo timedatectl set-timezone your_time_zone

For example, if GMT+3:30 is "Asia/Tehran," you would run:

bash

    sudo timedatectl set-timezone Asia/Tehran

    This will update your system's time zone to GMT+3:30.

Step 2: Auto-Start Your Script at Boot

To auto-start your Python script at boot, you can create a systemd service. Here's how to do it:

    Create a systemd service file for your Python script. Replace yourusername with your actual username and adjust the paths as needed:

    bash

sudo nano /etc/systemd/system/recorder.service

Add the following content to the file:

plaintext

[Unit]
Description=Your Recorder Script

[Service]
Type=simple
User=yourusername
ExecStart=/usr/bin/python3 /path/to/your/recorder.py
WorkingDirectory=/path/to/your/script/directory

[Install]
WantedBy=multi-user.target

Save and exit the text editor.

Enable the systemd service to start at boot:

bash

sudo systemctl enable recorder.service

Start the service:

bash

sudo systemctl start recorder.service

Your Python script will now start automatically at boot.

You can also check the status of the service to make sure it's running without errors:

bash

sudo systemctl status recorder.service
