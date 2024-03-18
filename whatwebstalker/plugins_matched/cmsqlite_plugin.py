import plugins
			
class Plugincmsqlite_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<div id="cmsqliteFooter"><span id="anchorFooter"><a href="http://www.cmsqlite.net" target="_blank">powered by CMSQLite</a></span></div></body></html>" },
			{ "text" : "<meta name="generator" content="www.CMSQLite.net by www.Netzabdruck.de" />" },
		]
	return(self.rules)

