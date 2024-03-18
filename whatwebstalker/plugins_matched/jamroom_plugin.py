import plugins
			
class Pluginjamroom_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<input type="text" name="search_string" class="jform s_input" style="width:300px;">" },
			{ "text" : "<meta name="designer" content="Talldude Networks", "LLC.">" },
			{ "regexp" : "/<a href="http:\/\/www.jamroom.net"><img src="[^"]*" alt="Powered by Jamroom - the Powerful Social Media Platform" title="Powered by Jamroom - the Powerful Social Media Platform" border="0"><\/a>/" },
			{ "version" : "/<meta name="generator" content="Jamroom ([\d\.]+)">/" },
		]
	return(self.rules)

