import plugins
			
class Pluginanyinventory_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "		<title>anyInventory: Top</title>" },
			{ "regexp" : "/					 you have inventoried <b>[0-9]*<\/b>  items with <a href="http:\/\/anyinventory.sourceforge.net\/">anyInventory", "the most flexible and powerful web-based inventory system<\/a>/" },
			{ "version" : "/								anyInventory ([\d\.]+)/" },
		]
		return(self.rules)
