import plugins
			
class Plugintrendnet_print_server_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<frame name="Banner" scrolling="no" noresize target="Inhalt" src="head.htm">" },
			{ "url" : "/head.htm", "model" : "/<td width="415" align="right" background="bg.gif" valign="bottom"><b><font size="2" color="#FFFFFF">[^<]+ Print Server<br>([^<]{5,15})<\/font><\/b><\/td>/" },
			{ "certainty" : "25", "version" : "/^PRINT_SERVER WEB ([\d\.]+)$/", "search" : "headers[server]" },
		]
		return(self.rules)

