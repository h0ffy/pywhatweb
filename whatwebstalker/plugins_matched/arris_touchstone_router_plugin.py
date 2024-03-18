import sys
import os
			
class arris_touchstone_router_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "certainty" : '25", "search" : 'headers[server]", "regexp" : '/^NET-DK\/[\d\.]+$/ }
			{ "url" : '/logo_t.gif", "md5" : '634c757842b122c6cd4458051ab0ed12" }
			{ "regexp" : '/<br><center>&#169 Copyright (2004-)?20[\d]{2}", "ARRIS Group", "Inc\.", "All rights reserved\.<\/center><\/BODY><\/HTML>/ }
			{ "text" : '<FRAME name="tabs" src="/menu.htm?3" frameborder="0" scrolling="no">' }
			{ "url" : '/vers.htm", "version" : '/<BR> SW_REV: ([^\s^<]+)<BR> MODEL: ([^\s^<]+)  <\/TD><\/TR><tr vAlign=top><td width="170">Product Type:<\/td>/ }
			{ "url" : '/cgi-bin/vers_cgi", "version" : '/HW_REV: [^<]+<br>[\s]+VENDOR: Arris Interactive", "L\.L\.C\.<br>[\s]+BOOTR: [^<]+<br>[\s]+SW_REV: ([^\s^<]+)<br>[\s]+MODEL: ([^\s^<]+)<\/td>/ }
			{ "url" : '/cgi-bin/vers_cgi", "firmware" : '/HW_REV: [^<]+<br>[\s]+VENDOR: Arris Interactive", "L\.L\.C\.<br>[\s]+BOOTR: ([^<^\s]+)<br>[\s]+SW_REV: ([^\s^<]+)<br>[\s]+MODEL: ([^\s^<]+)<\/td>/ }
			{ "url" : '/cgi-bin/vers_cgi", "model" : '/HW_REV: [^<]+<br>[\s]+VENDOR: Arris Interactive", "L\.L\.C\.<br>[\s]+BOOTR: [^<]+<br>[\s]+SW_REV: ([^\s^<]+)<br>[\s]+MODEL: ([^\s^<]+)<\/td>/", "offset" : '1 }
			{ "url" : '/vers.htm", "model" : '/<BR> SW_REV: ([^\s^<]+)<BR> MODEL: ([^\s^<]+)  <\/TD><\/TR><tr vAlign=top><td width="170">Product Type:<\/td>/", "offset" : '1 }
	]

