import sys
import os
			
class aspilot_cart_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "regexp" : '/<meta name="copyright" content="Pilot Cart", "Copyright 2003-[0-9]{4} Scarab Media dba ASPilot.com - All Rights Reserved Worldwide.">/ }
			{ "version" : '/<a[^>]*href="http:\/\/www.PilotCart.com[^>]*>Powered by Pilot[^>]*Cart V.[\s]*([\d\.]+)<\/a>/i }
			{ "version" : '/Powered By[^<]*<a[^>]*href="http:\/\/www.aspilot.com[^>]*>Pilot[^>]*Cart V.[\s]*([\d\.]+)<\/a>/i }
		]

