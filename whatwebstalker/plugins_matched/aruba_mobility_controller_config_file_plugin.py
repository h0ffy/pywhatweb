import sys
import os
			
class Pluginaruba_mobility_controller_config_file_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "logging level warnings stm" },
			{ "text" : "packet-capture-defaults tcp disable udp disable sysmsg disable other disable" },
			{ "text" : "ids-policy rate-frame-type-param disassoc node-time-interval" },
		]
		return(self.rules)

