import plugins
			
class Pluginsophos_email_appliance_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[server]", "regexp" : "/^Sophos Email Appliance$/" },
			{ "search" : "headers", "string" : /[Ss]erver: Sophos Email Appliance\r?\n.+Location: https?:\/\/([^\/]+)/m },
			{ "text" : "<td class="logincontent" valign="top"><a href="http://www.sophos.com"><img src="images/logo_sophos.gif" border="0" alt="Email Appliance"></a></td>" },
			{ "text" : "<title>Sophos Email Appliance</title>", "certainty" : "75 },
			{ "text" : "<!-- end main content -->", "certainty" : "25 },
		]
	return(self.rules)

