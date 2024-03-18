import plugins
			
class Pluginobject_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "regexp" : "/<object/i},
			{ "module" : /<object [^>]*classid\s*=\s*['"]([^"']+)['"]/i", "offset" : "0", "name" : "classid" },
			{ "module" : /<object [^>]*classid\s*=\s*([^\s>'"]+)/i", "offset" : "0", "name" : "classid" },
			{ "string" : /<object [^>]*(codebase|codetype|type)\s*=\s*['"]([^"']+)['"]/i", "offset" : "1 },
			{ "string" : /<object [^>]*(codebase|codetype|type)\s*=\s*([^\s>'"]+)/i", "offset" : "1 },
		]
		return(self.rules)
