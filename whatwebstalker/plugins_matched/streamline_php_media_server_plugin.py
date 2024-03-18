import plugins
			
class Pluginstreamline_php_media_server_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "                <div style="font-size: 10pt">A PHP Streaming Media Server</div>" },
			{ "text" : "    <title>Streamline Media Installation Wizard</title>" },
			{ "text" : "            &copy; 2003-2010 Streamline" },
			{ "md5" : "10bf2f9eff6be7d5efd25ce6b70099f4", "url" : "images/streamline.png" },
		]
	return(self.rules)

