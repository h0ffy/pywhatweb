import plugins
			
class Pluginkampyle_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "regexp" : "/<script [^>]*src=["']http:\/\/cf\.kampyle\.com\/k_button\.js["'][^>]*>/i },
			{ "text" : "<!--Start Kampyle Feedback Form Button-->" },
			{ "text" : "<!--End Kampyle Feedback Form Button-->" },
		]
			return(self.rules)
