import sys
import os
			
class Pluginconnectix_board_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "text" : "	<title>Installation de Connectix Boards</title>" },
			{ "text" : "    <title>Connectix Boards - Fatal Error</title>" },
			{ "text" : "	<title>Connectix Boards Error</title>" },
			{ "version" : "/Powered by <a href="http:\/\/www.connectix-boards.org"[^>]*>Connectix Boards<\/a> ([^&]+) &copy; [0-9]{4}-[0-9]{4}/" },
		]

