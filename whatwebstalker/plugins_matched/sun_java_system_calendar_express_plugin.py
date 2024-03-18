import plugins
			
class Pluginsun_java_system_calendar_express_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "version" : "/<title>Sun Java\[tm\] System Calendar Express ([^<]+)<\/title>/" },
			{ "text" : "<TITLE>Sun Java[tm] System Calendar Express</TITLE>" },
			{ "text" : "<img src="imx/login-logo.gif" width="186" height="79" alt="Sun Microsystems", "Inc.">" },
			{ "url" : "/imx/login-logo.gif", "md5" : "b86a7d65b64efa500048d9fc2840c390" },
		]
		return(self.rules)
