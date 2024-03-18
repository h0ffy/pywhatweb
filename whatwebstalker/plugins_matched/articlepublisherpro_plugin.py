import plugins
			
class Pluginarticlepublisherpro_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<script>location.replace("./admin.php?showlogin");</script>" },
			{ "text" : "<title>Article Publisher PRO Administrator Control Panel</title>" },
			{ "text" : "<img src="/images/logo_app.gif"></div></td><td width="60%"><div id="title" class="column">Admin Control Panel</div></td>" },
			{ "text" : "		<form name=fl method=post action=admin.php?login>" },
			{ "text" : "<br><br><center><b>Please use a proper method to browse article(s) - The method you are using is not allowed...</b></center>" },
			{ "version" : "/<div class="powered">Powered by <a href="http:\/\/www.ArticlePublisherPRO.com" target="_blank">Article Publisher PRO<\/a>  v([\d\.]+)/" },
		]
		return(self.rules)
