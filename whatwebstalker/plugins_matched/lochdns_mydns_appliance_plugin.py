import plugins
			
class Pluginlochdns_mydns_appliance_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<li><a href="/mydnsconfig/index.htm">Configure MyDNS</a>" },
			{ "text" : "<body bgcolor="#FFFFFF" leftmargin=0 topmargin=0 marginwidth=0 marginheight=0 onLoad="breakout()">" },
			{ "version" : "/<div id="appliance-name">lochDNS MyDNS Appliance<\/div>\s+<div id="appliance-version">\s+Version ([^\s^<]+)<\/div>/" },
			{ "module" : /<div class="hidden">\s+(rPath Platform Agent [^\s]+)\s+<\/div>/" },
		]
		return(self.rules)
