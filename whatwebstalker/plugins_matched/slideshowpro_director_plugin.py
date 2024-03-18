import plugins
			
class Pluginslideshowpro_director_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "version" : "/<div id="simple-footer">\s+<span>SlideShowPro Director ([^<]+)<\/span>/" },
			{ "text" : "</div> <!--close login-container-->	</body>" },
		]
		return(self.rules)

