import plugins
			
class Pluginjcore_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "version" : "/<script type='text\/javascript'>\s+var JCORE_VERSION = '([^']+)';/" },
			{ "version" : "/<link href='https?:\/\/[^'^\?]+\/static\.php\?request=css(&amp;admin=1)?&amp;[\d]+\-v([\d\.]+)/", "offset" : "1 },
		]
		return(self.rules)

