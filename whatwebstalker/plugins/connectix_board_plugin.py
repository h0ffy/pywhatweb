import plugins
			
class Pluginconnectix_board_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "	<title>Installation de Connectix Boards</title>" },
			{ "text" : "    <title>Connectix Boards - Fatal Error</title>" },
			{ "text" : "	<title>Connectix Boards Error</title>" },
			{ "version" : "/Powered by <a href="http:\/\/www.connectix-boards.org"[^>]*>Connectix Boards<\/a> ([^&]+) &copy; [0-9]{4}-[0-9]{4}/" },
		]
	return(self.rules)
