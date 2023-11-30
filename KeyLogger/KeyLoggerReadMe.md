#Key Logging Script
This folder contains all of the files for the Keylogging script.

Main.py is the main file that calls the MyKeyLogger.py file.
MyKeyLogger.py performs the logic of the key logging, in order to use, you should install the necessary Python libraries and change the directory file path that the log file is created.

The mykeylogger.service file is a user level daemon file that is handled by systemd. In order to use this effectively, you can put it in at ~/.config/systemd/user and run the necessary commands to enable systemd to start this file on boot. 
This allows the keylogger to work across boots

The key logger use a library called setproctitle in order to disguise the process name and make it difficult to find. Because of the limited CPU and memory usage, process ownership belonging to systemd, and the inconspicuous process title, this process is extremely difficult to discover for an IDS.
The key logger stores logs and rotates them once they hit a certain size in order to maintain a minimal footprint on the system. The file can be further configured to export the logs via email.
