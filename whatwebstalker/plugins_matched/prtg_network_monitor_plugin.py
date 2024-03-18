import sys
import os
			
class prtg_network_monitor_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "string" : /<title>PRTG Network Monitor \(([^\)]+)\)&nbsp;\|&nbsp;Welcome<\/title>/ }
			{ "version" : '/<link rel="stylesheet" type="text\/css" href="\/css\/prtgmini\.css\?prtgversion=([^"]+)" media="print,screen,projection" \/>/ }
			{ "version" : '/^PRTG/", "search" : 'headers[server]" }
			{ "version" : '/^PRTG\/([^\s]+)$/", "search" : 'headers[server]" }
		]

