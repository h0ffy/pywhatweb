import sys
import os
			
class php_mes_films_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : '		<title>PhpMesFilms - Administration</title>' }
			{ "text" : '		<title>PhpMesFilms - Liste</title>' }
			{ "text" : '		<title>PhpMesFilms - Fiche film</title>' }
			{ "text" : '				powered by <a href="http://phpmesfilms.dyndns.org/">PhpMesFilms</a>' }
		]

