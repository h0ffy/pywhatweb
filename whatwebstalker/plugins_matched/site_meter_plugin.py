import plugins
			
class Pluginsite_meter_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "account" : "/<script [^>]*src=["']http:\/\/[^>]+sitemeter\.com\/js\/counter\.js\?site=([^"^'^>]+)[^>]*>/i },
			{ "account" : "/<img [^>]*src=["']http:\/\/[^>]+sitemeter\.com\/meter\.asp\?site=([^"^'^>]+)[^>]*>/i },
			{ "certainty" : "25", "text" : "<!-- Site Meter -->" },
			{ "regexp" : "/<!-- Copyright \(c\)20[\d]{2} Site Meter -->/" },
		]
			return(self.rules)
