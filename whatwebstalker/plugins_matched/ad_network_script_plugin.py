import plugins
			
class Pluginad_network_script_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "version" : "/<td width="100%" height="33" bgcolor="#ED7900" class="copyright">&copy; Web Administration Panel .v([\d\.]+) by <a href="http:\/\/www.kaonsoftwares.com\/" class="copyright" target="_blank">Kaon Softwares<\/a>. All Rights Reserved.<\/td>/" },
			{ "version" : "/<td height="70%" valign="bottom" align="right"><font face="verdana" size="1" color="gray">&copy; Web Administration Panel .v([\d\.]+) by <a href="http:\/\/www.kaonsoftwares.com\/" class=" target="_blank">Kaon Softwares<\/a>. All Rights Reserved.<\/font><\/td>/" },
		]
			return(self.rules)
