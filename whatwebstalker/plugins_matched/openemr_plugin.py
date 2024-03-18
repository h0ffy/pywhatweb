import plugins
			
class Pluginopenemr_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "certainty" : "25", "ghdb" : "inurl:interface/login/login_frame.php filetype:php" },
			{ "regexp" : "/<body ONLOAD="javascript:top\.location\.href='interface\/login\/login_frame\.php(\?site=default)?';">/" },
			{ "version" : "/type="text\/css">[\s]+<\/head>[\s]+<body class="body_title">[\s]+<span class="title_bar">[^<]+ v([^\s^<]+)<\/span><br>/" },
			{ "regexp" : "/<!--<frame src="\/[^\/]+\/interface\/login\/filler\.php" name="Filler Bottom" scrolling="no" noresize frameborder="NO">-->/" },
			{ "certainty" : "75", "search" : "headers[set-cookie]", "regexp" : "/OpenEMR=[^\s]+;/" },
		]
		return(self.rules)
