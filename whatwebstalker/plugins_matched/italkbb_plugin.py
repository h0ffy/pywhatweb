import sys
import os
			
class italkbb_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "version" : '/<HTML><HEAD><TITLE>[^>]+ V([\d\.]+)[\s]+<\/TITLE><STYLE type=text\/css>TD \{FONT-SIZE: 12px; LINE-HEIGHT: normal; TEXT-ALIGN: center\}<\/STYLE>/ }
			{ "regexp" : '/<P align=center><FONT size=5>welcome to phone settings<\/FONT><\/P><FORM action=\/a /i }
	]

