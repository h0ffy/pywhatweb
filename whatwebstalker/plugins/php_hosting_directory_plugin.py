import plugins


class Pluginphp_hosting_directory_plugin(plugins.Base):
    def __init__(self):
    	pass

    def start(self):
        self.rules = [
			{"version":
			    "/<title>PHP Hosting Directory ([\\d\\.]+) Powered by JnSHosts\\.com<\\/title>/"},
			{"version": "/<a href="http: \/\/www.jnshosts.com\/php-hosting-directory-([\d\.]+).php"[^>]+>PHP Hosting Directory<\/a>/" },
			{ "version" : "/<font size="6"><b>PHP Hosting Directory ([\d\.]+)<\/b><\/font>/" },
		]
	return(self.rules)
