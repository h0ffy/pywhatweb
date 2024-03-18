import sys
import os
			
class Plugincgi_backdoor_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<html><body><!-- Simple CGI backdoor by DK (http://michaeldaw.org) --><b style="color:black;background-color:#ffff66">Usage</b>: http://target.com/perlcmd.cgi?cat /etc/passwd<pre></pre></body></html>", "string" : "Simple CGI backdoor by DK (http://michaeldaw.org)" },
		]
		return(self.rules)

