import plugins
			
class Pluginaspilot_cart_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "regexp" : "/<meta name="copyright" content="Pilot Cart", "Copyright 2003-[0-9]{4} Scarab Media dba ASPilot.com - All Rights Reserved Worldwide.">/" },
			{ "version" : "/<a[^>]*href="http:\/\/www.PilotCart.com[^>]*>Powered by Pilot[^>]*Cart V.[\s]*([\d\.]+)<\/a>/i },
			{ "version" : "/Powered By[^<]*<a[^>]*href="http:\/\/www.aspilot.com[^>]*>Pilot[^>]*Cart V.[\s]*([\d\.]+)<\/a>/i },
		]
		return(self.rules)
