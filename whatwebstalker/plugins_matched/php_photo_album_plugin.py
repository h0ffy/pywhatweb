import plugins
			
class Pluginphp_photo_album_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "certainty" : "75", "version" : "/<!--phpalbum ([^\s]+) -->/" },
			{ "text" : "<LINK REL="stylesheet" HREF="main.php?cmd=theme&var1=style_css" TYPE="text/css">" },
			{ "text" : "<font size="2">Powered by </font><a class="me" href="http://www.phpalbum.net"><font size="2">PHP Photo Album</font></a>" },
			{ "text" : "<!-- <font size="2">Powered by <a class="me"href="http://www.phpalbum.net">PHP Photo Album</font></a> -->" },
		]
		return(self.rules)
