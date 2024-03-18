import plugins
			
class Pluginlog1_cms_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<meta http-equiv="Generator" content="log1_cms" />" },
			{ "text" : "<!-- please do not deleate info below", "thank you -->" },
			{ "text" : "<p>Powered by <a href="http://log1cms.sourceforge.net" target="_blank"> Log1 CMS</a></p>" },
			{ "text" : "<title>log1 cms: Login as Admin to</title>" },
			{ "text" : "<link href="engine/styles/login.css.php" rel="stylesheet" type="text/css" />" },
			{ "text" : "<img src="engine/images/logo.gif" alt="log1 CMS logo"/>" },
		]
		return(self.rules)
