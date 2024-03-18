import plugins
			
class Pluginsabros.us_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "	<title>sabros.us/" },
			{ "text" : "		<p class="powered">powered by: <a title="sabros.us" href="http://sabros.us/">sabros.us</a></p>", "version" : "1.8" },
			{ "text" : "		<p class="powered">powered by: <a title="sabros.us" href="http://sourceforge.net/projects/sabrosus/">sabros.us</a></p>", "version" : "1.7" },
			{ "version" : "/	<meta name="generator" content="sabros.us ([\d\.]+)" \/>/" },
		]
	return(self.rules)
