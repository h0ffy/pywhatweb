import plugins
			
class Pluginphotopost_php_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<title>PhotoPost Administration Menu</title>" },
			{ "text" : "<frame name="mainFrame"  src="adm-misc.php?admact=mainmenu" scrolling="yes" frameborder="0" marginwidth="0" marginheight="0" border="no" />" },
			{ "text" : "Powered by: <a target="_blank" href="http://www.photopost.com">PhotoPost</a> PHP<br />" },
			{ "text" : "Powered by: <a target="_blank" href="http://www.photopost.com">PhotoPost</a> PHP vB3 Enhanced<br />" },
			{ "text" : " - Powered by PhotoPost</title>" },
		]
	return(self.rules)

