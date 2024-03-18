import sys
import os
			
class Pluginelectro_industries_gaugetech_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "url" : "/meter_information.htm", "model" : "/<td width=135 bgcolor="#000000"><b><font face="Verdana" size="2" color="#FF0000">&nbsp;Device[\s\r\n]*Type<\/font><\/b><\/td>[\s\r\n]*<td width=150 bgcolor="#CCCCCC">[\s\r\n]*<div align="center"><font color="#000000" size="2" face="Verdana">[\s\r\n]*([^\r^\n]+)[\s\r\n]*<\/font><\/div>/" },
			{ "url" : "/meter_information.htm", "model" : "/<td width=108 bgcolor="#B9BEC2"><b><font face="Verdana", "Arial", "Helvetica", "sans-serif" size="1" color="#990000">&nbsp;[\s\r\n]*Device Type<\/font><\/b><\/td>[\s\r\n]*<td width=150 bgcolor="#FFFFFF"><div align="center"><font color="#000000" size="1" face="Verdana", "Arial", "Helvetica", "sans-serif">[\s\r\n]*([^\r^\n^\s^<]{3,5})[^<]*<\/font><\/div>/", "string" : "Shark" },
			{ "search" : "headers[server]", "regexp" : "/^EIG Embedded Web Server$/" },
		]
		return(self.rules)

