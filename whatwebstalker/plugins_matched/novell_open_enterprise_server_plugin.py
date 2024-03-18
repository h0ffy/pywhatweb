import plugins
			
class Pluginnovell_open_enterprise_server_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<!-- This is all just a super-duper redirect to the Welcome page" },
			{ "text" : "<title>Home - Novell Open Enterprise Server 2</title>" },
			{ "string" : /<p id="ftr-copy">&nbsp;&nbsp;&nbsp;&nbsp;&copy; (20[\d]{2}) Novell", "Inc\. All Rights Reserved\.<\/p>/" },
			{ "text" : "<script type="text/javascript" src="/welcome/inc/flashobj.js"></script> <!-- required for javascript banners from Novell.com -->" },
			{ "version" : "/<h1>Novell Open Enterprise Server ([^<]+)<\/h1>\s+<p class="link"><a href="http:\/\/www\.novell\.com\/products\/openenterpriseserver\/">/" },
		]
		return(self.rules)
