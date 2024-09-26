#! /usr/bin/env python3

import gps               # the gpsd interface module
import maidenhead as mh  # maidenhead library to convert lat/long

session = gps.gps(mode=gps.WATCH_ENABLE)

try:
    while 0 == session.read():
        if not (gps.MODE_SET & session.valid):
            # not useful, probably not a TPV message
            continue

        if ((gps.isfinite(session.fix.latitude) and
             gps.isfinite(session.fix.longitude))):
            level=4
            print (mh.to_maiden(session.fix.latitude, 
                    session.fix.longitude, level))
            break
        else:
            print("NOFIX")
            break

except KeyboardInterrupt:
    # got a ^C.  Say bye, bye
    print('')

# Got ^C, or fell out of the loop.  Cleanup, and leave.
session.close()
exit(0)
