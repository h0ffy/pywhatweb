import plugins
			
class Pluginonze_miner_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "certainty" : "25", "text" : "<link rel="stylesheet" href="transcriber.css" type="text/css">" },
			{ "version" : "/<tr><td align=center valign=bottom>Version[\s]+([^\s^<]+)<br>[\s]+Copyright/" },
			{ "regexp" : "/&copy; 2004-20[\d]{2} <a href="http:\/\/www\.ling\.canterbury\.ac\.nz\/" target="onze">ONZE Project<\/a> University of Canterbury", "NZ/" },
			{ "text" : "<a href="http://onzeminer.sourceforge.net">ONZE Miner</a> is free software distributed under the terms of the <a href="/miner/gpl.txt" target="license">GNU General Public License</a>" },
		]
		return(self.rules)
