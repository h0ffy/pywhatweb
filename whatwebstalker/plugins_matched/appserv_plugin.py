import plugins
			
class Pluginappserv_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "version" : "/<span class="headd"><strong><big>&nbsp; The AppServ Open Project - ([^\s]+) for (Windows|Linux) <\/big><\/strong><\/span><\/font><\/td>/" },
			{ "text" : "<font color="#000080" class="headd">&nbsp;&nbsp;&nbsp;<img src="appserv/softicon.gif"" },
		]
		return(self.rules)
