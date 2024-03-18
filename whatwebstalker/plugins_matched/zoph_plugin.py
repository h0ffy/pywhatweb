import plugins
			
class Pluginzoph_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<li class="selected"><a href="zoph.php">home</a></li><li ><a href="albums.php">albums</a></li><li ><a href="categories.php">categories</a></li><li >" },
			{ "text" : "<title>Zoph - Home</title>" },
		]
	return(self.rules)

