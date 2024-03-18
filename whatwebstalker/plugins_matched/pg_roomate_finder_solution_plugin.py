import plugins
			
class Pluginpg_roomate_finder_solution_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<div align="center" style="padding-top: 20px; padding-bottom:20px;">Powered by <a href="http://www.realtysoft.pro/roommate/" title="real estate web site design", "real estate listing software">PG Roomate Finder Solution - roommate estate web site design</a></div></td></tr>" },
		]
	return(self.rules)
