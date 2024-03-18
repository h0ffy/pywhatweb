import plugins
			
class Plugini_catcher_console_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "   // These vars will be filled in by i-Catcher Console" },
			{ "text" : " <title>i-Catcher Console - Live view</title>" },
			{ "regexp" : "/     i-Catcher Console is Copyright [\d]{4}-[\d]{4} <a[^>]+href="http:\/\/www.icode.co.uk\/">iCode Systems<\/a>./" },
			{ "version" : "/     i-Catcher Console ([\d\.]+) is Copyright [\d]{4}-[\d]{4} <a class="footer" href="http:\/\/www.icode.co.uk\/">iCode Systems<\/a>./" },
		]
			return(self.rules)
