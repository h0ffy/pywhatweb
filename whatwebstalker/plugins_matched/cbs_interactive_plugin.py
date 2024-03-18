import plugins
			
class Plugincbs_interactive_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "regexp" : "/<script[^>]+ src="http:\/\/dw\.com\.com\/js\/dw\.js"><\/script>/" },
			{ "account" : "/<script>DW.pageParams = \{siteId:'([^']+)'\};DW.clear\(\);<\/script>/" },
			{ "account" : "/<img src="http:\/\/dw\.com\.com\/clear\/c\.gif\?sid=([^"^\s^>^&]+)/" },
		]
		return(self.rules)
