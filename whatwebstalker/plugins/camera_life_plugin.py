import plugins
			
class Plugincamera_life_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "version" : "/<meta name="generator" content="Camera Life version ([^"]+)">},
			{ "string" : "<a href="http://fulldecent.github.io/cameralife"><i class="fa fa-globe"></i> Built with Camera Life</a>'},
			{ "version" : "/This site is powered by Camera Life version ([^ ]+)},
		]
	return(self.rules)
