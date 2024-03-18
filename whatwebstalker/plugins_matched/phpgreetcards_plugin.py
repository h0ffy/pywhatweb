import plugins
			
class Pluginphpgreetcards_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<td align="right"><font color="#b8c2cc">Powered by <a href="http://www.w2b.ru/webapplications/index.php" target="_blank">phpGreetCards</a>", "" },
			{ "text" : "<td align="right"><font color="#b8c2cc">Powered by <a href="http://www.w2bpm.com/index.php?cat=phpGreetCards" target="_blank">phpGreetCards</a>", "" },
		]
		return(self.rules)
