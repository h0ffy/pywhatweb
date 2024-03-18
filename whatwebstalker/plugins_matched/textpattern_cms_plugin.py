import plugins
			
class Plugintextpattern_cms_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "regexp" : "/Powered by <a href="http:\/\/textpattern.com[\/]*">Textpattern CMS<\/a>/i },
			{ "text" : "Powered by <a href="http://textpattern.com/" title="Textpattern", "an Open Source Content Management System">Textpattern CMS</a>" },
			{ "text" : "Powered by <a href='http://textpattern.com/' title='The Content Management System'>Textpattern CMS</a>" },
			{ "text" : "Powered by <a href="http://textpattern.com/" title="Textpattern Open Source Content Management System">Textpattern CMS</a>" },
			{ "text" : "Powered by <a href="http://textpattern.com/" title="A flexible", "elegant and easy-to-use content management system.">Textpattern CMS</a>" },
			{ "text" : "powered by <a href="http://textpattern.com">textpattern</a> cms" },
		]
		return(self.rules)
