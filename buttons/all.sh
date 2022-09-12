#!/bin/bash
/usr/bin/python3 /home/pi/buttons/up.py &
#> /dev/null 2>&1
/usr/bin/python3 /home/pi/buttons/down.py &
# > /dev/null 2>&1
/usr/bin/python3 /home/pi/buttons/play.py &
# > /dev/null 2>&1
/usr/bin/python3 /home/pi/buttons/next.py &
# > /dev/null 2>&1
exit 0
