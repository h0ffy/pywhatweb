import plugins


class Pluginphpmysport_plugin(plugins.Base):
    def __init__(self):
    	pass

    def start(self):
        self.rules = [
			{"text": "Powered by phpMySport <a href="http: // phpmysport.sourceforge.net" title="phpMySport">"},
			{"text": "<a href="http: // phpmysport.sourceforge.net" title="phpMySport">", "certainty": "25 },
			{ "text" : "<div id="footer">R&eacute;alisation phpMySport" },
			{ "text" : "/tpl_image/by_phpmysport.gif" border="0"" },
		]
	return(self.rules)
