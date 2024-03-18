import plugins
			
class Pluginglfusion_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "certainty" : "75", "regexp" : "/<div (class|id)="gl_moomenu1">/" },
			{ "certainty" : "75", "text" : "<ul class="gl_moomenu1">" },
			{ "regexp" : "/Page created in [\d\.]+ seconds( |&nbsp;)by <a href="http:\/\/www.glfusion.org\/"[^>]*>glFusion<\/a>/" },
		]
		return(self.rules)

