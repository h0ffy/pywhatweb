import plugins
			
class Pluginprice_comparison_script_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "version" : "/<td height="10%" valign="bottom" align="right"><font face="verdana" size="1" color="gray">&copy; Web Administration Panel .v([\d\.]+) by <a href="http:\/\/www.kaonsoftwares.com\/" class=" target="_blank">Kaon Softwares<\/a>. All Rights Reserved.<\/font><\/td>/" },
			{ "version" : "/<td height="19" colspan="6" align="right"><font face="verdana" size="1" color="gray">&copy; Web Administration Panel .v([\d\.]+) by <a href="http:\/\/www.kaonsoftwares.com\/" class=" target="_blank">Kaon Softwares<\/a>. All Rights Reserved.<\/font><\/td>/" },
			{ "version" : "/<td height="70%" valign="bottom" align="right"><font face="verdana" size="1" color="gray">&copy; Web Administration Panel .v([\d\.]+) by <a href="http:\/\/www.kaonsoftwares.com\/" class=" target="_blank">Kaon Softwares<\/a>. All Rights Reserved.<\/font><\/td>/" },
		]
		return(self.rules)
