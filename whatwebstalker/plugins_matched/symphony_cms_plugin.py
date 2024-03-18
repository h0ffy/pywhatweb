import plugins
			
class Pluginsymphony_cms_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "	<title>Symphony | Login</title>" },
			{ "text" : "<meta name="generator" content="Symphony CMS" />" },
			{ "regexp" : "/Powered by <a[^>]+href="http:\/\/www.symphony-cms.com[\/]?">Symphony CMS<\/a>/" },
			{ "regexp" : "/Powered by <a[^>]+href="http:\/\/symphony-cms.com[\/]?">Symphony CMS<\/a>/" },
			{ "text" : "powered by <a href="http://www.symphony21.com">SYMPHONY</a>." },
			{ "text" : "Powered by <a href="http://symphony21.com/">Symphony</a>" },
			{ "text" : "Powered by <a class="symphony" href="http://symphony21.com/">Symphony</a>" },
			{ "text" : "Powered by <a class="symphony" href="http://symphony-cms.com/">Symphony</a>" },
			{ "text" : "Site powered by <a href="http://www.symphony-cms.com" class="external">Symphony</a>" },
			{ "text" : "Powered by <a href="http://symphony-cms.com/" rel="external">Symphony</a>" },
			{ "version" : "/Powered by <a[^>]+href="http:\/\/www.symphony-cms.com[\/]?">Symphony CMS ([\d\.]{1,3})<\/a>/" },
			{ "version" : "/Powered by <a[^>]+href="http:\/\/symphony-cms.com[\/]?">Symphony CMS ([\d\.]{1,3})<\/a>/" },
		]
	return(self.rules)

