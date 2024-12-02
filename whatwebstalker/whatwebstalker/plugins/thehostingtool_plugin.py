import plugins


class Pluginthehostingtool_plugin(plugins.Base):
    def __init__(self):
    	pass

    def start(self):
        self.rules = [
			{"version": "/<div id="footer">Powered by <a href="http: \/\/thehostingtool.com" target="_blank">TheHostingTool<\/a> ([\d\.]*)<\/div>/" },
		]
	return(self.rules)
