import sys
import os
			
class eticket_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "regexp" : "/<td><a href="(http:\/\/)?www\.eticketsupport\.com" target="_blank">Powered by eTicket<\/a><\/td>/" },
			{ "text" : "<div class="pre-footer">Support Ticket System</div>" },
			{ "text" : "<link rel="stylesheet" href="themes/eticket/style.css" type="text/css">" },
			{ "text" : "<p><strong>Note:</strong> &quot;/path/to/automail.pl&quot; should be the <a href="http://en.wikipedia.org/wiki/Full_path">full path</a>" },
		]

