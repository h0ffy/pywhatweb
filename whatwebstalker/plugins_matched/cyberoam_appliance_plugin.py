import sys
import os
			
class cyberoam_appliance_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "url" : '/images/loginbox_left_logo.jpg", "md5" : 'ecb82a4554f2ef5eefd06040cdae9872" }
			{ "url" : '/images/session_ex.jpg", "md5" : '7241a011a6057cdb723eccbf178b0e3a" }
			{ "url" : '/corporate/webpages/sessionexpired.jsp", "version" : '/<font face="arial" size=2 color=white>([^<]+ build [^<]+)<\/font>/ }
			{ "text" : '<td align="right" class="arial12whitebold">Log on to:&nbsp; </td>' }
			{ "text" : '<INPUT TYPE=HIDDEN NAME="js_autodetect_results" VALUE="SMPREF_JS_OFF">' }
			{ "text" : '<noscript><font class="arial12whitebold">JavaScript must be enabled in order for you to use cyberoam admin console.</font></noscript><br>' }
			{ "text" : '<!-- PUT THE LOGIC OF YOUR PAGE HERE -->' }
	]

