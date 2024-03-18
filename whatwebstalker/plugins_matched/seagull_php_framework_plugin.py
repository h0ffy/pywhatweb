import sys
import os
			
class seagull_php_framework_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : "    <meta name="generator" content="Seagull Framework" />" },
			{ "regexp" : "/    Powered by <a href="http:\/\/seagullproject.org[\/]*" title="Seagull framework homepage">Seagull PHP Framework<\/a>/" },
			{ "regexp" : "/        var SGL_JS_SESSID[\s]*=/" },
			{ "regexp" : "/<link rel="help" href="http:\/\/trac.seagullproject.org[\/]*" title="Seagull Documentation." \/>/" },
			{ "text" : "    <title>Seagull Framework :: Installation</title>        <meta http-equiv="Content-Type" content="text/html; charset=iso-8859-15" />" },
			{ "url" : "/themes/default/images/logo.png", "md5" : "4986dcbd7b531e29c58b5808b1f8cdd3" },
			{ "version" : "/    Powered by <a href="http:\/\/seagullproject.org[\/]?" title="Seagull PHP Framework">Seagull PHP Framework<\/a> v([\d\.]+)/" },
		]

