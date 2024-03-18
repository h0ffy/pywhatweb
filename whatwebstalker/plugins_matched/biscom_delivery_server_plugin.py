import plugins
			
class Pluginbiscom_delivery_server_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<link rel="StyleSheet" href="/bds/stylesheets/fds.css" type="text/css">" },
			{ "text" : "<script src="/bds/includes/fdsJavascript.do" type="text/javascript"></script>" },
			{ "text" : "<link rel="ICON" href="/bds/images/icons/favicon.ico" />" },
			{ "url" : "/bds/images/icons/favicon.ico", "md5" : "eb05f77bf80d66f0db6b1f682ff08bee" },
		]
	return(self.rules)

