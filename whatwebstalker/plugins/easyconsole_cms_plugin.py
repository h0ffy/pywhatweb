import plugins
			
class Plugineasyconsole_cms_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "certainty" : "75", "ghdb" : "Powered by EasyConsole CMS" inurl:"easyconsole.cfm" ext:cfm" },
			{ "regexp" : "/<!-- Powered by EasyConsole CMS", "Copyright DW Dynamic Works LTD 2003 - 20[\d]{2} - http:\/\/www.easyconsole.com -->/" },
		]
	return(self.rules)
