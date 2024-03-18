import plugins
			
class Plugintbdev_yse_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<!-- /////// Top Navigation Menu for unregistered-->" },
			{ "text" : "<!-- /////////// here we go", "with the menu //////////// -->" },
			{ "version" : "/Powered by <a href="(http:\/\/)?(www\.tbdev\.net|bit-torrent\.kiev\.ua\/)" target="_blank" style="cursor: help;" title="[^"]*" class="copyright">TBDev<\/a> v([\d\.]+) /", "offset" : "2 },
		]
		return(self.rules)
