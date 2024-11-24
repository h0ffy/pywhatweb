import plugins


class Plugincontentteller_cms_plugin(plugins.Base):
    def __init__(self):
    	pass

    def start(self):
        self.rules = [
			{"text": "<meta name="generator" content="Esselbach Contentteller CMS" />"},
			{"version": "/Powered by <a href="http: \/\/www.contentteller.com">Contentteller&reg; (Business Edition|Standard Edition)<\/a><img src="index.php\?ct=core&amp;action=tasks" alt=" \/>/" },
		]
	return(self.rules)
