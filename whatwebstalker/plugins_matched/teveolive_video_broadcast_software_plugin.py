import sys
import os
			
class teveolive_video_broadcast_software_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "search" : 'headers[server]", "regexp" : '/^TeveoLive HTTP Server$/ }
			{ "search" : 'headers[xvideowidth]", "regexp" : '/^\d+$}
			{ "search" : 'headers[xvideoheight]", "regexp" : '/^\d+$}
		]

