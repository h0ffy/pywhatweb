import sys
import os
			
class netbotz_network_monitoring_device_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "regexp" : '/<TITLE>NetBotz( Network Monitoring) Appliance - [^<]*<\/TITLE>/ }
			{ "text" : '<LINK REL="StyleSheet" TYPE="text/css" HREF="/netbotz.css">' }
			{ "text" : '<!-- Launch the NetBotz Applications.  This will require Java 1.3.0 OR ANYTHING NEWER -->' }
			{ "text" : '<a href="http://www.netbotz.com" target="_top"><img border="0" src="/colorlogo.gif"></a>' }
			{ "text" : '	<TITLE>Device Status Summary Page</TITLE>' }
			{ "url" : '/statusHeader.html", "version" : '/<a href="http:\/\/updates.netbotz.com\/releases\/([\d\.]+)\/install.html" target="_instAV">\(Install Advanced View Application\)<\/a>/ }
	]

