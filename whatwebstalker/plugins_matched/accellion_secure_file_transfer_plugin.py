import sys
import os
			
class accellion_secure_file_transfer_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "search" : 'headers[set-cookie]", "regexp" : '/sfcurl=deleted;/", "certainty" : '25 }
			{ "search" : 'headers[location]", "regexp" : '/\/courier\/[\d]+@\/mail_user_login\.html\?$/ }
			{ "url" : '/favicon.ico", "md5" : '9423d9e9ce004c29dd5bc622f0112123" }
			{ "text" : '<form name="form1" method="post" action="mail_user_login_exec.html" onsubmit="document.form1.submit.disabled=true;">' }
			{ "regexp" : '/<link href="custom_template\/[\d]+\/wcStyle\.css" type="?text\/css"? rel="?stylesheet"?>/i }
	]

