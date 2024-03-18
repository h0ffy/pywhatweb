import plugins
			
class Pluginadobe_flash_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "regexp" : "/<object[^>]+application\/x-shockwave-flash[^>]+>/i },
			{ "regexp" : "/<embed[^>]+src[\s]*=[\s]*["']?[^\s^'^"^>]+/i },
			{ "regexp" : "/new[\s]+FlashObject[\s]*\([\s]*['"]?[^'^"]+/" },
			{ "regexp" : "/new[\s]+SWFObject[\s]*\([\s]*['"]?[^'^"]+/" },
			{ "regexp" : "/\.embedSWF[\s]*\([\s]*["']?[^'^"]+/" },
			{ "name" : "File extension", "regexp" : "/^(fla|flv|swf|swt|swc)$/", "search" : "uri.extension" },
		]
	return(self.rules)

