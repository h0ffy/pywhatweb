import sys
import os
			
class solarwinds_network_performance_monitor_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "string" : "Broken", "text" : "<b>Cannot access main SQL Server database.</b><br><br><b>Connection</b>" },
			{ "text" : "<TITLE>SolarWinds Network Management</TITLE>" },
			{ "text" : "<TD Class=PageHeader>Network Performance Monitor</TD>" },
			{ "text" : "<link rel="stylesheet" type="text/css" href="/SolarWinds.css">", "version" : "Old" },
			{ "regexp" : "/<title>[\r\n]*	Orion Network Performance Monitor[\r\n]*<\/title>/" },
			{ "text" : "<link rel="stylesheet" type="text/css" href="/SolarWinds.css" />" },
			{ "text" : "<!-- Stylesheets left here to support legacy resources -->" },
			{ "text" : "<img src="/NetPerfMon/images/SolarWinds.Logo.gif" alt="Site Logo"/>" },
			{ "text" : "<img src="../NetPerfMon/images/SolarWinds.Logo.jpg" border=0>" },
			{ "text" : "<img src="/NetPerfMon/images/SolarWinds.Logo.jpg" border=0>" },
			{ "text" : "<a href="/Login.asp"><u><b>Retry Login<b><u></a>" },
			{ "version" : "/<div id="footer">[^S]*SolarWinds Orion Network Performance Monitor ([^&]+)&copy; 1995-[0-9]{4} All Rights Reserved[^<]*<\/div>/" },
		]

