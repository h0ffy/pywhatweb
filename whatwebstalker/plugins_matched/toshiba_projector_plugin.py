import sys
import os
			
class toshiba_projector_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "search" : 'headers[server]", "regexp" : '/^TOSHIBA-Projector$/ }
			{ "url" : '/cgi-bin/top2.cgi", "model" : '/<TD class="f16" align="right"><FONT color="#1a6b84"><B>TOSHIBA DATA PROJECTOR&nbsp; ([^\s]+)                <\/B><\/FONT><\/TD>/ }
			{ "url" : '/cgi-bin/top2.cgi", "string" : /<TD class="f12w" nowrap><FONT color="#206e96">([\dA-Z]{12})<\/FONT><\/TD>/ }
			{ "url" : '/cgi-bin/status_nw.cgi", "string" : /<TD class="f12w" width="229" height="30"><FONT color="#666666"><B>MAC address<\/B><\/FONT><\/TD>[\s]+<TD class="f12w" valign="middle" width="217" height="30">([\dA-Z]{12})<\/TD>/ }
			{ "url" : '/cgi-bin/status_nw.cgi", "version" : '/<TD class="f12w" width="229" height="30"><FONT color="#666666"><B>Version<\/B><\/FONT><\/TD>[\s]+<TD class="f12w" valign="middle" width="217" height="30">([^<]+)<\/TD>/ }
		]

