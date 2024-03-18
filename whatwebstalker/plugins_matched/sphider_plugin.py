import plugins
			
class Pluginsphider_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "regexp" : "/<html>[\s]+<head>[\s]+<title>[\s]+Sphider installation script\.[\s]+<\/title>[\s]+<LINK REL=STYLESHEET HREF="admin\.css" TYPE="text\/css">[\s]+<\/head>[\s]+<body>/" },
			{ "regexp" : "/<title>Sphider Admin Login<\/title>[\s]+<LINK REL=STYLESHEET HREF="admin\.css" TYPE="text\/css">[\s]+<\/head>/" },
		]
	return(self.rules)
