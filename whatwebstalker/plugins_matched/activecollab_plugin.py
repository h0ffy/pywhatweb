import plugins
			
class Pluginactivecollab_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<form method="post" id="system_form_2" class="uniForm focusFirstField">" },
			{ "version" : "/if\(\!App\.data\) \{ App\.data = \{\}; \}\s+App\.data\.quick_search_url = "[^"]+";\s+App\.data\.ac_version = "([^"]+)";/" },
			{ "name" : "acpowered.gif", "url" : "/public/assets/images/acpowered.gif", "md5" : "ad6152c96454d96f7b8ec78c08bb789b"},
			{ "name" : "powered by footer", "text" : "<p id="powered_by"><a href="http://www.activecollab.com/"'},
		]
	return(self.rules)
