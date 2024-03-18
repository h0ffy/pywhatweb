import plugins
			
class Pluginalcatel_lucent_omniswitch_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<title>Webview Logon Page</title>" },
			{ "text" : "document.write(errMsg=="?"&nbsp;":("<u>Error</u>&nbsp;-&nbsp;" + errMsg));" },
		]
		return(self.rules)

