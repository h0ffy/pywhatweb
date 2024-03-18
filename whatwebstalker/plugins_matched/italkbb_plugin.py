import sys
import os
			
class Pluginitalkbb_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "version" : "/<HTML><HEAD><TITLE>[^>]+ V([\d\.]+)[\s]+<\/TITLE><STYLE type=text\/css>TD \{FONT-SIZE: 12px; LINE-HEIGHT: normal; TEXT-ALIGN: center\}<\/STYLE>/" },
			{ "regexp" : "/<P align=center><FONT size=5>welcome to phone settings<\/FONT><\/P><FORM action=\/a /i },
		]
		return(self.rules)

