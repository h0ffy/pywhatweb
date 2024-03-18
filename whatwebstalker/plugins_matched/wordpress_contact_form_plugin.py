import plugins
			
class Pluginwordpress_contact_form_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "version" : "/<input type="hidden" name="_wpcf([\d\.]+)" value="1" \/>/" },
		]
		return(self.rules)
