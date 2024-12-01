import plugins
			
class Pluginaardvark_topsites_php_plugin(plugins.Base):
    def __init__(self):
    	super().__init__()
    def start(self):
        self.rules = [
			{ "ghdb" : "Powered by Aardvark Topsites PHP" },
			{ "regexp" : r"/Powered by <a href=\"http:\/\/www.aardvarktopsitesphp.com[^>]*>[^A]*Aardvark Topsites PHP/i" },
			{ "version" : r"/Powered by <a href=\"http:\/\/www.aardvarktopsitesphp.com\/\"><b>Aardvark Topsites PHP<\/b><\/a> ([\d\.]+)/" },
			{ "version" : r"/Powered by <a href=\"http:\/\/www.aardvarkind.com\/\">Aardvark Topsites PHP<\/a> ([\d\.]+)/" },
		]
        return self.rules