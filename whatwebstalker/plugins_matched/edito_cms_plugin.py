import plugins
			
class Pluginedito_cms_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "regexp" : "/<meta name="(g|G)enerator" content="(E|e)dito( CMS)? - www\.edito\.pl"[\s]*\/?>/" },
			{ "regexp" : "/Powered by[\s]*:?[\s]+<a[^>]+href="http:\/\/www.edito.pl[\/]?"[^>]+title="Edito CMS"[^>]*>/i },
		]
	return(self.rules)

