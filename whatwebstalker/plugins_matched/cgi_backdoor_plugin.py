import sys
import os
			
class cgi_backdoor_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : '<html><body><!-- Simple CGI backdoor by DK (http://michaeldaw.org) --><b style="color:black;background-color:#ffff66">Usage</b>: http://target.com/perlcmd.cgi?cat /etc/passwd<pre></pre></body></html>", "string" : 'Simple CGI backdoor by DK (http://michaeldaw.org)' }
		]

