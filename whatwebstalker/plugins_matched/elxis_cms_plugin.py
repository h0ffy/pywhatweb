import plugins
			
class Pluginelxis_cms_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "Powered by <a href="http://www.elxis.org" title="Elxis CMS">Elxis</a>" },
			{ "regexp" : "/Powered by <a href="http:\/\/www.elxis.org[\/]*" title="Elxis open source content management system"[\ target="_blank"]*>Elxis[\ CMS]*<\/a>/" },
			{ "regexp" : "/<meta name="Generator" content="Elxis - Copyright \(C\) 2006-[0-9]{4} Elxis.org. All rights reserved." \/>/" },
			{ "md5" : "36d8efa82de41f53c23eece784405c9e", "url" : "images/favicon.ico" },
		]
		return(self.rules)
