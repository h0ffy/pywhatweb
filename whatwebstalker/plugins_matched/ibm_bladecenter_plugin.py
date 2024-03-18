import sys
import os
			
class ibm_bladecenter_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "url" : '/shared/ibmbch.png", "md5" : 'c24b87d43f33783193e98ac25fd016ee" }
			{ "url" : '/shared/ibmbcs.png", "md5" : 'f4f76aeba5ba885fac1d4e5bbe535f0f" }
			{ "string" : /<h1><img src="\/shared\/ibmbc[^\s^\.]+\.png" alt="IBM BladeCenter ([^\s^"]+) Advanced Management Module" border="0" \/><\/h1>/ }
			{ "text" : '<h1><img src="/shared/ibmbc.png" alt="IBM BladeCenter Advanced Management Module" border="0" /></h1>' }
			{ "text" : '<img id="logo" src="/shared/banner_logo.png" alt="IBM" width="41" height="15" />' }
			{ "text" : '<form method="post" name="login" action="/shared/userlogin.php"><input type="hidden" name="SESSID"' }
			{ "text" : '<img src="/shared/banner_left.jpg" width=110 height=53 alt="banner" />' }
		]

