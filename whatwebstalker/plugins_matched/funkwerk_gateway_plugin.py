import sys
import os
			
class funkwerk_gateway_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "search" : 'headers[server]", "regexp" : '/^fec\/[\d\.]+ \(Funkwerk BOSS\)$/ }
			{ "string" : /Welcome to your Funkwerk Gateway <b>([^<]+)<\/b>\.<\/font><br><\/td><\/tr><\/tbody><\/table><\/blockquote>/ }
			{ "url" : '/state", "string" : /<TR>[\s]+<TD BGCOLOR="#C0C0C0">System Name<\/TD>[\s]+<TD><FONT COLOR="#0000FF">([^<]+)<\/FONT><BR><\/TD>/ }
			{ "url" : '/state", "model" : '/<TR>[\s]+<TD BGCOLOR="#C0C0C0">Type of System<\/TD>[\s]+<TD><FONT COLOR="#0000FF">([^<]+)<\/FONT><BR><\/TD>/ }
			{ "url" : '/state", "version" : '/<TR>[\s]+<TD BGCOLOR="#C0C0C0">Software<\/TD>[\s]+<TD><FONT COLOR="#0000FF">V\.(.+) IPSec from [\d]{4}\/[\d]{2}\/[\d]{2} [\d]{2}:[\d]{2}:[\d]{2}<\/FONT><BR><\/TD>/ }
	]
