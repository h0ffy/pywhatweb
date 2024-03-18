import plugins
			
class Pluginavaya_aura_utility_server_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<span class="vmsTitle">Avaya Aura&#8482;&nbsp;Utility Server</span>" },
			{ "text" : "<div id="topBar"><div id="topBarLeft"><a href="#" class="helpAndExit" onclick="window.open(\'/webhelp/Base/Utility_toc.htm" },
		]
	return(self.rules)
