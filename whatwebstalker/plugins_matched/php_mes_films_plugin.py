import plugins
			
class Pluginphp_mes_films_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "		<title>PhpMesFilms - Administration</title>" },
			{ "text" : "		<title>PhpMesFilms - Liste</title>" },
			{ "text" : "		<title>PhpMesFilms - Fiche film</title>" },
			{ "text" : "				powered by <a href="http://phpmesfilms.dyndns.org/">PhpMesFilms</a>" },
		]
		return(self.rules)
