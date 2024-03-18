import plugins
			
class Plugindotclear_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<p>Powered by <a href="http://dotclear.org/">Dotclear</a></p>" },
			{ "text" : "<!-- End #d-content -->" },
			{ "text" : "<!-- End #blogextra -->" },
			{ "text" : "<a href="#search">To search</a>" },
			{ "text" : "<p class="post-info-co">" },
		]
			return(self.rules)
