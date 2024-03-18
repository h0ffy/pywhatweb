import plugins
			
class Pluginphpkit_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "regexp" : "/<meta name="generator" content="PHPKIT WCMS \- Web Content Managment System \- mxbyte GbR copyright [\d]{4}\-[\d]{4}" \/>/" },
			{ "regexp" : "/<meta name="generator" content="PHPKIT WCMS Web Content Management System" \/>/" },
			{ "text" : "<meta name="author" content="PHPKIT WCMS - Web Content Management System - Copyright mxbyte GbR" />" },
			{ "text" : "<div id="pkcopyright"><a class="none" href="http://www.phpkit.com">PHPKIT ist eine eingetragene Marke der mxbyte GbR &copy;" },
			{ "text" : "<meta name="description" content="PHPKIT", "WCMS", "Web Content Management System", "Administration" />", "module" : "Admin Page" },
		]
	return(self.rules)
