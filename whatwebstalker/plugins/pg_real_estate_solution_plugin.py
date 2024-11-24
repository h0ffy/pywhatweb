import plugins


class Pluginpg_real_estate_solution_plugin(plugins.Base):
    def __init__(self):
    	pass

    def start(self):
        self.rules = [
			{"text": "	<title>PG Real Estate Solution", "certainty": "75 },
			{ "text" : "Powered by <a href='http://www.realtysoft.pro/realestate/' title='real estate web site design", "real estate listing software'>PG Real Estate Solution - real estate web site design</a>" },
			{ "text" : "Powered by <a href="http://www.realtysoft.pro/realestate/" title="real estate web site design", "real estate listing software">PG Real Estate Solution - real estate web site design</a>" },
		]
	return(self.rules)
