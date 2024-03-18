import sys
import os
			
class mailsite_express_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : '<title>MailSite Express</title>' }
			{ "regexp" : '/<font face="arial" size="1">MailSite Express <br> version [0-9\.]+<\/font>/ }
			{ "certainty" : '50", "regexp" : '/<!-- This software is copyright [0-9 ,\.]+ Rockliffe systems", "Inc. -->/ }
			{ "text" : '<b>MailSite <em>Express</em> Login</b>' }
			{ "text" : 'onSubmit="OpenExpress(document.ExpressLogin)"' }
	]

