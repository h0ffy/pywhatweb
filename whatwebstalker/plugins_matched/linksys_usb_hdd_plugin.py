import sys
import os
			
class linksys_usb_hdd_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "ghdb" : 'intitle:"Network Storage Link for USB 2.0 Disks" Firmware", "certainty" : '75 },
			{ "text" : '<title>Network Storage Link for USB 2.0 Disks</title>' },
			{ "firmware" : '/          Version: &nbsp;V([\d\.\-a-zA-Z]+)<\/span> &nbsp;&nbsp;<\/td>/ },
			{ "model" : '/	 <td align="center" width="100" class="mname">([^<]+)<\/td>/ },
		]

