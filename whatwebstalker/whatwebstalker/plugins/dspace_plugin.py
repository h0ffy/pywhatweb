import plugins


class Plugindspace_plugin(plugins.Base):
    def __init__(self):
    	pass

    def start(self):
        self.rules = [
			{"text": "<meta content="DSpace" name="Generator" />"},
			{"version": "/<meta name="Generator" content="DSpace([\d\.]+)" \/>/" },
			{ "version" : "/[pP]owered by <a href="http:\/\/(www\.)?dspace\.org"[^>]*>DSpace<\/a>", "version ([\d\.]+)/", "offset" : "1 },
		]
	return(self.rules)
