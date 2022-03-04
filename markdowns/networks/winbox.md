# Winbox
Winbox is the application used to access RouterOS to access the Mikrotik Firewall



---
### Daily Maintenance
1. Keep the Winbox Updated(https://mikrotik.com/download)
2. Check the working interfaces in IP -> Interface
   1. Check the LAN and WIFI bridges both have Tx Rates
3. Check the DHCP Server in IP -> DHCP Server
   1. Check that both LAN and WIFI IP addresses are being distributed
---
### Working Configuration
In the event the router suddenly and unexpectedly fails, a working onfiguration backup is available through either the IT Shared NEtwork Drive or this [This Google Drive Link](www.google.com) 

Steps to follow to restore the working configuration
1. Notify Head IT, SACs and Immediate Superior that the router will be rebooted
2. Open Winbox
3. Go to Files
4. File List will be opened
5. Select the working configuration and select Restore
6. Wait 30 seconds for the router to reboot.
7. Notify Head IT, SACs and Immediate Superior about the progress