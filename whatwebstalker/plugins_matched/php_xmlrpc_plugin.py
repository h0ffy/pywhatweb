import plugins
			
class Pluginphp_xmlrpc_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<meta name="generator" content="XML-RPC for PHP" />" },
			{ "version" : "/<div class="footer">Generated using PHP-XMLRPC ([\d\.]+)<\/div>/" },
		]
		return(self.rules)
