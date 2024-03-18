import plugins
			
class Pluginteveolive_video_broadcast_software_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[server]", "regexp" : "/^TeveoLive HTTP Server$/" },
			{ "search" : "headers[xvideowidth]", "regexp" : "/^\d+$},
			{ "search" : "headers[xvideoheight]", "regexp" : "/^\d+$},
		]
		return(self.rules)
