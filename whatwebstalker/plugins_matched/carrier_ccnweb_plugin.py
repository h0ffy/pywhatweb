import plugins
			
class Plugincarrier_ccnweb_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "url" : "/images/CCNWeb.gif", "md5" : "724cba3a2d5b36c754d55ae0e450429a" },
			{ "text" : "<APPLET CODE="JLogin.class" ARCHIVE="JLogin.jar" MAYSCRIPT WIDTH=310 HEIGHT=185>" },
		]
		return(self.rules)
