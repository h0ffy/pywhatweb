import plugins
			
class Plugincpassman_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<title>Collaborative Passwords Manager</title>" },
			{ "version" : "/<a href="http:\/\/cpassman.org[\/]?" target="_blank">cPassMan<\/a> ([^\ ]+)/" },
			{ "text" : "<a rel="license" href="http://creativecommons.org/licenses/by-nc-nd/3.0/" title="Collaborative Passwords Manager by Nils Laumaill&#233; is licensed under a Creative Commons Attribution-Noncommercial-No Derivative Works 3.0 License" target="_blank">" },
		]
		return(self.rules)
