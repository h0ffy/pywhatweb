import sys
import os
			
class proxmox_ve_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "version" : '/<a href='http:\/\/www\.proxmox\.com' target='_blank' class="boxheadline">Proxmox Virtual Environment ([^<^\s]+)<\/a>/ }
			{ "text" : '<img alt=" style="display:block;border:0px;width:1000px;max-height:300px;" src=\'/images/logo_pve.jpg\'>' }
		]

