import plugins
			
class Pluginslingbox_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[set-cookie]", "regexp" : "/_sling_skey=[^;]+/" },
			{ "version" : "/<!-- Footer start -->\s+<div id="footer_center">\s+<p>Portal Version:&nbsp;([^,]+)", "Plugin Version:&nbsp;/" },
		]
	return(self.rules)
