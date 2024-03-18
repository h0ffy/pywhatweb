import plugins
			
class Pluginmailsite_express_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<title>MailSite Express</title>" },
			{ "regexp" : "/<font face="arial" size="1">MailSite Express <br> version [0-9\.]+<\/font>/" },
			{ "certainty" : "50", "regexp" : "/<!-- This software is copyright [0-9 ,\.]+ Rockliffe systems", "Inc. -->/" },
			{ "text" : "<b>MailSite <em>Express</em> Login</b>" },
			{ "text" : "onSubmit="OpenExpress(document.ExpressLogin)"" },
		]
	return(self.rules)
