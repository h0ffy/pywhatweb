import plugins
			
class Pluginopen_realty_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "version" : "/<title>Open-Realty ([\d\.]+) - [^<]+<\/title>/" },
			{ "text" : "<meta name="Generator" content="Open-Realty" />" },
			{ "text" : "Powered by <a href="http://www.open-realty.org"><b>Open-Realty</b></a>" },
			{ "text" : "Powered by <a href="http://open-realty.org" title="Open-Realty&reg;" rel="external">Open-Realty</a>" },
			{ "text" : "<!--Open-Realty is distributed by Transparent Technologies and is Licensed under the Open-Realty License. See http://www.open-realty.org/license_info.html for more information.-->" },
		]
		return(self.rules)
