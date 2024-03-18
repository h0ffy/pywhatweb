import plugins
			
class Pluginopenkm_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<form name="login" method="post" action="j_security_check" onsubmit="setCookie()">" },
			{ "regexp" : "/<title>OpenKM Login<\/title>[\s]+<\/head>[\s]+<body onload="document\.forms\[0\]\.elements\[0\]\.focus\(\)">/" },
		]
		return(self.rules)
