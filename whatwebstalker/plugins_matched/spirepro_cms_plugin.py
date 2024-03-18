import plugins
			
class Pluginspirepro_cms_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<script xmlns:a="http://www.1stomni.com/spire/aml" type="text/javascript"" },
			{ "text" : "<meta name="Spire-Last-Modified" content="" },
			{ "regexp" : "/<meta name="Spire-Editor" content="([^"]+)">/" },
			{ "string" : /^SpirePRO CMS v([\d\.]+ \(Microkernel v[\d]+; CMS Server v[\d]+\)) /", "search" : "headers[x-generator]" },
			{ "string" : /^SpirePRO CMS v([\d\.]+ \(Microkernel v[\d]+; CMS Server v[\d]+\)) /", "search" : "headers[generator]" },
			{ "regexp" : "/^SpirePRO CMS/", "search" : "headers" },
		]
	return(self.rules)
