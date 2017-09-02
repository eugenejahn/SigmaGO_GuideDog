
from gps3.agps3threaded import AGPS3mechanism
import time

class gps():
    def init(self):
        self.agps_thread = AGPS3mechanism()  # Instantiate AGPS3 Mechanisms
        self.agps_thread.stream_data()  # From localhost (), or other hosts, by example, (host='gps.ddns.net')
#        self.agps_thread.run_thread()  # Throttle time to sleep after an empty lookup, default '()' 0.2 two tenths of a second

    def start(self):
        self.agps_thread.run_thread()
        while True:  # All data is available via instantiated thread data stream attribute.
        # line #140-ff of /usr/local/lib/python3.5/dist-packages/gps3/agps.py
            print('---------------------')
            print(                   self.agps_thread.data_stream.time)
            print('Lat:{}   '.format(self.agps_thread.data_stream.lat))
            print('Lon:{}   '.format(self.agps_thread.data_stream.lon))
            print('Speed:{} '.format(self.agps_thread.data_stream.speed))
            print('Course:{}'.format(self.agps_thread.data_stream.track))
            print('---------------------')
            time.sleep(1) # Sleep, or do other things for as long as you like.

