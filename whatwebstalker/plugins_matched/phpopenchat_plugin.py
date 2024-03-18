import plugins
			
class Pluginphpopenchat_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "regexp" : "/<html><body bgcolor="white">[\s]+You don't read the INSTALL instructions!<br>[\s]+Use the <a href="admin\/install\.php">PHPOpenChat-Installer<\/a>[\s]+to install and configure your chat\.[\s]+<\/body><\/html>/" },
			{ "regexp" : "/<html>[\s]+<head>[\s]+<title>PHPOpenChat Installation<\/title>[\s]+<\/head>[\s]+<body>[\s]+<h2>PHPOpenChat Installer<\/h2>[\s]+Step: [\s]+&nbsp;<b><font color="red">1<\/font><\/b>&nbsp;&nbsp;<b>2<\/b>&nbsp;&nbsp;<b>3<\/b>&nbsp;&nbsp;<b>4<\/b>&nbsp;&nbsp;<b>5<\/b>&nbsp;[\s]+<table border=1>[\s]+<form action="install\.php" method="post">/" },
		]
		return(self.rules)

