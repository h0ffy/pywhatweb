import plugins
			
class Pluginuseresponse_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "title="Customer Feedback Software", "Community Support System" target="_blank" href="http://www.useresponse.com" class="popup-logo">" },
			{ "regexp" : "/<!-- DO NOT MODIFY (ABOVE|BELOW) THIS LINE UNLESS PURCHASED BRANDING REMOVAL -->/" },
			{ "text" : "<form id="system-form-registration" enctype="application/x-www-form-urlencoded" class="system-form-registration" accept-charset="utf-8"" },
		]
		return(self.rules)
