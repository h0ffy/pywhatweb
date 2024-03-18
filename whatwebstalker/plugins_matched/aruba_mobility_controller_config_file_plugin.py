import sys
import os
			
class aruba_mobility_controller_config_file_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : 'logging level warnings stm' }
			{ "text" : 'packet-capture-defaults tcp disable udp disable sysmsg disable other disable' }
			{ "text" : 'ids-policy rate-frame-type-param disassoc node-time-interval' }
		]

