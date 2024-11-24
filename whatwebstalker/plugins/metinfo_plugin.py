import plugins


class Pluginmetinfo_plugin(plugins.Base):
    def __init__(self):
    	pass

    def start(self):
        self.rules = [
			{"regexp": "/<meta name="copyright" content="Copyright 2008 - 20[\d]{2} MetInfo">/" },
			{ "regexp" : "/<meta name="author" content="[^"]+--Powered by MetInfo">/" },
			{ "version" : "/Powered by <a href="http:\/\/www.MetInfo.cn" target="_blank" title="MetInfo enterprise website manager system"><b>[^<]+<\/b><\/a> ([\d\.]+)/" },
		]
	return(self.rules)
