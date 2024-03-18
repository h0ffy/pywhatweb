import sys
import os
			
class Pluginoscommerce_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "regexp" : "/<[^>]+(src|href)\s*=\s*[^>]\bosCsid=([a-z0-9]{26}|[a-z0-9]{32})/" },
			{ "certainty" : "25", "text" : "The Exchange Project - Community Made Shopping!'},
			{ "string" : "warning", "text" : "<td class="messageStackWarning"><img src="images/icons/warning.gif"'},
			{ "version" : "/<img src="images\/oscommerce.png" border="0" alt="osCommerce ([^"]+)"/", "url" : "/admin/login.php","name" : "admin page version" },
			{ "text" : "Powered by <a href="http://www.oscommerce.com" target="_blank">osCommerce</a>" },
			{ "search" : "headers[set-cookie]", "text" : "cookie_test=please_accept_for_session;" },
			{ "search" : "headers[set-cookie]", "regexp" : "/osCsid=[a-z0-9]{32};/" },
		]

