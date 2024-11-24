import plugins


class Pluginblogn_plus_plugin(plugins.Base):
    def __init__(self):
    	pass

    def start(self):
        self.rules = [
			{"regexp": "/Powered by[\\s]*<a href="http: \/\/www.blogn.org[^>]*>BlognPlus/i },
			{ "version" : "/<meta name="generator"[^>]*content="BlognPlus ([0-9\.]+)/" },
		]
	return(self.rules)
