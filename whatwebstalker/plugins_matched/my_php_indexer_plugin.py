import plugins
			
class Pluginmy_php_indexer_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "version" : "/<!--Copyright--><a target="_blank" class="l" href="http:\/\/www.mafiatic.com">Powered by My PHP Indexer ([\d\.]+) \| Copyright &copy; [0-9]{4}\-[0-9]{4} Mafiatic Inc.<\/a><!--Copyright-->/" },
		]
		return(self.rules)

