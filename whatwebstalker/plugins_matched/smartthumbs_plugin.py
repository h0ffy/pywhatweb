import plugins
			
class Pluginsmartthumbs_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "regexp" : "/POWERED[\s]+BY[\s]+<a href="http:\/\/www.smart-scripts.com">SMART THUMBS<\/a>/" },
			{ "text" : "POWERED BY<span> <a href="http://www.thumbsrotator.com"><b><span style="font-size: 11px; font-family: Verdana", "Arial;">SMART THUMBS</span>" },
		]
		return(self.rules)
