import sys
import os
			
class Pluginapphp_calendar_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "version" : "/<!-- This script was generated by ApPHP Calendar v\.([\d\.]+) \(http:\/\/www\.apphp\.com\) -->/" },
			{ "text" : "<tr class='tr_days'><td class='th'>Sunday</td><td class='th'>Monday</td><td class='th'>Tuesday</td><td class='th'>Wednesday</td><td class='th'>Thursday</td><td class='th'>Friday</td><td class='th'>Satarday</td></tr>" },
		]
		return(self.rules)

