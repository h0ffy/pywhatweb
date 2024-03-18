import sys
import os
			
class uebimiau_webmail_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "version" : "/					<td class="info">Uebimiau Webmail v([^<]{1,15})<\/td>/" },
			{ "text" : "<title>Uebimiau ( Installer )</title>", "module" : "Install Page" },
			{ "text" : "<p>You are about to re-install Uebimiau Webmail on you system.<br>Thanks to log with your UebiMiau Admin ID and password to continue.</p>", "module" : "Install Page" },
			{ "text" : "<script type="text/javascript" src="themes/default/js/webmail.js"></script>" },
			{ "text" : "<meta name="keywords" content="uebimiau,tdah,uebimiau,webmail,email,mail,client,application,pop3,php,open     source,free,sourceforge,development" />", "certainty" : "75 },
		]

