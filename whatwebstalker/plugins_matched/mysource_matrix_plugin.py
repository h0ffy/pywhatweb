import plugins
			
class Pluginmysource_matrix_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<p class="right">Powered by <a href="http://www.squiz.co.uk/mysource_matrix" target="_blank">MySource Matrix</a></p>" },
			{ "text" : "class="squiz">Powered by MySource Matrix - a Squiz.net initiative</a> </div>  </div>" },
			{ "text" : "<p>Powered By MySource Matrix - A Squiz.net  Initiative</p>" },
			{ "text" : "  MySource", "MySource Matrix and Squiz.net are registered Trademarks of Squiz Pty Ltd" },
		]
		return(self.rules)
