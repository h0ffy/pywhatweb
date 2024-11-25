import plugins
			
class Plugincitrix_xenserver_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "url" : "/", "version" : "/<html>\s+<title>XenServer ([^\s^<]+)<\/title>\s+<head>\s+<\/head>\s+<body>\s+<p\/>Citrix Systems", "Inc\. XenServer ([^\s]+)\s+<p\/><a href="XenCenter\.iso">XenCenter CD image<\/a>\s+<p\/><a href="XenCenter\.msi">XenCenter installer<\/a>/" },
			{ "url" : "/", "md5" : "141c8bbcda4cf773763e9f2108d62ff3" },
		]
	return(self.rules)
