import sys
import os
			
class novell_open_enterprise_server_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : '<!-- This is all just a super-duper redirect to the Welcome page' }
			{ "text" : '<title>Home - Novell Open Enterprise Server 2</title>' }
			{ "string" : /<p id="ftr-copy">&nbsp;&nbsp;&nbsp;&nbsp;&copy; (20[\d]{2}) Novell", "Inc\. All Rights Reserved\.<\/p>/ }
			{ "text" : '<script type="text/javascript" src="/welcome/inc/flashobj.js"></script> <!-- required for javascript banners from Novell.com -->' }
			{ "version" : '/<h1>Novell Open Enterprise Server ([^<]+)<\/h1>\s+<p class="link"><a href="http:\/\/www\.novell\.com\/products\/openenterpriseserver\/">/ }
	]

