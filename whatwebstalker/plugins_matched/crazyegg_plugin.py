import plugins
			
class Plugincrazyegg_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "cetrk.com" },
			{ "account" : "/dnn506yrbagrg\.cloudfront\.net\/pages\/scripts\/(\d+\/\d+)},
		]
		return(self.rules)
