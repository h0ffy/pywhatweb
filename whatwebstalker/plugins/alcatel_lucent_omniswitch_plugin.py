import plugins
			
class Pluginalcatel_lucent_omniswitch_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<title>Webview Logon Page</title>" },
<<<<<<< HEAD
			{ "text" : "document.write(errMsg=="?"&nbsp;":("<u>Error</u>&nbsp;-&nbsp;" + errMsg));" },
		]
	return(self.rules)
=======
			{ "text" : "document.write(errMsg==\"?\"&nbsp;\":(\"<u>Error</u>&nbsp;-&nbsp;\" + errMsg));" },
		]
        return(self.rules)
>>>>>>> parent of c1541b4c (Merge branch 'main' of https://github.com/h0ffy/pywhatweb)
