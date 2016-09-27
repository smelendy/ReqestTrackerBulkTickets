#!/bin/bash

/opt/rt4/bin/rt ls -o -Created -t ticket "Status != 'resolved'" -q 6 -f id,subject,created,id| grep "`date +"%a %b %d"`"   > /tmp/out
sed 's/$/ "https:\/\/rt.umw.local\/Ticket\/Display.html=/' /tmp/out |awk {'print $0$1'}| awk {'print $1","$2,$3,$4 ","$NF'} > ticketsreport.csv
