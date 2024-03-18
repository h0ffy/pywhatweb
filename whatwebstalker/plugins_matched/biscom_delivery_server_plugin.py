import sys
import os
			
class biscom_delivery_server_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : "<link rel="StyleSheet" href="/bds/stylesheets/fds.css" type="text/css">" },
			{ "text" : "<script src="/bds/includes/fdsJavascript.do" type="text/javascript"></script>" },
			{ "text" : "<link rel="ICON" href="/bds/images/icons/favicon.ico" />" },
			{ "url" : "/bds/images/icons/favicon.ico", "md5" : "eb05f77bf80d66f0db6b1f682ff08bee" },
		]

