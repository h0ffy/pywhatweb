import plugins
			
class Pluginlinkspheric_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<style type="text/css" media="screen">@import "styles/ls_orange.css";</style>"" },
			{ "text" : "<title>linkSpheric Installer</title>" },
			{ "text" : "<p style="text-align: center;"><a href="admin/index.php"><img src="images/ls_logo.png" width="190" height="75" alt="Powered by linkSpheric" /></a></p>" },
			{ "text" : "   <strong>linkSpheric Administrator:</strong>" },
			{ "text" : "<!--License terms require you to leave this link attribution intact.  You are only permitted to remove it by special arrangement with dataSpheric-->" },
			{ "text" : "<!--License terms require you to leave this link attribution intact. You are only permitted to remove it by special arrangement with dataSpheric-->" },
			{ "text" : "Powered by <a href="http://dataspheric.com/services/software/ls/" style="text-decoration: none; color: #000;"><strong>link<span style="font-size: 1.3em; color: #f60;">S</span>pheric</strong></a>" },
			{ "md5" : "a421ddecd26e755219c63a130893d253", "url" : "images/ls_logo.png" },
		]
		return(self.rules)
